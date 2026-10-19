// Threads 對標抓取：Chrome 版（在已登入 Threads 的 Chrome 分頁裡執行）。
// 用法：先打開 https://www.threads.com/@<帳號>，在該分頁執行本檔全文，再呼叫
//   __lusStart('<帳號>', 上限篇數或 0)
// 進度：__lusStatus()；取資料：__lusRows(起始, 筆數) 回傳 TSV 行（欄位同 threads_scrape.py 的 COLUMNS）。
// 只讀：不按讚、不留言、不追蹤、不開私訊；捲動間隔 2–4 秒隨機，每 25 次休息 12–25 秒。
(() => {
  if (window.__lus && window.__lus.hooked) return;
  const S = (window.__lus = { acc: '', posts: {}, profile: null, hasNext: null, done: false,
    running: false, stopReason: '', rateLimited: false, scrolls: 0, hooked: true });

  const URL_RE = /(https?:\/\/\S+|www\.\S+)/g;
  const TAG_RE = /#[^\s#]+/g;
  const pad = n => String(n).padStart(2, '0');
  const fmt = d => `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())} ${pad(d.getUTCHours())}:${pad(d.getUTCMinutes())}`;

  function captionOf(p) {
    if (p.caption && p.caption.text) return p.caption.text;
    const fr = (((p.text_post_app_info || {}).text_fragments || {}).fragments) || [];
    return fr.map(f => (f && f.plaintext) || '').join('');
  }

  function row(p) {
    const info = p.text_post_app_info || {};
    const text = captionOf(p);
    const car = p.carousel_media || [];
    const hasVideo = !!(p.video_versions && p.video_versions.length) || car.some(c => c && c.video_versions && c.video_versions.length);
    let media, count;
    if (car.length) { media = `image x${car.length}`; count = car.length; }
    else if (p.video_versions && p.video_versions.length) { media = 'video'; count = 1; }
    else if (p.image_versions2 && (p.image_versions2.candidates || []).length) { media = 'image x1'; count = 1; }
    else { media = 'text'; count = 0; }
    let links = (text.match(URL_RE) || []).length;
    if (info.link_preview_attachment && !links) links = 1;
    const fr = ((info.text_fragments || {}).fragments) || [];
    const tags = Math.max((text.match(TAG_RE) || []).length, fr.filter(f => f && f.fragment_type === 'hashtag').length);
    const rta = info.reply_to_author;
    const t = new Date(p.taken_at * 1000);
    return {
      code: p.code, utc: fmt(t), taiwan: fmt(new Date(t.getTime() + 8 * 3600e3)),
      likes: p.like_count || 0, replies: info.direct_reply_count || 0,
      reposts: info.repost_count || p.repost_count || 0, media,
      text: text.replace(/\t/g, ' ').replace(/\r/g, '').replace(/\n/g, ' / '),
      carousel_count: count, has_video: hasVideo ? 1 : 0, link_count: links,
      hashtag_count: tags, caption_length: [...text].length,
      reply_to: (rta && rta.username) || '',
      topic_tag: (info.tag_header && info.tag_header.display_name) || '', taken_at: p.taken_at,
    };
  }

  function feed(obj, fromGql) {
    const stack = [obj];
    while (stack.length) {
      const d = stack.pop();
      if (Array.isArray(d)) { for (const x of d) stack.push(x); continue; }
      if (!d || typeof d !== 'object') continue;
      for (const k in d) { const v = d[k]; if (v && typeof v === 'object') stack.push(v); }
      const acc = S.acc.toLowerCase();
      if (!acc) continue;
      if (typeof d.code === 'string' && 'taken_at' in d && d.user && typeof d.user === 'object'
          && ('caption' in d || 'like_count' in d)) {
        if ((d.user.username || '').toLowerCase() === acc && !S.posts[d.code]) {
          try { S.posts[d.code] = row(d); } catch (e) {}
        }
      } else if ((d.username || '').toLowerCase() === acc && 'follower_count' in d) {
        const keep = {};
        for (const k of ['username', 'full_name', 'pk', 'id', 'biography', 'follower_count', 'is_verified', 'bio_links'])
          keep[k] = d[k];
        if (!S.profile || JSON.stringify(keep).length > JSON.stringify(S.profile).length) S.profile = keep;
      }
      if (fromGql && 'has_next_page' in d && !('edges' in d)) S.hasNext = !!d.has_next_page;
    }
  }

  function parseText(txt, fromGql) {
    txt = (txt || '').trim();
    if (txt.startsWith('for (;;);')) txt = txt.slice(9);
    try { feed(JSON.parse(txt), fromGql); return; } catch (e) {}
    for (const line of txt.split('\n')) { try { feed(JSON.parse(line), fromGql); } catch (e) {} }
  }
  S.parseEmbedded = () => document.querySelectorAll('script[type="application/json"]').forEach(s => parseText(s.textContent, false));

  // 攔截分頁回應（只讀副本，不改內容）
  const oOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (m, url) { this.__lusUrl = String(url); return oOpen.apply(this, arguments); };
  const oSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function () {
    if (this.__lusUrl && this.__lusUrl.includes('/graphql')) {
      this.addEventListener('load', () => {
        if (this.status === 429) S.rateLimited = true;
        try { parseText(typeof this.responseText === 'string' ? this.responseText : '', true); } catch (e) {}
      });
    }
    return oSend.apply(this, arguments);
  };
  const oFetch = window.fetch;
  window.fetch = async function (input, init) {
    const res = await oFetch.apply(this, arguments);
    try {
      const url = typeof input === 'string' ? input : (input && input.url) || '';
      if (url.includes('/graphql')) {
        if (res.status === 429) S.rateLimited = true;
        res.clone().text().then(t => parseText(t, true)).catch(() => {});
      }
    } catch (e) {}
    return res;
  };

  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const rand = (a, b) => a + Math.random() * (b - a);

  window.__lusStart = async (acc, max = 0, idleRounds = 8) => {
    if (S.running) return 'already running';
    // 換帳號才清空；同帳號續抓保留已收集的貼文（頁面已載入的批次不會再送一次）
    if (acc !== S.acc) Object.assign(S, { posts: {}, profile: null });
    Object.assign(S, { acc, hasNext: null, done: false, running: true, stop: false,
      stopReason: '', rateLimited: false, scrolls: 0 });
    S.parseEmbedded();
    let idle = 0, last = -1;
    try {
      while (true) {
        const n = Object.keys(S.posts).length;
        if (max && n >= max) { S.stopReason = `max ${max}`; break; }
        if (S.rateLimited) { S.stopReason = '429 rate limited'; break; }
        if (S.stop) { S.stopReason = 'stopped'; break; }
        if (n === last) idle++; else { idle = 0; last = n; }
        if (S.hasNext === false && idle >= 3) { S.stopReason = 'has_next_page=false (reached first post)'; break; }
        if (idle >= idleRounds) { S.stopReason = `no new posts after ${idle} scrolls`; break; }
        window.scrollBy(0, rand(1400, 2600));
        S.scrolls++;
        await sleep(rand(2000, 4000));
        if (idle >= 3) {
          window.scrollBy(0, -rand(300, 600)); await sleep(rand(1000, 2000));
          window.scrollTo(0, document.documentElement.scrollHeight); await sleep(rand(2000, 4000));
        }
        if (S.scrolls % 25 === 0) await sleep(rand(12000, 25000));
      }
    } finally {
      S.running = false; S.done = true;
      // 存到 threads.com 的 localStorage，換頁不會遺失
      try { localStorage.setItem('__lus_' + acc, JSON.stringify({ rows: window.__lusRows(0, 1e6), profile: S.profile, status: window.__lusStatus() })); } catch (e) {}
    }
    return S.stopReason;
  };

  window.__lusStatus = () => {
    const rows = Object.values(S.posts);
    const ts = rows.map(r => r.taiwan).sort();
    return { acc: S.acc, count: rows.length, oldest: ts[0], newest: ts[ts.length - 1], scrolls: S.scrolls,
      hasNext: S.hasNext, running: S.running, done: S.done, stopReason: S.stopReason, rateLimited: S.rateLimited,
      followers: S.profile && S.profile.follower_count };
  };

  const COLS = ['code', 'utc', 'taiwan', 'likes', 'replies', 'reposts', 'media', 'text', 'carousel_count',
    'has_video', 'link_count', 'hashtag_count', 'caption_length', 'reply_to', 'topic_tag'];
  window.__lusRows = (start = 0, n = 50) => Object.values(S.posts)
    .sort((a, b) => b.taken_at - a.taken_at).slice(start, start + n)
    .map(r => COLS.map(c => String(r[c])).join('\t')).join('\n');
  window.__lusProfile = () => JSON.stringify(S.profile);
  window.__lusStop = () => { S.stop = true; return 'stopping'; };
  window.__lusSaved = () => Object.keys(localStorage).filter(k => k.startsWith('__lus_'))
    .map(k => { const v = JSON.parse(localStorage.getItem(k)); return [k.slice(6), v.status.count, v.status.oldest, v.status.stopReason]; });
  // 把貼文存成 <帳號>_posts.tsv 下載（製作師同意後才呼叫）。
  // 不給帳號＝目前頁面；給帳號＝從 localStorage 取（Chrome 會擋同站第二次自動下載，所以全部抓完再一次下載）
  window.__lusDownload = (acc) => {
    const saved = acc ? JSON.parse(localStorage.getItem('__lus_' + acc)) : null;
    const rows = saved ? saved.rows : window.__lusRows(0, 1e6);
    acc = acc || S.acc;
    const body = COLS.join('\t') + '\n' + rows + '\n';
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([body], { type: 'text/tab-separated-values;charset=utf-8' }));
    a.download = `${acc}_posts.tsv`;
    document.body.appendChild(a); a.click(); a.remove();
    return `${a.download}: ${rows.split('\n').length} rows`;
  };
})();
