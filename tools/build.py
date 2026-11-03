"""生成 KINETIC 主站的全部静态页面。

    python3 tools/build.py [App 的 l10n 目录]

默认 l10n 目录是 ../rep-counter/app/lib/l10n（两个仓库放在同一个上级目录时）。

- 隐私政策、用户协议的正文直接取自 App 的多语言文件（app_*.arb），保证网页和 App 内一致。
- 首页、动作页、指南、常见问题的文案在 tools/content.py、tools/guides.py。
- 首页样式和动效照搬设计稿 rep-counter/docs/site-redesign/index.html（assets/site.css、assets/home.js）。

网址：英文在根目录（/、/privacy.html…），简体中文在 /zh/，繁体中文在 /zh-hant/。
根目录的 /privacy.html、/delete-account.html 被 Google Play 后台和 App 引用，不能改名或删除。
"""

import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content import (  # noqa: E402
    APP_NAME, DESC, ENTITY, EXERCISES, EXP, FAQ, FAQP, HOME, JOINT, JOINT_DEF, POSTURE, SIDES, UI,
)
from compare import APPS, CHECKED, TH  # noqa: E402
from guides import BEGINNER_PLAN, GUIDE_UI, GUIDES  # noqa: E402
from legal_text import LEGAL  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
L10N = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "rep-counter/app/lib/l10n"

# 和 App 里 AppLegal 保持一致（app/lib/domain/models/app_links.dart）
OPERATOR = "shaolei wang"
EMAIL = "leishaolen@gmail.com"
EFFECTIVE_DATE = "2026-10-28"
POLICY_VERSION = "1.1"
REPLY_DAYS = 7
YEAR = 2026

# 内容页的「最后更新」和 sitemap 的 lastmod。改了页面内容时一起改。
UPDATED = "2026-11-03"

# 正式版上架后改成 True：「即将上架」换成 Google Play 下载按钮。
# 有 assets/badges/google-play-{en,zh,hant}.png 时用图片，没有时用文字按钮。图片是 Google 官方徽章
# （play.google.com/intl/en_us/badges/static/images/badges/{en,zh-cn,zh-tw}_badge_web_generic.png），
# 只裁掉了四周的透明边，三种语言的徽章才一样大；按徽章规范不能改色、变形。
PLAY_LIVE = True

BASE = "https://kinetic.lencoder.com"
PLAY = "https://play.google.com/store/apps/details?id=com.lencoder.sport.ai"

LANGS = ("en", "zh", "hant")
ARB = {
    lang: json.loads((L10N / f).read_text(encoding="utf-8"))
    for lang, f in {"en": "app_en.arb", "zh": "app_zh.arb", "hant": "app_zh_Hant.arb"}.items()
}
PREFIX = {"en": "", "zh": "/zh", "hant": "/zh-hant"}
HREFLANG = {"en": "en", "zh": "zh-Hans", "hant": "zh-Hant"}
OG_LOCALE = {"en": "en_US", "zh": "zh_CN", "hant": "zh_TW"}
# 本地化图片找不到时按顺序退回（繁中没有专门的分享图时用简中的）
ASSET_DIRS = {"en": [""], "zh": ["zh/", ""], "hant": ["zh-hant/", "zh/", ""]}

SITEMAP: list[str] = []


# ---------------------------------------------------------------- 工具函数

def esc(s: str) -> str:
    return html.escape(s, quote=True)


def arb(lang: str, key: str, **args) -> str:
    """取 App 文案并转义；占位符在转义后替换（值里不含 HTML）。"""
    s = html.escape(ARB[lang][key], quote=False)
    for k, v in args.items():
        s = s.replace("{" + k + "}", esc(str(v)))
    return s


def fill(s: str, **args) -> str:
    for k, v in args.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def tr(d: dict, lang: str, **args) -> str:
    return fill(d[lang], **args)


def href(lang: str, key: str) -> str:
    """站内链接。key 为空是首页，以 / 结尾是目录页。"""
    return PREFIX[lang] + "/" + key


def absurl(lang: str, key: str) -> str:
    return BASE + href(lang, key)


def asset(lang: str, name: str) -> str:
    for d in ASSET_DIRS[lang]:
        if (ROOT / "assets" / (d + name)).exists():
            return "/assets/" + d + name
    raise FileNotFoundError(name)


def play_url(lang: str, medium: str) -> str:
    # Play 管理中心「获取报告」按 utm_source 统计官网带来的安装
    return f"{PLAY}&referrer=utm_source%3Dwebsite%26utm_medium%3D{medium}%26utm_content%3D{lang}"


def get_button(lang: str, medium: str) -> str:
    if not PLAY_LIVE:
        return f'<span class="soon"><i></i>{UI["soon"][lang]}</span>'
    url = esc(play_url(lang, medium))
    badge = ROOT / "assets/badges" / f"google-play-{lang}.png"
    if badge.exists():
        return (f'<a class="play-badge" href="{url}"><img src="/assets/badges/{badge.name}" '
                f'alt="{esc(UI["get"][lang])}" width="188" height="56"></a>')
    return f'<a class="btn btn-pri" href="{url}">{UI["get"][lang]}</a>'


def ld(obj: dict) -> str:
    text = json.dumps(obj, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{text}\n</script>'


def author() -> dict:
    return {"@type": "Person", "name": OPERATOR}


def breadcrumbs(lang: str, items: list[tuple[str, str]]) -> tuple[str, str]:
    """返回（页面上的面包屑 HTML，BreadcrumbList 结构化数据）。最后一项是当前页。"""
    trail = [(UI["home"][lang], "")] + items
    links = []
    for i, (name, key) in enumerate(trail):
        links.append(name if i == len(trail) - 1 else f'<a href="{href(lang, key)}">{name}</a>')
    data = ld({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": html.unescape(name), "item": absurl(lang, key)}
            for i, (name, key) in enumerate(trail)
        ],
    })
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" <span>›</span> ".join(links)}</nav>', data


def article_ld(lang: str, key: str, title: str, desc: str) -> str:
    return ld({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": html.unescape(title),
        "description": html.unescape(desc),
        "inLanguage": HREFLANG[lang],
        "author": author(),
        "dateModified": UPDATED,
        "mainEntityOfPage": absurl(lang, key),
        "about": {"@type": "MobileApplication", "name": APP_NAME["en"]},
    })


def meta_block(lang: str) -> str:
    return (f'<div class="meta"><p>{UI["updated"][lang]}: {UPDATED} · {UI["author"][lang]}: {OPERATOR}</p>'
            f'<p>{UI["not_medical"][lang]}</p></div>')


def cta_box(lang: str, medium: str) -> str:
    return f'<div class="cta-box"><p>{UI["cta_line"][lang]}</p>{get_button(lang, medium)}</div>'


# ---------------------------------------------------------------- 页面骨架

BRAND_SVG = (
    '<svg width="26" height="34" viewBox="32 22 48 64" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<circle cx="44" cy="33" r="6.5" stroke="#C6FF3D" stroke-width="5"/>'
    '<path d="M45 41 L50 57 L72 62 L62 80 M47 46 L64 44" stroke="#C6FF3D" stroke-width="5"/>'
    '<path d="M65.2 60.4 A7 7 0 0 1 68.6 67.6" stroke="#2EE6FF" stroke-width="2.2" stroke-dasharray="2.4 2"/>'
    '<g fill="#06080B" stroke="#C6FF3D" stroke-width="2.4"><circle cx="50" cy="57" r="3.5"/><circle cx="72" cy="62" r="3.5"/><circle cx="62" cy="80" r="3.5"/></g></svg>'
)

# 旧版网址用 ?lang=zh / ?lang=hant 选语言，可能已经被别人收藏或转发，跳到对应的中文网址
OLD_LANG_PARAM = (
    "<script>(function(){var m=/[?&]lang=(zh|hant)(&|$)/.exec(location.search);"
    "if(m)location.replace((m[1]==='zh'?'/zh':'/zh-hant')+location.pathname+location.hash);})();</script>"
)
OLD_LANG_PAGES = ("", "privacy.html", "terms.html", "delete-account.html")


def layout(lang: str, key: str, *, title: str, desc: str, body: str, home: bool = False,
           head_extra: str = "", og_title: str | None = None, og_desc: str | None = None,
           og_type: str = "article", scripts: str = "", sitemap: bool = True) -> None:
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{absurl(l, key)}">' for l in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{absurl("en", key)}">'
    nav_items = [
        (UI["nav_how"][lang], "#how" if home else href(lang, "") + "#how"),
        (UI["nav_ex"][lang], href(lang, "exercises/")),
        (UI["nav_privacy"][lang], "#privacy" if home else href(lang, "") + "#privacy"),
        (UI["nav_guides"][lang], href(lang, "guides/")),
        (UI["nav_faq"][lang], href(lang, "faq/")),
    ]
    nav = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in nav_items)
    # 404 页只有英文一份，语言按钮指向各语言首页
    switch_key = "" if key == "404.html" else key
    if key == "404.html":
        alternates = ""
    current = ' aria-current="page"'
    langs = "".join(
        f'<a href="{href(l, switch_key)}" lang="{HREFLANG[l]}"{current if l == lang else ""}>{n}</a>'
        for l, n in (("en", "EN"), ("zh", "简"), ("hant", "繁"))
    )
    langbar = ""
    if lang == "en":
        langbar = (
            '<div class="langbar" id="langbar">'
            f'<span data-v="zh" hidden>{fill(UI["langbar_zh"]["en"], u=href("zh", switch_key))}</span>'
            f'<span data-v="hant" hidden>{fill(UI["langbar_hant"]["en"], u=href("hant", switch_key))}</span></div>'
        )
    footer_links = [
        (UI["nav_ex"][lang], "exercises/"), (UI["nav_guides"][lang], "guides/"), (UI["nav_faq"][lang], "faq/"),
        (UI["privacy"][lang], "privacy.html"), (UI["terms"][lang], "terms.html"), (UI["delete"][lang], "delete-account.html"),
    ]
    footer = "".join(f'<a href="{href(lang, k)}">{t}</a>' for t, k in footer_links)
    doc = f"""<!doctype html>
<html lang="{HREFLANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{OLD_LANG_PARAM if lang == "en" and key in OLD_LANG_PAGES else ""}
<title>{esc(html.unescape(title))}</title>
<meta name="description" content="{esc(html.unescape(desc))}">
<link rel="canonical" href="{absurl(lang, key)}">
{alternates}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="KINETIC">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta property="og:url" content="{absurl(lang, key)}">
<meta property="og:title" content="{esc(html.unescape(og_title or title))}">
<meta property="og:description" content="{esc(html.unescape(og_desc or desc))}">
<meta property="og:image" content="{BASE}{asset(lang, "og-1200x630.png")}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#06080B">
<link rel="icon" href="/assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{head_extra}
</head>
<body>
<a class="skip" href="#main">{UI["skip"][lang]}</a>
<div class="progress" aria-hidden="true"></div>
{langbar}
<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="{href(lang, "")}" aria-label="KINETIC">{BRAND_SVG}KINETIC<b>//</b></a>
    <ul>{nav}</ul>
    <nav class="langs" aria-label="{UI["lang_label"][lang]}">{langs}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <span>© {YEAR} KINETIC · {UI["operated"][lang]} {OPERATOR}</span>
    <nav aria-label="Footer">{footer}</nav>
  </div>
</footer>
<script src="/assets/site.js"></script>
{scripts}
</body>
</html>
"""
    doc = "\n".join(line for line in doc.split("\n") if line.strip() != "")
    path = ROOT / PREFIX[lang].lstrip("/") / (key + "index.html" if key == "" or key.endswith("/") else key)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc + "\n", encoding="utf-8")
    if sitemap and lang == "en":
        SITEMAP.append(key)


# ---------------------------------------------------------------- 动作卡片和判定文字

def rule_parts(e: dict, lang: str) -> tuple[str, str]:
    """卡片上的「≤ 110°」「≥ 160°」。"""
    if not e["two"]:
        return f"≤ {e['done']}°", UI["single"][lang]
    if e["ext"]:
        return f"≥ {e['done']}°", f"≤ {e['start']}°"
    return f"≤ {e['done']}°", f"≥ {e['start']}°"


def rule_text(e: dict, lang: str) -> str:
    k = "rule_single" if not e["two"] else "rule_ext" if e["ext"] else "rule_flex"
    return tr(EXP[k], lang, done=e["done"], start=e["start"])


def ex_vars(e: dict, lang: str) -> dict:
    name = e["name"][lang]
    plural = e["plural"][lang]
    return {
        "name": name,
        "name_l": name.lower() if lang == "en" else name,
        "plural": plural,
        "Plural": plural[:1].upper() + plural[1:] if lang == "en" else plural,
        "joint": JOINT[e["joint"]][lang],
        "joint_l": JOINT[e["joint"]][lang].lower() if lang == "en" else JOINT[e["joint"]][lang],
        "done": e["done"],
        "start": e["start"],
    }


def ex_card(e: dict, lang: str, i: int) -> str:
    k, second = rule_parts(e, lang)
    v = ex_vars(e, lang)
    return f"""<a class="ex" href="{href(lang, "exercises/" + e["slug"] + "/")}" style="transition-delay:{i * 0.06:.2f}s">
  <div class="top"><span class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 20h16M4 20L16 6M10 20a6 6 0 0 0-2-4.5"/></svg></span><span class="code">{e["code"]}</span></div>
  <h3>{tr(EXP["h1"], lang, **v)[:1].upper() + tr(EXP["h1"], lang, **v)[1:]}</h3>
  <div class="rule"><span>{v["joint"]}</span><span class="k">{k}</span><span>{second}</span></div>
  <span class="mono" style="font-size:12px;color:var(--text3)">{POSTURE[e["posture"]]["short"][lang]}</span>
  <span class="go">{UI["how_go"][lang]}</span>
</a>"""


def faq_items(lang: str, only: list[str] | None = None) -> list[tuple[str, str]]:
    items = []
    for fid, qa in FAQ:
        if only is None or fid in only:
            q, a = qa[lang]
            items.append((q, fill(a, p=PREFIX[lang])))
    return items


def faq_html(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="ans">{a}</div></details>'
        for i, (q, a) in enumerate(items)
    )


def faq_ld(lang: str, items: list[tuple[str, str]]) -> str:
    def plain(s: str) -> str:
        import re
        return html.unescape(re.sub(r"<[^>]+>", "", s))
    return ld({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": HREFLANG[lang],
        "mainEntity": [
            {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
            for q, a in items
        ],
    })


# ---------------------------------------------------------------- 首页

def app_ld(lang: str) -> str:
    return ld({
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": APP_NAME["en"],
        "alternateName": ["KINETIC", APP_NAME["zh"], APP_NAME["hant"]],
        "operatingSystem": "Android",
        "applicationCategory": "HealthApplication",
        "inLanguage": ["en", "zh-Hans", "zh-Hant"],
        "description": ENTITY[lang],
        "url": absurl(lang, ""),
        "installUrl": PLAY,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Person", "name": OPERATOR, "email": EMAIL},
        "screenshot": [BASE + asset(lang, f"shot-{i}.jpg") for i in range(1, 5)],
    })


def home(lang: str) -> None:
    H = {k: v[lang] for k, v in HOME.items()}
    line1, line2 = H["h1"]
    h1 = " ".join(f"<span>{w}</span>" for w in line1) + '<span class="l2">' + " ".join(f"<span>{w}</span>" for w in line2) + "</span>"
    facts = "".join(f"<span>{f}</span>" for f in H["facts"])
    steps = "".join(f'<li data-s="{i}"><div><b>{a}</b><span>{b}</span></div></li>' for i, (a, b) in enumerate(H["how_steps"]))
    keep = "".join(f'<div class="rv d{i + 1}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate(H["priv_keep"]))
    icons = [("rgba(198,255,61,.12)", "var(--lime)", "▦"), ("rgba(255,138,61,.14)", "var(--orange)", "◆"), ("rgba(46,230,255,.12)", "var(--cyan)", "▣")]
    feat = "".join(
        f'<div class="rv d{i + 2}"><i style="background:{bg};color:{c}">{ic}</i><div><b>{a}</b><span>{b}</span></div></div>'
        for i, ((a, b), (bg, c, ic)) in enumerate(zip(H["track_feat"], icons))
    )

    def lis(items: list[str]) -> str:
        return "".join(f'<li class="x">{s[2:]}</li>' if s.startswith("x:") else f"<li>{s}</li>" for s in items)

    rot = ["-3deg", "2deg", "-2deg", "3deg"]
    shots = "".join(
        f'<figure style="--r:{rot[i]};transition-delay:{0.05 + i * 0.1:.2f}s"><img src="{asset(lang, f"shot-{i + 1}.jpg")}" width="540" height="960" loading="lazy" alt="{esc(alt)}"><figcaption>{cap}</figcaption></figure>'
        for i, (cap, alt) in enumerate(H["shots"])
    )
    cards = "\n".join(ex_card(e, lang, i) for i, e in enumerate(EXERCISES))
    home_faq = faq_items(lang, ["how", "video", "off", "signin", "newphone"])
    p = PREFIX[lang]

    body = f"""
<nav class="rail" aria-label="Sections">
  <a href="#top" aria-label="Top"></a><a href="#how" aria-label="{esc(UI["nav_how"][lang])}"></a><a href="#exercises" aria-label="{esc(UI["nav_ex"][lang])}"></a>
  <a href="#privacy" aria-label="{esc(UI["nav_privacy"][lang])}"></a><a href="#track" aria-label="{esc(H["track_eyebrow"])}"></a><a href="#guest" aria-label="{esc(H["guest_eyebrow"])}"></a>
  <a href="#setup" aria-label="{esc(H["setup_eyebrow"])}"></a><a href="#screens" aria-label="{esc(H["shots_eyebrow"])}"></a><a href="#faq" aria-label="{esc(UI["nav_faq"][lang])}"></a><a href="#get" aria-label="{esc(UI["get"][lang])}"></a>
</nav>

<section class="hero sec" id="top" data-fx="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">{H["eyebrow"]}</p>
      <h1 class="split" style="margin-top:16px">{h1}</h1>
      <p class="lead intro rv d2">{ENTITY[lang]}</p>
      <div class="cta rv d3">
        {get_button(lang, "hero")}
        <a class="btn btn-sec" href="#how">{H["see_how"]}</a>
      </div>
      <div class="facts rv d4">{facts}</div>
    </div>
    <div class="phone" role="img" aria-label="{esc(H["phone_aria"])}">
      <div class="grid"></div>
      <div class="vf" id="heroVf">
        <div class="edge"></div><div class="run"><i></i></div>
        <div class="cn tl"></div><div class="cn tr"></div><div class="cn bl"></div><div class="cn br"></div>
        <svg class="skel" viewBox="0 0 272 474" aria-hidden="true"><g id="heroSkel" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" style="color:var(--c);filter:drop-shadow(0 0 7px currentColor)"></g></svg>
        <div class="hud"><span class="n" id="heroN">0</span><div class="a" id="heroA">{H["js"]["knee"]} 180°</div></div>
        <div class="plus1" id="heroPlus">+1</div>
        <div class="pill" id="heroPill">{H["tracking"]}</div>
      </div>
      <div class="prog"><i id="heroProg"></i></div>
      <div class="bar"><span></span><span></span><span class="p"></span></div>
    </div>
  </div>
</section>

<section class="how sec" id="how" data-fx="how">
  <div class="wrap">
    <div>
      <p class="eyebrow rv">{H["how_eyebrow"]}</p>
      <h2 class="rv d1" style="margin-top:14px">{H["how_h2"]}</h2>
      <p class="lead rv d2" style="margin-top:18px">{H["how_lead"]}</p>
      <ol class="steps rv d3" id="steps">{steps}</ol>
    </div>
    <div class="gauge rv d2">
      <div class="deg"><b id="gDeg">180°</b><span>{H["knee_angle"]}</span></div>
      <div class="cnt"><b id="gCnt">0</b><span class="mono" style="display:block;font-size:12px;color:var(--text3)">{H["reps"]}</span></div>
      <svg viewBox="0 0 500 500" aria-hidden="true">
        <g stroke="#1C2530" stroke-width="1"><line x1="40" y1="440" x2="460" y2="440"/></g>
        <path id="gArcBg" fill="none" stroke="#1C2530" stroke-width="14" stroke-linecap="round"/>
        <path id="gArc" fill="none" stroke="#2EE6FF" stroke-width="14" stroke-linecap="round" style="filter:drop-shadow(0 0 8px #2EE6FF)"/>
        <g id="gTicks" font-family="JetBrains Mono" font-size="13"></g>
        <g id="gSkel" fill="none" stroke="#E8F0F2" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"></g>
      </svg>
    </div>
  </div>
</section>

<section class="sec" id="exercises" data-fx="ex">
  <div class="wrap">
    <p class="eyebrow rv">{H["ex_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["ex_h2"]}</h2>
    <div class="tally rv d2"><b id="exCount">0</b><p class="lead" style="max-width:520px">{H["ex_lead"]}</p></div>
    <div class="ex-grid" id="exGrid">
{cards}
    </div>
  </div>
</section>

<section class="priv sec" id="privacy" data-fx="priv">
  <div class="wrap">
    <p class="eyebrow rv">{H["priv_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["priv_h2"]}</h2>
    <p class="lead rv d2" style="margin-top:18px">{H["priv_lead"]}</p>
    <div class="stage rv d3" aria-label="{esc(H["priv_aria"])}" role="img">
      <div class="pkt"></div><div class="pkt"></div><div class="pkt"></div>
      <div class="dev"><div class="ph"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#C6FF3D" stroke-width="1.8" aria-hidden="true"><path d="M3 8h3l2-3h8l2 3h3v12H3zM12 17a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"/></svg></div>{H["priv_dev"]}</div>
      <div class="wall"></div>
      <div class="cloud"><svg width="96" height="64" viewBox="0 0 24 16" fill="none" stroke="#8A9AA6" stroke-width="1.2" aria-hidden="true"><path d="M6 15h12a4 4 0 0 0 .5-8A6 6 0 0 0 7 6a4.5 4.5 0 0 0-1 9z"/><path d="M9 7l6 6M15 7l-6 6" stroke="#FF6B7F"/></svg>{H["priv_cloud"]}</div>
    </div>
    <div class="keep">{keep}</div>
    <p class="rv d4" style="margin-top:22px"><a href="{p}/guides/on-device-pose-detection/">{H["priv_more"]}</a></p>
  </div>
</section>

<section class="track sec" id="track" data-fx="cal">
  <div class="wrap">
    <div class="cal rv" aria-label="{esc(H["cal_aria"])}" role="img">
      <div class="hd"><span style="font-weight:700">{H["cal_title"]}</span><b>2026.10</b></div>
      <div class="days" id="calDays"></div>
      <div class="ft">
        <div><span>{H["cal_streak"]}</span><b style="color:var(--orange)" id="calStreak">0</b></div>
        <div><span>{H["cal_month"]}</span><b style="color:var(--lime)" id="calMonth">0</b></div>
        <div><span>{H["cal_total"]}</span><b style="color:var(--cyan)" id="calTotal">0</b></div>
      </div>
      <div class="badge" id="calBadge">
        <svg width="44" height="48" viewBox="0 0 56 62" fill="rgba(198,255,61,.12)" stroke="#C6FF3D" stroke-width="3" aria-hidden="true"><polygon points="28,2 54,17 54,45 28,60 2,45 2,17"/><path d="M18 31l7 7 13-14" fill="none"/></svg>
        <div><b>{H["badge_t"]}</b><span style="display:block;color:var(--text2);font-size:14px">{H["badge_b"]}</span></div>
      </div>
    </div>
    <div>
      <p class="eyebrow rv">{H["track_eyebrow"]}</p>
      <h2 class="rv d1" style="margin-top:14px">{H["track_h2"]}</h2>
      <p class="lead rv d2" style="margin-top:18px">{H["track_lead"]}</p>
      <div class="feat">{feat}</div>
    </div>
  </div>
</section>

<section class="guest sec" id="guest" data-fx="guest">
  <div class="wrap">
    <p class="eyebrow rv">{H["guest_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["guest_h2"]}</h2>
    <p class="lead rv d2" style="margin-top:18px">{H["guest_lead"]}</p>
    <div class="box rv d3">
      <div class="mode" id="mGuest"><h3>{H["guest_t"]}</h3><ul>{lis(H["guest_list"])}</ul></div>
      <div class="sw"><button type="button" role="switch" aria-checked="false" aria-label="{esc(H["in_t"])}" id="modeSw"><i></i></button><span id="swLabel">{H["js"]["guest"]}</span></div>
      <div class="mode" id="mIn"><h3>{H["in_t"]}</h3><ul>{lis(H["in_list"])}</ul></div>
    </div>
  </div>
</section>

<section class="setup sec" id="setup" data-fx="setup">
  <div class="wrap">
    <p class="eyebrow rv">{H["setup_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["setup_h2"]}</h2>
    <p class="lead rv d2" style="margin-top:18px">{H["setup_lead"]}</p>
    <div class="cards">
      <div class="card rv d2">
        <h3>{H["setup_sq_t"]} <span>SQUAT</span></h3>
        <svg viewBox="0 0 320 150" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-label="{esc(H["setup_sq_aria"])}" role="img">
          <path class="draw" d="M10 136H310" stroke="#2A3542" stroke-width="2"/>
          <g stroke="#C6FF3D" stroke-width="3"><rect class="draw" x="34" y="70" width="22" height="40" rx="4"/><path class="draw" d="M45 110V134M36 134H54"/></g>
          <path class="draw" d="M56 76L218 22M56 104L218 134" stroke="#2EE6FF" stroke-width="1.5" stroke-dasharray="4 4"/>
          <g stroke="#E8F0F2" stroke-width="3"><circle class="draw" cx="240" cy="30" r="8"/><path class="draw" d="M240 38V80M226 50H254M240 80L228 106L232 134M240 80L252 106L248 134"/></g>
          <text x="146" y="128" text-anchor="middle" fill="#C9D4DB" font-family="Inter" font-size="12">2–3 m</text>
        </svg>
        <p>{H["setup_sq_b"]}</p>
      </div>
      <div class="card rv d3">
        <h3>{H["setup_pu_t"]} <span style="background:var(--lime)">PUSH-UP</span></h3>
        <svg viewBox="0 0 320 150" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-label="{esc(H["setup_pu_aria"])}" role="img">
          <path class="draw" d="M10 130H310" stroke="#2A3542" stroke-width="2"/>
          <g stroke="#E8F0F2" stroke-width="3"><circle class="draw" cx="150" cy="80" r="7"/><path class="draw" d="M158 84L258 104L292 120M162 86L166 106L160 128"/></g>
          <g stroke="#C6FF3D" stroke-width="3"><rect class="draw" x="30" y="98" width="18" height="30" rx="3"/></g>
          <path class="draw" d="M48 102L140 66M48 126L296 126" stroke="#2EE6FF" stroke-width="1.5" stroke-dasharray="4 4"/>
          <text x="98" y="118" text-anchor="middle" fill="#C9D4DB" font-family="Inter" font-size="12">~1.5 m</text>
        </svg>
        <p>{H["setup_pu_b"]}</p>
      </div>
    </div>
    <p class="rv d4" style="margin-top:22px"><a href="{p}/guides/phone-placement/">{UI["all_placement"][lang]}</a></p>
  </div>
</section>

<section class="shots sec" id="screens" data-fx="shots">
  <div class="wrap">
    <p class="eyebrow rv">{H["shots_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["shots_h2"]}</h2>
    <div class="reel" tabindex="0" aria-label="{esc(H["shots_aria"])}">{shots}</div>
  </div>
</section>

<section class="sec" id="faq" data-fx="faq">
  <div class="wrap">
    <p class="eyebrow rv">{H["faq_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{H["faq_h2"]}</h2>
    <div class="faq-list rv d2">
{faq_html(home_faq)}
    </div>
    <p class="rv d3" style="margin-top:22px"><a href="{p}/faq/">{UI["all_faq"][lang]}</a></p>
  </div>
</section>

<section class="cta-sec sec" id="get" data-fx="cta">
  <span class="ring" aria-hidden="true"></span><span class="ring" aria-hidden="true"></span><span class="ring" aria-hidden="true"></span>
  <div class="wrap" style="position:relative">
    <p class="eyebrow rv">{H["cta_eyebrow"]}</p>
    <h2 class="rv d1" style="margin-top:14px">{" ".join(line1)}<br><span style="color:var(--lime)">{" ".join(line2)}</span></h2>
    <p class="lead rv d2">{H["cta_lead"]}</p>
    <div class="cta rv d3">{get_button(lang, "footer")}</div>
    <p class="contact rv d4">{fill(H["contact"], e=EMAIL, d=REPLY_DAYS)}</p>
  </div>
</section>
"""
    if lang != "en":
        body = body.replace('style="margin-top:16px">', 'style="margin-top:16px;letter-spacing:0">', 1)
    i18n = json.dumps(H["js"], ensure_ascii=False)
    layout(
        lang, "", title=H["title"], desc=DESC[lang], body=body, home=True, og_type="website",
        og_title=H["og_title"], og_desc=H["og_desc"],
        head_extra=app_ld(lang) + "\n" + faq_ld(lang, home_faq),
        scripts=f"<script>window.KI18N={i18n};</script>\n<script src=\"/assets/home.js\"></script>",
    )


# ---------------------------------------------------------------- 动作页

def exercise_page(e: dict, lang: str) -> None:
    v = ex_vars(e, lang)
    key = f"exercises/{e['slug']}/"
    # 英文标题用首字母大写（Overhead Press Counter），正文保持句首大写
    title = tr(EXP["title"], lang, **({**v, "name": v["name"].title(), "Plural": v["plural"].title()} if lang == "en" else v))
    h1 = tr(EXP["h1"], lang, **v)
    h1 = h1[:1].upper() + h1[1:]
    desc = tr(EXP["desc"], lang, rule=rule_text(e, lang), **v)
    ans_key = "ans_single" if not e["two"] else "ans_ext" if e["ext"] else "ans_flex"
    ans = tr(EXP[ans_key], lang, **v)
    if lang == "en":
        ans = ans[:1].upper() + ans[1:]
    posture = POSTURE[e["posture"]]
    k, second = rule_parts(e, lang)
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["nav_ex"][lang], "exercises/"), (h1, key)])
    how = tr(EXP["measured"], lang, **{**v, "def": JOINT_DEF[e["joint"]][lang]}) + e["std"][lang]
    how_extra = EXP["single_note"][lang] if not e["two"] else SIDES[e["sides"]][lang]
    shot = ""
    if e["id"] == "squat":
        shot = f'<img class="shot" src="{asset(lang, "shot-2.jpg")}" width="540" height="960" loading="lazy" alt="{esc(tr(EXP["shot_alt"], lang, **v))}">'
    steps = "".join(f"<li>{s}</li>" for s in posture["steps"][lang])
    tips = "".join(f"<li>{s}</li>" for s in e["tips"][lang])
    miss = "".join(f"<li>{s}</li>" for s in e["miss"][lang] + EXP["miss_common"][lang])
    others = "".join(
        f'<a href="{href(lang, "exercises/" + o["slug"] + "/")}">{tr(EXP["h1"], lang, **ex_vars(o, lang))[:1].upper() + tr(EXP["h1"], lang, **ex_vars(o, lang))[1:]}<span>{JOINT[o["joint"]][lang]} {rule_parts(o, lang)[0]}</span></a>'
        for o in EXERCISES if o is not e
    )
    body = f"""
<article class="page">
{crumbs}
<p class="eyebrow">{e["code"]} · AI REP COUNTER</p>
<h1>{h1}</h1>
<div class="answer"><p>{ans} {posture["title"][lang]}{"." if lang == "en" else "。"}</p></div>
<div class="spec">
  <div><span>{EXP["spec_joint"][lang]}</span><b class="c">{v["joint"]}</b></div>
  <div><span>{EXP["spec_done"][lang]}</span><b>{k}</b></div>
  <div><span>{EXP["spec_start"][lang]}</span><b class="c">{second}</b></div>
  <div><span>{EXP["spec_phone"][lang]}</span><b class="c" style="font-size:16px">{posture["short"][lang]}</b></div>
</div>
<h2>{tr(EXP["h_how"], lang, **v)}</h2>
{shot}
<p>{how}</p>
<p>{how_extra}</p>
<h2>{EXP["h_setup"][lang]}</h2>
<ol>{steps}</ol>
<p><a href="{PREFIX[lang]}/guides/phone-placement/">{UI["all_placement"][lang]}</a></p>
<h2>{EXP["h_form"][lang]}</h2>
<ul>{tips}</ul>
<h2>{EXP["h_miss"][lang]}</h2>
<ul>{miss}</ul>
<h2>{EXP["h_adjust"][lang]}</h2>
<p>{EXP["adjust"][lang]}</p>
{cta_box(lang, "exercise")}
<h2>{EXP["h_more"][lang]}</h2>
<div class="related">{others}</div>
{meta_block(lang)}
</article>
"""
    layout(lang, key, title=title, desc=desc, body=body,
           head_extra=crumbs_ld + "\n" + article_ld(lang, key, title, desc))


def exercises_hub(lang: str) -> None:
    key = "exercises/"
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["nav_ex"][lang], key)])
    cards = "\n".join(ex_card(e, lang, 0) for e in EXERCISES)
    body = f"""
<div class="page wide">
{crumbs}
<p class="eyebrow">AI REP COUNTER</p>
<h1>{EXP["hub_h1"][lang]}</h1>
<p class="lead" style="margin-top:18px">{EXP["hub_lead"][lang]}</p>
<div class="ex-grid">
{cards}
</div>
{cta_box(lang, "exercises")}
</div>
"""
    layout(lang, key, title=EXP["hub_title"][lang], desc=EXP["hub_desc"][lang], body=body, og_type="website",
           head_extra=crumbs_ld)


# ---------------------------------------------------------------- 指南

def placement_table(lang: str) -> str:
    rows = "".join(
        f'<tr><td><a href="{href(lang, "exercises/" + e["slug"] + "/")}">{e["name"][lang]}</a></td>'
        f'<td>{POSTURE[e["posture"]]["short"][lang]}</td><td>{JOINT[e["joint"]][lang]} {rule_parts(e, lang)[0]}</td></tr>'
        for e in EXERCISES
    )
    return (f'<div class="tbl-wrap"><table class="tbl"><tr><th>{GUIDE_UI["th_ex"][lang]}</th>'
            f'<th>{GUIDE_UI["th_phone"][lang]}</th><th>{GUIDE_UI["th_rule"][lang]}</th></tr>{rows}</table></div>')


def posture_sections(lang: str) -> str:
    out = []
    for pid, p in POSTURE.items():
        if pid == "lying":
            continue
        users = [e for e in EXERCISES if POSTURE[e["posture"]] is p]
        names = "、".join(e["name"][lang] for e in users) if lang != "en" else ", ".join(e["name"][lang] for e in users)
        steps = "".join(f"<li>{s}</li>" for s in p["steps"][lang])
        out.append(f'<h3>{p["title"][lang]}</h3><p><b>{GUIDE_UI["used_by"][lang]}</b>: {names}</p><ol>{steps}</ol>')
    return "\n".join(out)


def squat_plan(lang: str) -> str:
    cells, reps = [], 20
    for day in range(1, 31):
        if day % 4 == 0:
            cells.append(f'<td><b>{day}</b><br>{GUIDE_UI["rest"][lang]}</td>')
        else:
            cells.append(f"<td><b>{day}</b><br>{reps}</td>")
            reps += 5
    rows = "".join("<tr>" + "".join(cells[i:i + 6]) + "</tr>" for i in range(0, 30, 6))
    return f'<div class="tbl-wrap"><table class="tbl" style="text-align:center">{rows}</table></div>'


def beginner_plan(lang: str) -> str:
    by_id = {e["id"]: e for e in EXERCISES}
    weeks = len(BEGINNER_PLAN[0][1])
    head = (f'<th>{GUIDE_UI["th_ex"][lang]}</th><th>{GUIDE_UI["th_phone"][lang]}</th>'
            + "".join(f'<th>{tr(GUIDE_UI["week"], lang, n=i + 1)}</th>' for i in range(weeks)))
    rows = []
    for ex_id, plan in BEGINNER_PLAN:
        e = by_id[ex_id]
        name = f'<a href="{href(lang, "exercises/" + e["slug"] + "/")}">{e["name"][lang]}</a>'
        if ex_id == "lunge":
            name += f'<br><small>{GUIDE_UI["lunge_note"][lang]}</small>'
        cells = "".join(
            "<td>—</td>" if w is None else f"<td>{w[0]} × {w[1]}<br><small>= {w[0] * w[1]}</small></td>"
            for w in plan
        )
        rows.append(f'<tr><td>{name}</td><td>{POSTURE[e["posture"]]["short"][lang]}</td>{cells}</tr>')
    return f'<div class="tbl-wrap"><table class="tbl plan"><tr>{head}</tr>{"".join(rows)}</table></div>'


def compare_table(lang: str) -> str:
    cols = ("platform", "price", "exercises", "video", "data", "extras")
    head = "".join(f"<th>{TH[c][lang]}</th>" for c in ("app",) + cols)
    rows = []
    for a in APPS:
        # 对方的商店页加 nofollow：只是引用出处，不给对方传递权重
        link = (f'<a href="{href(lang, "")}">{esc(a["name"])}</a>' if a["url"] is None
                else f'<a href="{esc(a["url"])}" rel="nofollow noopener">{esc(a["name"])}</a>')
        cells = "".join(f"<td>{a[c][lang]}</td>" for c in cols)
        rows.append(f'<tr><td><b>{link}</b><br><small>{esc(a["dev"])}</small></td>{cells}</tr>')
    return f'<div class="tbl-wrap wide"><table class="tbl cmp"><tr>{head}</tr>{"".join(rows)}</table></div>'


def guide_page(g: dict, lang: str) -> None:
    key = f"guides/{g['slug']}/"
    title, desc = g["title"][lang], g["desc"][lang]
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["nav_guides"][lang], "guides/"), (g["h1"][lang], key)])
    content = fill(g["body"][lang], p=PREFIX[lang])
    if "{table}" in content:
        content = fill(content, table=placement_table(lang), postures=posture_sections(lang))
    if "{plan}" in content:
        content = fill(content, plan=squat_plan(lang))
    if "{beginner}" in content:
        content = fill(content, beginner=beginner_plan(lang))
    if "{compare}" in content:
        content = fill(content, compare=compare_table(lang), checked=CHECKED, e=EMAIL)
    related = "".join(
        f'<a href="{href(lang, "guides/" + o["slug"] + "/")}">{o["h1"][lang]}<span>{o["card"][lang]}</span></a>'
        for o in GUIDES if o is not g
    )
    body = f"""
<article class="page">
{crumbs}
<p class="eyebrow">GUIDE</p>
<h1>{g["h1"][lang]}</h1>
<div class="answer"><p>{g["answer"][lang]}</p></div>
{content}
{cta_box(lang, "guide")}
<h2>{UI["nav_guides"][lang]}</h2>
<div class="related">{related}</div>
{meta_block(lang)}
</article>
"""
    layout(lang, key, title=title, desc=desc, body=body,
           head_extra=crumbs_ld + "\n" + article_ld(lang, key, title, desc))


def guides_hub(lang: str) -> None:
    key = "guides/"
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["nav_guides"][lang], key)])
    cards = "".join(
        f'<a href="{href(lang, "guides/" + g["slug"] + "/")}">{g["h1"][lang]}<span>{g["card"][lang]}</span></a>'
        for g in GUIDES
    )
    body = f"""
<div class="page">
{crumbs}
<p class="eyebrow">GUIDES</p>
<h1>{GUIDE_UI["hub_h1"][lang]}</h1>
<p class="lead" style="margin-top:18px">{GUIDE_UI["hub_desc"][lang]}</p>
<div class="related" style="margin-top:30px">{cards}</div>
{cta_box(lang, "guides")}
</div>
"""
    layout(lang, key, title=GUIDE_UI["hub_title"][lang], desc=GUIDE_UI["hub_desc"][lang], body=body,
           og_type="website", head_extra=crumbs_ld)


# ---------------------------------------------------------------- 常见问题

def faq_page(lang: str) -> None:
    key = "faq/"
    items = faq_items(lang)
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["nav_faq"][lang], key)])
    body = f"""
<div class="page">
{crumbs}
<p class="eyebrow">FAQ</p>
<h1>{FAQP["h1"][lang]}</h1>
<div class="faq-list">
{faq_html(items)}
</div>
<p style="margin-top:22px">{fill(FAQP["more"][lang], e=EMAIL)}</p>
{cta_box(lang, "faq")}
</div>
"""
    layout(lang, key, title=FAQP["title"][lang], desc=FAQP["desc"][lang], body=body, og_type="website",
           head_extra=crumbs_ld + "\n" + faq_ld(lang, items))


# ---------------------------------------------------------------- 隐私政策、用户协议、删除账号

def legal_footer(lang: str) -> str:
    return (f'<p class="meta">{arb(lang, "legalEffective", date=EFFECTIVE_DATE)} · '
            f'{arb(lang, "legalOperator", name=OPERATOR)}</p>')


def privacy(lang: str) -> None:
    sections = []
    for i in range(1, 9):
        body = arb(lang, "prvS8Body", email=EMAIL, days=REPLY_DAYS) if i == 8 else arb(lang, f"prvS{i}Body")
        warn = f'<p class="warn-text">{arb(lang, "prvS6Warn")}</p>' if i == 6 else ""
        extra = f"<p>{LEGAL['delete_hint'][lang]}</p>" if i == 7 else ""
        sections.append(f'<div class="sect"><h3>{arb(lang, f"prvS{i}Title")}</h3><p>{body}</p>{warn}{extra}</div>')
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["privacy"][lang], "privacy.html")])
    body = f"""
<div class="page">
{crumbs}
<p class="eyebrow">PRIVACY · v{POLICY_VERSION}</p>
<h1>{arb(lang, "prvTitle")}</h1>
<p style="margin-top:14px">{fill(LEGAL["same_as_app"][lang], v=POLICY_VERSION)}</p>
<div class="box hero"><h3>{arb(lang, "prvHeroTitle")}</h3><p>{arb(lang, "prvHeroBody")}</p></div>
<div class="cols2">
<div class="box ok"><h3>{arb(lang, "prvKeepTitle")}</h3><p class="lines">{arb(lang, "prvKeepBody")}</p></div>
<div class="box no"><h3>{arb(lang, "prvNeverTitle")}</h3><p class="lines">{arb(lang, "prvNeverBody")}</p></div>
</div>
{"".join(sections)}
{legal_footer(lang)}
</div>
"""
    layout(lang, "privacy.html", title=f"{UI['privacy'][lang]} · KINETIC", desc=ARB[lang]["prvHeroBody"],
           body=body, head_extra=crumbs_ld)


def terms(lang: str) -> None:
    sections = []
    for i in range(1, 9):
        if i == 6:
            body = arb(lang, "trmS6Body", company=OPERATOR)
        elif i == 8:
            body = arb(lang, "trmS8Body", email=EMAIL)
        else:
            body = arb(lang, f"trmS{i}Body")
        sections.append(f'<div class="sect"><h3>{arb(lang, f"trmS{i}Title")}</h3><p>{body}</p></div>')
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["terms"][lang], "terms.html")])
    body = f"""
<div class="page">
{crumbs}
<p class="eyebrow">TERMS · v{POLICY_VERSION}</p>
<h1>{arb(lang, "trmTitle")}</h1>
<p style="margin-top:14px">{fill(LEGAL["same_as_app_terms"][lang], v=POLICY_VERSION)}</p>
<div class="box warn"><p>{arb(lang, "trmRisk")}</p></div>
{"".join(sections)}
{legal_footer(lang)}
</div>
"""
    layout(lang, "terms.html", title=f"{UI['terms'][lang]} · KINETIC", desc=ARB[lang]["trmRisk"][:155],
           body=body, head_extra=crumbs_ld)


def delete_page(lang: str) -> None:
    t = {k: v[lang] for k, v in LEGAL.items()}
    crumbs, crumbs_ld = breadcrumbs(lang, [(UI["delete"][lang], "delete-account.html")])
    body = f"""
<div class="page">
{crumbs}
<p class="eyebrow">ACCOUNT DELETION</p>
<h1>{UI["delete"][lang]}</h1>
<p style="margin-top:14px">{fill(t["del_lead"], n=OPERATOR)}</p>
<div class="box hero"><p>{t["del_where"]}</p></div>
<h2>{t["del_m1"]}</h2>
<ol><li>{t["del_s1"]}</li><li>{t["del_s2"]}</li><li>{t["del_s3"]}</li></ol>
<div class="box danger"><p>{t["del_what"]}</p></div>
<h2>{t["del_m2"]}</h2>
<p>{t["del_m2b"]}</p>
<p class="warn-text">{arb(lang, "prvS6Warn")}</p>
<h2>{t["del_m3"]}</h2>
<p>{fill(t["del_m3b"], e=EMAIL, d=REPLY_DAYS)}</p>
<h2>{t["del_stats"]}</h2>
<p>{t["del_statsb"]}</p>
</div>
"""
    layout(lang, "delete-account.html", title=f"{UI['delete'][lang]} · KINETIC",
           desc=html.unescape(fill(t["del_lead"], n=OPERATOR)), body=body, head_extra=crumbs_ld)


def not_found() -> None:
    links = " · ".join(f'<a href="{href(l, "")}">{UI["home"][l]}</a>' for l in LANGS)
    body = f"""
<div class="nf">
<b>404</b>
<h1 style="font-size:28px;margin-top:10px">{UI["nf_title"]["en"]} · {UI["nf_title"]["zh"]}</h1>
<p style="color:var(--text2);margin:14px 0 24px">{UI["nf_body"]["en"]}<br>{UI["nf_body"]["zh"]}</p>
<p>{links} · <a href="/exercises/">{UI["nav_ex"]["en"]}</a></p>
</div>
"""
    layout("en", "404.html", title="404 · KINETIC", desc=DESC["en"], body=body,
           head_extra='<meta name="robots" content="noindex">', sitemap=False)


# ---------------------------------------------------------------- robots、sitemap、llms.txt

def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        "# 允许所有爬虫，包括 AI 搜索（OAI-SearchBot、PerplexityBot、Claude-SearchBot 等）\n"
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {BASE}/sitemap.xml\n",
        encoding="utf-8",
    )


def write_sitemap() -> None:
    urls = []
    for key in SITEMAP:
        alts = "".join(
            f'<xhtml:link rel="alternate" hreflang="{HREFLANG[l]}" href="{absurl(l, key)}"/>' for l in LANGS
        ) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{absurl("en", key)}"/>'
        for lang in LANGS:
            urls.append(f"<url><loc>{absurl(lang, key)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n",
        encoding="utf-8",
    )


def write_llms() -> None:
    ex = "\n".join(
        f"- [{e['name']['en']} counter]({absurl('en', 'exercises/' + e['slug'] + '/')}): "
        f"{JOINT[e['joint']]['en'].lower()} angle, {rule_text(e, 'en')}"
        for e in EXERCISES
    )
    guides = "\n".join(f"- [{g['h1']['en']}]({absurl('en', 'guides/' + g['slug'] + '/')}): {g['card']['en']}" for g in GUIDES)
    text = f"""# KINETIC: AI Rep Counter

> {ENTITY["en"]}

Key facts:
- Platform: Android ({PLAY}). No iOS version yet.
- Price: free, no ads.
- Counts 11 exercises from joint angles measured with the phone camera (Google ML Kit pose detection, on-device).
- Video is never recorded or uploaded. Workout records are stored only on the phone, per Google account; guest mode saves nothing.
- Works offline. Languages: English, Simplified Chinese, Traditional Chinese.
- Developer: {OPERATOR} ({EMAIL}).

## Exercises
{ex}

## Guides
{guides}
- [FAQ]({absurl("en", "faq/")})

## Policies
- [Privacy policy]({absurl("en", "privacy.html")})
- [Terms of use]({absurl("en", "terms.html")})
- [Delete account and data]({absurl("en", "delete-account.html")})

Chinese versions: {absurl("zh", "")} (Simplified), {absurl("hant", "")} (Traditional).
"""
    (ROOT / "llms.txt").write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- 生成

for lang in LANGS:
    home(lang)
    exercises_hub(lang)
    for e in EXERCISES:
        exercise_page(e, lang)
    guides_hub(lang)
    for g in GUIDES:
        guide_page(g, lang)
    faq_page(lang)
    privacy(lang)
    terms(lang)
    delete_page(lang)
not_found()
write_robots()
write_sitemap()
write_llms()
print(f"built {len(SITEMAP)} pages × {len(LANGS)} languages, plus 404, robots.txt, sitemap.xml, llms.txt")
