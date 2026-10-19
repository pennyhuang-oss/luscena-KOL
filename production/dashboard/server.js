// 零依賴靜態伺服器（公開，不設帳密）。Railway 會跑 `npm start`。
// 只供應 index.html、stats.json 和 img/ 底下的大頭照，其餘檔案一律 404。
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const ROOT = __dirname;
const PORT = process.env.PORT || 3000;
const TYPES = { '.jpg': 'image/jpeg', '.png': 'image/png' };

function send(res, code, type, body, cache) {
  res.writeHead(code, { 'Content-Type': type, 'Cache-Control': cache || 'public, max-age=300' });
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
    return fs.readFile(path.join(ROOT, 'index.html'), (err, html) =>
      err ? send(res, 500, 'text/plain; charset=utf-8', 'index.html 讀取失敗')
          : send(res, 200, 'text/html; charset=utf-8', html, 'no-cache'));
  }
  if (urlPath === '/stats.json') {
    return fs.readFile(path.join(ROOT, 'data', 'stats.json'), (err, json) =>
      err ? send(res, 404, 'application/json; charset=utf-8', '{}')
          : send(res, 200, 'application/json; charset=utf-8', json, 'no-cache'));
  }

  const ext = path.extname(urlPath).toLowerCase();
  const file = path.normalize(path.join(ROOT, urlPath));
  if (!urlPath.startsWith('/img/') || !TYPES[ext] || !file.startsWith(path.join(ROOT, 'img') + path.sep)) {
    return send(res, 404, 'text/plain; charset=utf-8', 'Not found');
  }
  fs.readFile(file, (err, data) => (err ? send(res, 404, 'text/plain; charset=utf-8', 'Not found') : send(res, 200, TYPES[ext], data)));
});

server.listen(PORT, () => console.log(`dashboard listening on ${PORT}`));
