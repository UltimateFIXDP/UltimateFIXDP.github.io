'use strict';
/**
 * Site behaviour:
 *   1. Language toggle (UA / EN) — applies window.SITE_I18N
 *   2. Pulls the latest release tag from GitHub and updates the download buttons
 *   3. Persists language choice via localStorage
 *   4. Shows the total download count of every release
 */

const REPO = 'LittleBitUA/UltimateFIXDP';

function detectInitialLang() {
  const saved = (function(){ try { return localStorage.getItem('lang'); } catch { return null; } })();
  if (saved === 'uk' || saved === 'en') return saved;
  const nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
  return nav.startsWith('uk') ? 'uk' : 'en';
}

function applyLang(lang) {
  const TR = window.SITE_I18N || {};
  const table = TR[lang] || TR.en || {};
  document.body.dataset.lang = lang;
  document.documentElement.lang = lang === 'uk' ? 'uk' : 'en';

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const k = el.dataset.i18n;
    if (table[k] !== undefined) el.textContent = table[k];
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const k = el.dataset.i18nHtml;
    if (table[k] !== undefined) el.innerHTML = table[k];
  });
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    const k = el.dataset.i18nTitle;
    if (table[k] !== undefined) el.title = table[k];
  });

  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.setLang === lang);
  });

  try { localStorage.setItem('lang', lang); } catch {}
}

async function fetchLatestRelease() {
  try {
    const r = await fetch('https://api.github.com/repos/' + REPO + '/releases/latest', {
      headers: { 'Accept': 'application/vnd.github+json' },
    });
    if (!r.ok) return null;
    const data = await r.json();
    return {
      tag:    data.tag_name,
      name:   data.name,
      url:    data.html_url,
      asset:  (data.assets || []).find(a => /\.zip$/i.test(a.name)),
    };
  } catch { return null; }
}

function setDownloadMeta(release) {
  const metaEl = document.getElementById('download-meta');
  const btnEls = document.querySelectorAll('[id^="download-btn"]');

  if (!release) {
    if (metaEl) metaEl.textContent = '— · Latest';
    return;
  }
  if (metaEl) {
    const sizeMb = release.asset ? (release.asset.size / 1024 / 1024).toFixed(0) + ' MB · ' : '';
    metaEl.textContent = sizeMb + release.tag;
  }
  btnEls.forEach(btn => {
    btn.href = release.asset ? release.asset.browser_download_url : release.url;
  });
}

async function fetchDownloads() {
  try {
    const r = await fetch('https://api.github.com/repos/' + REPO + '/releases?per_page=100', {
      headers: { 'Accept': 'application/vnd.github+json' },
    });
    if (!r.ok) return null;
    const list = await r.json();
    let total = 0;
    for (const rel of list) for (const a of (rel.assets || [])) total += a.download_count || 0;
    return total;
  } catch { return null; }
}

function setDownloads(total) {
  if (total === null || total === undefined) return;
  const el = document.getElementById('downloads');
  const sep = document.getElementById('downloads-sep');
  const count = document.getElementById('downloads-count');
  if (!el || !count) return;
  count.textContent = total.toLocaleString();
  el.hidden = false;
  if (sep) sep.hidden = false;
}

// Cards fade in as they come into view; without IntersectionObserver everything simply shows.
function setupReveal() {
  const els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('shown')); return; }
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('shown'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(e => io.observe(e));
}

// The section in view is lit in the top bar.
function setupActiveNav() {
  const links = [...document.querySelectorAll('.nav a[href^="#"]')];
  const map = new Map(links.map(a => [a.getAttribute('href').slice(1), a]));
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      links.forEach(a => a.classList.remove('active'));
      const a = map.get(en.target.id);
      if (a) a.classList.add('active');
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  map.forEach((a, id) => { const s = document.getElementById(id); if (s) io.observe(s); });
}

// Screenshots open over the page.
function setupLightbox() {
  const box = document.getElementById('lightbox');
  if (!box) return;
  const img = box.querySelector('img');
  document.querySelectorAll('a.zoom').forEach(a => a.addEventListener('click', e => {
    e.preventDefault();
    img.src = a.getAttribute('href');
    img.alt = (a.querySelector('img') || {}).alt || '';
    box.hidden = false;
  }));
  const close = () => { box.hidden = true; img.removeAttribute('src'); };
  box.addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !box.hidden) close(); });
}

// The live F10 menu: sections on the left, switches on the right.
function setupMenu() {
  const fx = document.getElementById('fx');
  if (!fx) return;
  const tabs = [...fx.querySelectorAll('.fx-tab')];
  const panels = [...fx.querySelectorAll('.fx-panel')];
  tabs.forEach(tab => tab.addEventListener('click', () => {
    tabs.forEach(t => { const on = t === tab; t.classList.toggle('active', on); t.setAttribute('aria-selected', on ? 'true' : 'false'); });
    panels.forEach(p => { p.hidden = p.dataset.panel !== tab.dataset.tab; });
  }));
  fx.querySelectorAll('.fx-item').forEach(item => item.addEventListener('click', () => {
    item.setAttribute('aria-pressed', item.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
  }));
}

function setupScrollTop() {
  const btn = document.getElementById('scroll-top');
  if (!btn) return;
  const update = () => btn.classList.toggle('visible', window.scrollY > 400);
  window.addEventListener('scroll', update, { passive: true });
  update();
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

document.addEventListener('DOMContentLoaded', async () => {
  applyLang(detectInitialLang());
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => applyLang(btn.dataset.setLang));
  });
  setupScrollTop();
  setupReveal();
  setupActiveNav();
  setupLightbox();
  setupMenu();
  const [release, downloads] = await Promise.all([fetchLatestRelease(), fetchDownloads()]);
  setDownloadMeta(release);
  setDownloads(downloads);
});
