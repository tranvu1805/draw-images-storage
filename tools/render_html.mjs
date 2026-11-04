// Render src/theory_review/<id>.html fragments to work/raw/<id>.png with KaTeX.
// Usage: node tools/render_html.mjs img188 img189 …   (no ids = every .html source)
// The fragment is placed inside <div id="root">; math in $…$ (inline) or $$…$$ (display).
// Optional first-line comment <!-- width: 300 --> overrides the final width (read by build.py).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import puppeteer from 'puppeteer-core';

const TOOLS = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.dirname(TOOLS);
const SRC = path.join(REPO, 'src', 'theory_review');
const RAW = path.join(REPO, 'work', 'raw');
fs.mkdirSync(RAW, { recursive: true });
const katex = pathToFileURL(path.join(TOOLS, 'node_modules', 'katex', 'dist')).href;

let ids = process.argv.slice(2);
if (!ids.length) ids = fs.readdirSync(SRC).filter(f => f.endsWith('.html')).map(f => f.slice(0, -5));

const page = (body) => `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="${katex}/katex.min.css">
<script src="${katex}/katex.min.js"></script>
<script src="${katex}/contrib/mhchem.min.js"></script>
<script src="${katex}/contrib/auto-render.min.js"></script>
<style>
  html,body{margin:0;background:#fff}
  #root{display:inline-block;padding:6px 8px;font-family:"Times New Roman",serif;font-size:20px;color:#111;line-height:1.35}
  .katex{font-size:1.05em}
  table{border-collapse:collapse}
  td,th{border:1px solid #111;padding:4px 10px;text-align:center;font-weight:normal}
  th{font-weight:bold}
  .left{text-align:left}
  .nob td{border:none}
</style></head><body><div id="root">${body}</div>
<script>
  renderMathInElement(document.getElementById('root'), {delimiters:[
    {left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}], throwOnError:false});
  document.fonts.ready.then(()=>{document.body.dataset.ready='1'});
</script></body></html>`;

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  headless: true,
  args: ['--no-first-run', '--allow-file-access-from-files'],
  userDataDir: path.join(REPO, 'work', 'chrome-profile'),
});
const tab = await browser.newPage();
await tab.setViewport({ width: 1600, height: 1200, deviceScaleFactor: 3 });
const tmp = path.join(REPO, 'work', 'page.html');
for (const id of ids) {
  const body = fs.readFileSync(path.join(SRC, `${id}.html`), 'utf8');
  fs.writeFileSync(tmp, page(body));
  await tab.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
  await tab.waitForSelector('body[data-ready="1"]', { timeout: 10000 });
  const el = await tab.$('#root');
  await el.screenshot({ path: path.join(RAW, `${id}.png`), omitBackground: false });
  console.log('rendered', id);
}
await browser.close();
