import { chromium } from 'playwright';
import http from 'http';
import { createReadStream, existsSync, statSync } from 'fs';
import path from 'path';

function serve(root, port) {
  const types = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.otf':'font/otf','.mp4':'video/mp4','.webmanifest':'application/manifest+json','.ico':'image/x-icon','.pdf':'application/pdf'};
  return new Promise(res => {
    const s = http.createServer((req, rsp) => {
      let p = decodeURIComponent(req.url.split('?')[0]);
      if (p.endsWith('/')) p += 'index.html';
      let f = path.join(root, p);
      if (!existsSync(f) || statSync(f).isDirectory()) { rsp.writeHead(404); rsp.end(); return; }
      rsp.writeHead(200, {'content-type': types[path.extname(f)] || 'application/octet-stream'});
      createReadStream(f).pipe(rsp);
    }).listen(port, '127.0.0.1', () => res(s));
  });
}

const [legacySrv, newSrv] = await Promise.all([serve('/home/claude/maverix-legacy', 4501), serve('/home/claude/maverix-astro/dist', 4502)]);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage();
// block third-party (consent scripts etc.)
await page.route(/^(?!http:\/\/127\.0\.0\.1)/, r => r.abort());
const targets = [
  ['legacy-home-1440','http://127.0.0.1:4501/index.html',1440],
  ['new-home-1440','http://127.0.0.1:4502/index.html',1440],
  ['legacy-diag-1440','http://127.0.0.1:4501/diagnostics.html',1440],
  ['new-diag-1440','http://127.0.0.1:4502/diagnostics.html',1440],
  ['legacy-team-390','http://127.0.0.1:4501/team.html',390],
  ['new-team-390','http://127.0.0.1:4502/team.html',390],
];
for (const [name, url, w] of targets) {
  await page.setViewportSize({ width: w, height: 1000 });
  await page.goto(url, { waitUntil: 'networkidle' }).catch(()=>{});
  await page.addStyleTag({ content: '*{animation:none!important;transition:none!important}.reveal-on-scroll{opacity:1!important;transform:none!important}' }).catch(()=>{});
  await page.evaluate(() => document.querySelectorAll('.reveal-on-scroll').forEach(e => e.classList.add('is-in-view'))).catch(()=>{});
  await page.waitForTimeout(300);
  await page.screenshot({ path: `/tmp/${name}.png`, fullPage: true });
  console.log(name, 'ok');
}
await browser.close(); legacySrv.close(); newSrv.close();
