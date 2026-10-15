// 零依賴靜態檔案伺服器（公開，不設帳密）。Railway 會跑 `npm start`。
// 只供應 index.html 和 img/ 底下的圖片，其餘檔案（含本檔、package.json）一律 404。
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = __dirname;
const PORT = process.env.PORT || 3000;

// index.html 是 claude.ai artifact 的片段（沒有 doctype／head），這裡補上外殼，避免瀏覽器進入 quirks mode。
const SHELL_HEAD =
  '<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">' +
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">' +
  '</head><body style="margin:0">';
const SHELL_TAIL = '</body></html>';

const TYPES = {
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.png': 'image/png',
  '.webp': 'image/webp',
};

function send(res, code, type, body) {
  res.writeHead(code, { 'Content-Type': type, 'Cache-Control': 'public, max-age=300' });
  res.end(body);
}

const server = http.createServer((req, res) => {
  let urlPath;
  try {
    urlPath = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  } catch {
    return send(res, 400, 'text/plain; charset=utf-8', 'Bad request');
  }

  if (urlPath === '/' || urlPath === '/index.html') {
    fs.readFile(path.join(ROOT, 'index.html'), 'utf8', (err, html) => {
      if (err) return send(res, 500, 'text/plain; charset=utf-8', 'index.html 讀取失敗');
      send(res, 200, 'text/html; charset=utf-8', SHELL_HEAD + html + SHELL_TAIL);
    });
    return;
  }

  // 只允許 /img/ 底下、副檔名在白名單內的檔案
  const ext = path.extname(urlPath).toLowerCase();
  const file = path.normalize(path.join(ROOT, urlPath));
  if (!urlPath.startsWith('/img/') || !TYPES[ext] || !file.startsWith(path.join(ROOT, 'img') + path.sep)) {
    return send(res, 404, 'text/plain; charset=utf-8', 'Not found');
  }
  fs.readFile(file, (err, data) => {
    if (err) return send(res, 404, 'text/plain; charset=utf-8', 'Not found');
    send(res, 200, TYPES[ext], data);
  });
});

server.listen(PORT, () => console.log(`catalog listening on ${PORT}`));
