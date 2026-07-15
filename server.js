// RINGER — static server + tiny friend-leaderboard API (no deps).
// Scores are stored per (group, UTC-day, player) as JSON on a persistent volume.
const http = require('http');
const fs   = require('fs');
const path = require('path');

const PORT = process.env.PORT || 8080;
const DB   = process.env.DB_PATH || '/data/scores.json';
const ROOT = __dirname;

let store = {};
try { store = JSON.parse(fs.readFileSync(DB, 'utf8')); } catch (e) { store = {}; }
let saveTimer = null;
function save() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    try { fs.mkdirSync(path.dirname(DB), { recursive: true }); fs.writeFileSync(DB, JSON.stringify(store)); }
    catch (e) { console.error('save failed:', e.message); }
  }, 400);
}

const utcDay = () => new Date().toISOString().slice(0, 10);
const cleanGroup = g => (String(g || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 12)) || 'PUBLIC';
const cleanName  = n => (String(n || 'anon').replace(/[<>\n\r\t]/g, '').trim().slice(0, 20)) || 'anon';
const key = (g, d) => g + '|' + d;

function board(g, day, pid) {
  const bucket = store[key(g, day)] || {};
  const all = Object.values(bucket);
  const count = all.length;
  const average = count ? Math.round(all.reduce((a, v) => a + v.score, 0) / count) : 0;
  const rows = Object.entries(bucket)
    .map(([id, v]) => ({ pid: id, name: v.name, score: v.score, level: v.level }))
    .sort((a, b) => b.score - a.score || b.level - a.level)
    .slice(0, 50)
    .map(r => ({ name: r.name, score: r.score, level: r.level, you: r.pid === pid }));
  let rank = null;
  if (pid && bucket[pid] !== undefined) {
    const my = bucket[pid].score;
    rank = 1 + Object.values(bucket).filter(v => v.score > my).length;
  }
  return { group: g, day, count, average, rank, rows };
}

function sendJSON(res, obj, code = 200) {
  const s = JSON.stringify(obj);
  res.writeHead(code, { 'content-type': 'application/json', 'content-length': Buffer.byteLength(s) });
  res.end(s);
}

const MIME = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.js': 'text/javascript', '.css': 'text/css', '.ico': 'image/x-icon', '.svg': 'image/svg+xml' };
function serveStatic(req, res) {
  let p = req.url.split('?')[0];
  if (p === '/' || p === '') p = '/index.html';
  const safe = path.normalize(p).replace(/^(\.\.[\/\\])+/, '');
  const file = path.join(ROOT, safe);
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end('no'); }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404, { 'content-type': 'text/plain' }); return res.end('not found'); }
    res.writeHead(200, { 'content-type': MIME[path.extname(file)] || 'application/octet-stream', 'cache-control': 'no-cache' });
    res.end(buf);
  });
}

const server = http.createServer((req, res) => {
  const u = req.url.split('?')[0];

  if (u === '/api/board' && req.method === 'GET') {
    const q = new URL(req.url, 'http://x').searchParams;
    return sendJSON(res, board(cleanGroup(q.get('group')), utcDay(), String(q.get('pid') || '')));
  }

  if (u === '/api/score' && req.method === 'POST') {
    let body = '', tooBig = false;
    req.on('data', c => { body += c; if (body.length > 4000) { tooBig = true; req.destroy(); } });
    req.on('end', () => {
      if (tooBig) return;
      let b; try { b = JSON.parse(body); } catch (e) { return sendJSON(res, { error: 'bad json' }, 400); }
      const g = cleanGroup(b.group), day = utcDay();
      const pid = String(b.playerId || '').replace(/[^\w-]/g, '').slice(0, 64);
      if (!pid) return sendJSON(res, { error: 'no pid' }, 400);
      const name = cleanName(b.name);
      const score = Math.max(0, Math.min(1000000, Math.floor(Number(b.score) || 0)));
      const level = Math.max(0, Math.min(9999, Math.floor(Number(b.level) || 0)));
      const k = key(g, day);
      const bucket = store[k] || (store[k] = {});
      const prev = bucket[pid];
      if (!prev || score > prev.score) bucket[pid] = { name, score, level, updated: Date.now() };
      else bucket[pid].name = name;               // keep best score, refresh name
      save();
      return sendJSON(res, board(g, day, pid));
    });
    return;
  }

  serveStatic(req, res);
});

server.listen(PORT, () => console.log('ringer listening on', PORT, 'db', DB));
