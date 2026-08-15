import { chromium } from 'playwright';
import http from 'http';
import { createReadStream, existsSync, statSync } from 'fs';
import path from 'path';

function serve(root, port) {
  const types = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.otf':'font/otf','.mp4':'video/mp4','.ico':'image/x-icon'};
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

const srv = await serve('dist', 4510);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const results = [];
const check = (name, cond) => results.push([name, cond ? 'PASS' : 'FAIL']);
const errs = [];

// Desktop context
let page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
page.on('pageerror', e => errs.push('pageerror: ' + e.message));
page.on('console', m => { if (m.type() === 'error' && !m.text().includes('net::')) errs.push('console: ' + m.text()); });
await page.route(/^(?!http:\/\/127\.0\.0\.1)/, r => r.abort());

// 1. TabBar on video page
await page.goto('http://127.0.0.1:4510/products/ebus-needles.html', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(400);
check('tab: features active initially', await page.$eval('#pane-features', el => el.classList.contains('is-active')));
await page.click('button[aria-controls="pane-videos"]');
check('tab: videos activates on click', await page.$eval('#pane-videos', el => el.classList.contains('is-active')));
check('tab: features deactivates', await page.$eval('#pane-features', el => !el.classList.contains('is-active')));

// 2. BioModal on team page (all 12)
await page.goto('http://127.0.0.1:4510/team.html', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(600);
const memberCount = (await page.$$('.member')).length;
check('team: 12 member cards', memberCount === 12);
let modalsOk = 0;
for (let i = 0; i < memberCount; i++) {
  const members = await page.$$('.member');
  await members[i].click();
  await page.waitForTimeout(120);
  const open = await page.$('.modal.open');
  if (open) {
    const overflow = await page.evaluate(() => document.body.style.overflow);
    const focusInClose = await page.evaluate(() => document.activeElement?.classList.contains('close'));
    await page.keyboard.press('Escape');
    await page.waitForTimeout(120);
    const closed = !(await page.$('.modal.open'));
    const overflowRestored = await page.evaluate(() => document.body.style.overflow === '');
    if (open && overflow === 'hidden' && focusInClose && closed && overflowRestored) modalsOk++;
  }
}
check(`team: modals open/escape-close (${modalsOk}/12)`, modalsOk === 12);
// overlay close
await (await page.$$('.member'))[0].click(); await page.waitForTimeout(120);
await page.$eval('.modal.open .overlay', el => el.click()); await page.waitForTimeout(120);
check('team: overlay click closes', !(await page.$('.modal.open')));

// 3. Stat count-up on homepage
await page.goto('http://127.0.0.1:4510/', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(300);
await page.evaluate(() => document.querySelector('.statgrid')?.scrollIntoView());
await page.waitForTimeout(1600);
const stats = await page.$$eval('.stat-number', els => els.map(e => e.textContent));
check('home: stats present (8)', stats.length >= 8);
check('home: >63% intact after animation', stats.some(s => s === '>63%'));
check('home: 10–20% intact', stats.some(s => s === '10–20%'));
check('home: 2.5M intact', stats.some(s => s === '2.5M'));

// 4. Mobile menu
page = await browser.newPage({ viewport: { width: 390, height: 800 } });
page.on('pageerror', e => errs.push('mobile pageerror: ' + e.message));
await page.route(/^(?!http:\/\/127\.0\.0\.1)/, r => r.abort());
await page.goto('http://127.0.0.1:4510/', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(600);
await page.click('.hamburger');
await page.waitForTimeout(150);
check('mobile: menu opens', await page.$eval('.nav-links', el => el.classList.contains('open')));
check('mobile: aria-expanded true', await page.$eval('.hamburger', el => el.getAttribute('aria-expanded') === 'true'));
await page.click('.nav-links > div:first-child a.nav-top-link');
await page.waitForTimeout(150);
check('mobile: products accordion opens', await page.$eval('.nav-links > div:first-child', el => el.classList.contains('sub-open')));
await page.keyboard.press('Escape');
await page.waitForTimeout(150);
check('mobile: Escape closes menu', await page.$eval('.nav-links', el => !el.classList.contains('open')));
// pathcard tap-expand
await page.evaluate(() => document.querySelector('.pathcard')?.scrollIntoView());
await page.waitForTimeout(400);
await page.click('.pathcard');
await page.waitForTimeout(200);
check('mobile: pathcard tap-expands', await page.$eval('.pathcard', el => el.classList.contains('open')));
// diagnostics photo-card expand
await page.goto('http://127.0.0.1:4510/diagnostics.html', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(600);
await page.evaluate(() => document.querySelector('.photo-card')?.scrollIntoView());
await page.waitForTimeout(300);
await page.click('.photo-card');
await page.waitForTimeout(200);
check('mobile: photo-card tap-expands', await page.$eval('.photo-card', el => el.classList.contains('open')));
// spec-hint visible on mobile product page
await page.goto('http://127.0.0.1:4510/products/ebus-needles.html', { waitUntil: 'networkidle' }).catch(()=>{});
await page.waitForTimeout(400);
check('mobile: spec-hint visible', await page.$eval('.spec-hint', el => getComputedStyle(el).display !== 'none'));
// overflow scan
for (const url of ['/', '/serpex.html', '/diagnostics.html', '/products/ebus-needles.html', '/careers.html']) {
  await page.goto('http://127.0.0.1:4510' + url, { waitUntil: 'networkidle' }).catch(()=>{});
  await page.waitForTimeout(300);
  const ovf = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  check(`mobile: no h-overflow ${url}`, !ovf);
}

console.log('\n=== RESULTS ===');
for (const [n, r] of results) console.log(r, '-', n);
console.log('failures:', results.filter(r => r[1] === 'FAIL').length);
console.log('js errors:', errs.length ? errs.slice(0,5) : 'none');
await browser.close(); srv.close();
