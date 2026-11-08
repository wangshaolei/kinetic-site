// 首页动效，照搬设计稿 rep-counter/docs/site-redesign/index.html。
// 界面文字由页面里的 window.KI18N 提供（build.py 按语言生成），这里不写死英文。
(function(){
  const T = window.KI18N || {};
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* stagger hero words */
  document.querySelectorAll('.hero .split span').forEach((s, i) => { if (!s.classList.contains('l2')) s.style.animationDelay = (0.1 + i * 0.09) + 's'; });

  const railLinks = [...document.querySelectorAll('.rail a')], navLinks = [...document.querySelectorAll('.nav ul a')];

  /* ---------- skeleton math (side-view squat) ---------- */
  function squatPose(s, ax, ay, sc) {           // s: 0 standing → 1 deepest
    const a = 26 * s * Math.PI / 180, b = 64 * s * Math.PI / 180, c = 36 * s * Math.PI / 180;
    const L1 = 62 * sc, L2 = 62 * sc, LT = 74 * sc;
    const K = [ax + L2 * Math.sin(a), ay - L2 * Math.cos(a)];
    const H = [K[0] - L1 * Math.sin(b), K[1] - L1 * Math.cos(b)];
    const S = [H[0] + LT * Math.sin(c), H[1] - LT * Math.cos(c)];
    const head = [S[0] + 8 * sc * Math.sin(c), S[1] - 22 * sc];
    const W = [S[0] + 48 * sc * Math.cos(c * .3), S[1] + 14 * sc];
    const v1 = [ax - K[0], ay - K[1]], v2 = [H[0] - K[0], H[1] - K[1]];
    const ang = Math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (Math.hypot(...v1) * Math.hypot(...v2))) * 180 / Math.PI;
    return { A: [ax, ay], K, H, S, head, W, ang };
  }
  const f = (p) => p[0].toFixed(1) + ' ' + p[1].toFixed(1);
  function skelSVG(p, sc, kneeColor) {
    return `<path d="M${f(p.A)} L${f(p.K)} L${f(p.H)} L${f(p.S)} M${f(p.S)} L${f(p.W)} M${f(p.A)} L${p.A[0] + 22 * sc} ${p.A[1]}"/>` +
      `<circle cx="${p.head[0].toFixed(1)}" cy="${p.head[1].toFixed(1)}" r="${12 * sc}"/>` +
      [p.K, p.H, p.S].map((q, i) => `<circle cx="${q[0].toFixed(1)}" cy="${q[1].toFixed(1)}" r="${5 * sc}" fill="#0A1016" stroke-width="3" ${i === 0 && kneeColor ? `stroke="${kneeColor}"` : ''}/>`).join('');
  }
  // squat depth over time: hold, down, hold, up
  const depth = (t) => { const ph = (t % 2.6) / 2.6; if (ph < .2) return 0; if (ph < .5) return .5 - .5 * Math.cos((ph - .2) / .3 * Math.PI); if (ph < .62) return 1; if (ph < .9) return .5 + .5 * Math.cos((ph - .62) / .28 * Math.PI); return 0; };

  /* ---------- section observers ---------- */
  const visible = new Set();
  const once = new Set();
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      const fx = e.target.dataset.fx;
      if (e.isIntersecting) {
        e.target.classList.add('in'); visible.add(fx);
        if (!once.has(fx)) { once.add(fx); start[fx] && start[fx](); }
        const id = e.target.id; railLinks.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + id));
        navLinks.forEach(a => a.classList.toggle('on', a.getAttribute('href') === '#' + id));
      } else visible.delete(fx);
    });
  }, { threshold: .28 });
  document.querySelectorAll('.sec').forEach(s => io.observe(s));

  const countUp = (el, to, ms, fmt) => {
    if (reduce) { el.textContent = fmt ? fmt(to) : to; return; }
    const t0 = performance.now();
    const step = (t) => { const k = Math.max(0, Math.min(1, (t - t0) / ms)); const v = Math.round(to * (1 - Math.pow(1 - k, 3))); el.textContent = fmt ? fmt(v) : v; if (k < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  };

  /* ---------- HERO: live squat counter ---------- */
  const heroSkel = document.getElementById('heroSkel'), heroN = document.getElementById('heroN'), heroA = document.getElementById('heroA'),
        heroPill = document.getElementById('heroPill'), heroVf = document.getElementById('heroVf'), heroPlus = document.getElementById('heroPlus'), heroProg = document.getElementById('heroProg');
  let heroCount = 0, heroDown = false;
  /* ---------- HOW: gauge ---------- */
  const gArc = document.getElementById('gArc'), gArcBg = document.getElementById('gArcBg'), gSkel = document.getElementById('gSkel'),
        gDeg = document.getElementById('gDeg'), gCnt = document.getElementById('gCnt'), gTicks = document.getElementById('gTicks'), steps = [...document.querySelectorAll('#steps li')];
  let gCount = 0, gDown = false;
  const GA = [300, 430], GSC = 1.9;

  function arcPath(cx, cy, r, a0, a1) { // degrees, 0 = right, counter-clockwise visual (svg y down)
    const p = (a) => [cx + r * Math.cos(a * Math.PI / 180), cy - r * Math.sin(a * Math.PI / 180)];
    const s = p(a0), e = p(a1), large = Math.abs(a1 - a0) > 180 ? 1 : 0, sweep = a1 > a0 ? 0 : 1;
    return `M${f(s)} A${r} ${r} 0 ${large} ${sweep} ${f(e)}`;
  }

  function frame(now) {
    const t = now / 1000;
    if (visible.has('hero') || !once.has('hero')) {
      const p = squatPose(reduce ? .6 : depth(t), 150, 420, 1.45);
      heroSkel.innerHTML = skelSVG(p, 1.45);
      const ang = Math.round(p.ang);
      heroA.textContent = T.knee + ' ' + ang + '°';
      const deep = ang <= 110;
      heroVf.classList.toggle('y', !deep && ang < 150 && heroDown === false && depth(t) > .4);
      if (deep && !heroDown) { heroDown = true; heroPill.textContent = T.deep; }
      if (heroDown && ang >= 160) {
        heroDown = false; heroCount = heroCount >= 30 ? 1 : heroCount + 1; heroN.textContent = heroCount;
        heroN.classList.remove('pop'); void heroN.offsetWidth; heroN.classList.add('pop');
        heroPlus.classList.remove('go'); void heroPlus.offsetWidth; heroPlus.classList.add('go');
        heroPill.textContent = T.good; heroProg.style.width = (heroCount / 30 * 100) + '%';
      }
      if (!heroDown && ang < 160 && ang > 110) heroPill.textContent = T.lower;
    }
    if (visible.has('how')) {
      const p = squatPose(reduce ? .7 : depth(t + .3), GA[0], GA[1], GSC);
      gSkel.innerHTML = skelSVG(p, GSC, '#2EE6FF');
      const ang = p.ang, K = p.K;
      // arc between shin (down) and thigh directions around the knee
      const dirA = Math.atan2(-(p.A[1] - K[1]), p.A[0] - K[0]) * 180 / Math.PI;
      const dirH = Math.atan2(-(p.H[1] - K[1]), p.H[0] - K[0]) * 180 / Math.PI;
      let a0 = dirA, a1 = dirH; if (a1 < a0) a1 += 360;
      if (a1 - a0 > 180) { const tmp = a0; a0 = a1; a1 = tmp + 360; }
      gArcBg.setAttribute('d', arcPath(K[0], K[1], 70, a0, a0 + 180));
      gArc.setAttribute('d', arcPath(K[0], K[1], 70, a0, a0 + ang));
      const col = ang <= 110 ? '#3DFF8C' : ang >= 160 ? '#2EE6FF' : '#FFD23D';
      gArc.setAttribute('stroke', col); gArc.style.filter = `drop-shadow(0 0 8px ${col})`;
      gDeg.textContent = Math.round(ang) + '°'; gDeg.style.color = col;
      gTicks.innerHTML = [110, 160].map(v => { const a = (a0 + v) * Math.PI / 180, r1 = 58, r2 = 92; return `<line x1="${K[0] + r1 * Math.cos(a)}" y1="${K[1] - r1 * Math.sin(a)}" x2="${K[0] + r2 * Math.cos(a)}" y2="${K[1] - r2 * Math.sin(a)}" stroke="${v === 110 ? '#3DFF8C' : '#2EE6FF'}" stroke-width="2" stroke-dasharray="4 3"/><text x="${K[0] + 108 * Math.cos(a) - 14}" y="${K[1] - 108 * Math.sin(a) + 4}" fill="${v === 110 ? '#3DFF8C' : '#2EE6FF'}">${v}°</text>`; }).join('');
      const s = ang >= 160 && !gDown ? 0 : (ang <= 110 || gDown) && ang < 160 ? 1 : 2;
      if (ang <= 110) gDown = true;
      if (gDown && ang >= 160) { gDown = false; gCount++; gCnt.textContent = gCount; steps.forEach((li, i) => li.classList.toggle('act', i === 2)); }
      else steps.forEach((li, i) => li.classList.toggle('act', i === (gDown ? 1 : (ang >= 160 ? 0 : 1))));
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);


  const start = {
    ex() { countUp(document.getElementById('exCount'), 11, 900); },
    cal() {
      const days = document.getElementById('calDays'), missed = [3, 6, 7, 9, 11, 12];
      let html = '<span></span><span></span><span></span>';
      for (let d = 1; d <= 31; d++) html += `<span class="d${d === 24 ? ' today' : ''}" data-d="${d}">${d}</span>`;
      days.innerHTML = html;
      const cells = [...days.querySelectorAll('.d')];
      cells.forEach((c, i) => {
        const d = i + 1; if (d > 24) { c.style.opacity = '.4'; return; }
        setTimeout(() => {
          if (missed.includes(d)) c.classList.add('miss');
          else { c.classList.add('on' + (1 + (d * 7) % 4), 'pop'); setTimeout(() => c.classList.remove('pop'), 300); }
        }, reduce ? 0 : 200 + i * 55);
      });
      setTimeout(() => {
        countUp(document.getElementById('calStreak'), 12, 900);
        countUp(document.getElementById('calMonth'), 18, 900);
        countUp(document.getElementById('calTotal'), 3500, 1200, (v) => v.toLocaleString(T.locale));
      }, reduce ? 0 : 600);
      setTimeout(() => document.getElementById('calBadge').classList.add('show'), reduce ? 0 : 1900);
    },
    guest() {
      const sw = document.getElementById('modeSw'), lab = document.getElementById('swLabel'), g = document.getElementById('mGuest'), m = document.getElementById('mIn');
      const set = (on) => { sw.setAttribute('aria-checked', on); lab.textContent = on ? T.signedIn : T.guest; g.classList.toggle('act', !on); g.classList.toggle('dim', on); m.classList.toggle('act', on); m.classList.toggle('dim', !on); };
      set(false);
      let user = false;
      sw.addEventListener('click', () => { user = true; set(sw.getAttribute('aria-checked') !== 'true'); });
      if (!reduce) { let on = false; const tick = () => { if (user) return; if (visible.has('guest')) { on = !on; set(on); } setTimeout(tick, 2200); }; setTimeout(tick, 1200); }
    },
    setup() { document.getElementById('setup').classList.add('in'); }
  };
})();

// 宣传视频：点击后才换成 youtube-nocookie 播放器（不点不连 YouTube）
document.querySelectorAll('.promo .yt').forEach(b => b.addEventListener('click', () => {
  const f = document.createElement('iframe');
  f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0&playsinline=1';
  f.title = b.getAttribute('aria-label');
  f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
  f.allowFullscreen = true;
  f.referrerPolicy = 'strict-origin-when-cross-origin';
  b.replaceWith(f);
}));
