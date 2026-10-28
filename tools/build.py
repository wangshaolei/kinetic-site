"""生成 KINETIC 主站的静态页面。

隐私政策、用户协议的正文直接取自 App 的多语言文件（app/lib/l10n/app_*.arb），
保证网页和 App 内的版本一致。改了 App 里的文案后重新运行：

    python3 tools/build.py [App 的 l10n 目录]

默认 l10n 目录是 ../rep-counter/app/lib/l10n（两个仓库放在同一个上级目录时）。
"""

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
L10N = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "rep-counter/app/lib/l10n"

# 和 App 里 AppLegal 保持一致（app/lib/domain/models/app_links.dart）
OPERATOR = "shaolei wang"
EMAIL = "leishaolen@gmail.com"
EFFECTIVE_DATE = "2026-10-28"
POLICY_VERSION = "1.1"
REPLY_DAYS = 7
YEAR = 2026

LANGS = {"en": "app_en.arb", "zh": "app_zh.arb", "hant": "app_zh_Hant.arb"}
ARB = {k: json.loads((L10N / f).read_text(encoding="utf-8")) for k, f in LANGS.items()}

# 网页独有的文案（App 里没有的）
T = {
    "home": {"en": "Home", "zh": "首页", "hant": "首頁"},
    "privacy": {"en": "Privacy policy", "zh": "隐私政策", "hant": "隱私權政策"},
    "terms": {"en": "Terms of use", "zh": "用户协议", "hant": "使用者條款"},
    "delete": {"en": "Delete account and data", "zh": "删除账号与数据", "hant": "刪除帳號與資料"},
    "coming": {
        "en": "Coming soon to Google Play",
        "zh": "即将上架 Google Play",
        "hant": "即將上架 Google Play",
    },
    "same_as_app": {
        "en": "This is the same privacy policy shown in the app (v{v}).",
        "zh": "本页与 App 内的隐私政策（v{v}）内容相同。",
        "hant": "本頁與 App 內的隱私權政策（v{v}）內容相同。",
    },
    "same_as_app_terms": {
        "en": "These are the same terms shown in the app (v{v}).",
        "zh": "本页与 App 内的用户协议（v{v}）内容相同。",
        "hant": "本頁與 App 內的使用者條款（v{v}）內容相同。",
    },
    "delete_hint": {
        "en": "To delete your account and data, see <a href=\"delete-account.html\">Delete account and data</a>.",
        "zh": "删除账号与数据的方法见<a href=\"delete-account.html\">删除账号与数据</a>页面。",
        "hant": "刪除帳號與資料的方法請見<a href=\"delete-account.html\">刪除帳號與資料</a>頁面。",
    },
    "f1t": {"en": "11 exercises, counted for you", "zh": "11 种动作自动计数", "hant": "11 種動作自動計數"},
    "f1b": {
        "en": "Squats, push-ups, lunges, sit-ups and more. Each good rep counts +1, and it tells you when you're not there yet.",
        "zh": "深蹲、俯卧撑、弓步蹲、仰卧起坐等，动作标准一次 +1，不到位会提醒你。",
        "hant": "深蹲、伏地挺身、弓步蹲、仰臥起坐等，動作標準一次 +1，不到位會提醒你。",
    },
    "f3t": {"en": "Check-ins, badges, hero cards", "zh": "打卡、成就和达人卡片", "hant": "打卡、成就和達人卡片"},
    "f3b": {
        "en": "Sign in to keep workouts on your phone, fill your calendar and earn badges. Share a hero card after each workout.",
        "zh": "登录后训练记录按账号保存在手机上，计入打卡日历和成就；练完生成达人卡片分享。",
        "hant": "登入後訓練紀錄依帳號儲存在手機上，計入打卡日曆和成就；練完產生達人卡片分享。",
    },
    "f4t": {"en": "No sign-in needed", "zh": "不登录也能用", "hant": "不登入也能用"},
    "f4b": {
        "en": "Guest mode tracks and counts too. It just doesn't save your workouts.",
        "zh": "游客模式下识别和计数都能用，只是不保存训练记录。",
        "hant": "訪客模式下辨識和計數都能用，只是不會儲存訓練紀錄。",
    },
    "support": {"en": "Help and contact", "zh": "帮助与联系", "hant": "說明與聯絡"},
    "support_body": {
        "en": "Questions, problems or ideas? Email <a href=\"mailto:{e}\">{e}</a> and we'll reply within {d} business days.",
        "zh": "使用中遇到问题、想反馈建议，请发邮件到 <a href=\"mailto:{e}\">{e}</a>，我们会在 {d} 个工作日内回复。",
        "hant": "使用時遇到問題、想回饋建議，請寄信到 <a href=\"mailto:{e}\">{e}</a>，我們會在 {d} 個工作天內回覆。",
    },
    "faq1q": {"en": "The count seems off. What can I do?", "zh": "计数不准怎么办？", "hant": "計數不準怎麼辦？"},
    "faq1a": {
        "en": "Make sure your whole body is in frame and the room is well lit. Face the camera for squats; for push-ups, put the phone on the floor beside you.",
        "zh": "让头到脚全身入镜、光线充足。深蹲时正对镜头；俯卧撑时把手机放在地上、身体侧面对着镜头。",
        "hant": "讓頭到腳全身入鏡、光線充足。深蹲時正對鏡頭；伏地挺身時把手機放在地上、身體側面對著鏡頭。",
    },
    "faq2q": {
        "en": "Will my workouts move to a new phone?",
        "zh": "换手机后记录还在吗？",
        "hant": "換手機後紀錄還在嗎？",
    },
    "faq2a": {
        "en": "Workouts are stored only on your phone and there's no cloud backup. You can export them in Settings › Data & storage and keep the file yourself.",
        "zh": "记录只存在这台手机上，没有云端备份。可以在「设置 › 数据与存储」导出数据，自己保存文件。",
        "hant": "紀錄只存在這台手機上，沒有雲端備份。可以在「設定 › 資料與儲存」匯出資料，自己保存檔案。",
    },
    "op": {"en": "Operated by {n}", "zh": "运营方 {n}", "hant": "營運方 {n}"},
    "contact": {"en": "Contact: {e}", "zh": "联系邮箱：{e}", "hant": "聯絡信箱：{e}"},
    # 删除账号页（Google Play 账号删除政策要求的公开网页）
    "del_lead": {
        "en": "This page explains how to delete your account and data in KINETIC (developer: {n}).",
        "zh": "本页说明如何删除你在 KINETIC（开发者：{n}）中的账号与数据。",
        "hant": "本頁說明如何刪除你在 KINETIC（開發者：{n}）中的帳號與資料。",
    },
    "del_where": {
        "en": "Your workouts and account details are stored only on your phone. We don't keep your account data on any server.",
        "zh": "你的训练记录和账号资料只保存在你的手机上，我们的服务器上没有你的账号数据。",
        "hant": "你的訓練紀錄和帳號資料只儲存在你的手機上，我們的伺服器上沒有你的帳號資料。",
    },
    "del_m1": {"en": "Option 1: Delete in the app (recommended)", "zh": "方法一：在 App 内删除（推荐）", "hant": "方法一：在 App 內刪除（建議）"},
    "del_s1": {
        "en": "Open KINETIC and sign in to the account you want to delete.",
        "zh": "打开 KINETIC，登录要删除的账号。",
        "hant": "開啟 KINETIC，登入要刪除的帳號。",
    },
    "del_s2": {
        "en": "Go to <span class=\"path\">Settings › Data & storage</span>.",
        "zh": "进入<span class=\"path\">「设置 › 数据与存储」</span>。",
        "hant": "進入<span class=\"path\">「設定 › 資料與儲存」</span>。",
    },
    "del_s3": {
        "en": "Tap <span class=\"path\">Delete account and data</span> and confirm.",
        "zh": "点<span class=\"path\">「删除账号与数据」</span>，确认删除。",
        "hant": "點<span class=\"path\">「刪除帳號與資料」</span>，確認刪除。",
    },
    "del_what": {
        "en": "What gets deleted: all workouts, daily goals and settings for that account on this phone, plus the Google photo, name, email and account ID stored on the phone. The app's Google access is revoked at the same time. Deletion is immediate and can't be undone.",
        "zh": "会删除：这台手机上该账号的全部训练记录、每日目标和设置，以及本机保存的 Google 头像、昵称、邮箱和账号 ID；同时撤销本 App 的 Google 授权。删除立即生效，无法恢复。",
        "hant": "會刪除：這台手機上該帳號的全部訓練紀錄、每日目標和設定，以及本機儲存的 Google 頭像、暱稱、電子郵件和帳號 ID；同時撤銷本 App 的 Google 授權。刪除立即生效，無法復原。",
    },
    "del_m2": {"en": "Option 2: Uninstall the app", "zh": "方法二：卸载 App", "hant": "方法二：解除安裝 App"},
    "del_m2b": {
        "en": "Uninstalling KINETIC deletes all of its data on the phone, for every account. You can also remove KINETIC's access in your Google Account under <a href=\"https://myaccount.google.com/connections\">Third-party apps & services</a>.",
        "zh": "卸载 KINETIC 会删除手机上它的全部数据（所有账号）。也可以在 Google 账号的<a href=\"https://myaccount.google.com/connections\">「第三方应用和服务」</a>里移除 KINETIC 的访问权限。",
        "hant": "解除安裝 KINETIC 會刪除手機上它的全部資料（所有帳號）。也可以在 Google 帳戶的<a href=\"https://myaccount.google.com/connections\">「第三方應用程式和服務」</a>中移除 KINETIC 的存取權。",
    },
    "del_m3": {"en": "Option 3: Ask us by email", "zh": "方法三：发邮件申请", "hant": "方法三：寄信申請"},
    "del_m3b": {
        "en": "If you can no longer open the app, or want us to confirm, email <a href=\"mailto:{e}?subject=Delete%20KINETIC%20account\">{e}</a> with the subject \"Delete KINETIC account\" and the Google email you signed in with. We'll reply within {d} business days.",
        "zh": "如果已经打不开 App，或者想让我们确认，请发邮件到 <a href=\"mailto:{e}?subject=%E5%88%A0%E9%99%A4%20KINETIC%20%E8%B4%A6%E5%8F%B7\">{e}</a>，标题写「删除 KINETIC 账号」，附上登录用的 Google 邮箱。我们会在 {d} 个工作日内回复。",
        "hant": "如果已經無法開啟 App，或想請我們確認，請寄信到 <a href=\"mailto:{e}?subject=%E5%88%AA%E9%99%A4%20KINETIC%20%E5%B8%B3%E8%99%9F\">{e}</a>，主旨寫「刪除 KINETIC 帳號」，並附上登入用的 Google 電子郵件。我們會在 {d} 個工作天內回覆。",
    },
    "del_stats": {"en": "Anonymous usage stats", "zh": "匿名使用统计", "hant": "匿名使用統計"},
    "del_statsb": {
        "en": "Unless you turned off \"Usage stats and crash reports\", the app sends anonymous usage stats and crash reports through Google Firebase. They contain no account, email or video and can't be linked to your account, so they can't be deleted per account; they are removed automatically when Firebase's retention period ends. You can turn them off at any time in Settings.",
        "zh": "如果你没有关闭「使用统计与崩溃报告」，App 会通过 Google Firebase 发送匿名的使用统计和崩溃报告。这些数据不包含账号、邮箱或画面，无法和你的账号对应，所以不能按账号删除；它们按 Firebase 的保存期限到期后自动删除。你可以随时在「设置 › 使用统计与崩溃报告」关闭。",
        "hant": "如果你沒有關閉「使用統計與當機報告」，App 會透過 Google Firebase 傳送匿名的使用統計和當機報告。這些資料不包含帳號、電子郵件或畫面，無法和你的帳號對應，所以無法依帳號刪除；它們依 Firebase 的保存期限到期後自動刪除。你可以隨時在「設定 › 使用統計與當機報告」關閉。",
    },
    "desc": {
        "en": "KINETIC uses your phone's camera to count reps for push-ups, squats and more. Video stays on your phone.",
        "zh": "KINETIC 用手机摄像头为俯卧撑、深蹲等动作自动计数，画面不离开手机。",
        "hant": "KINETIC 用手機相機為伏地挺身、深蹲等動作自動計數，畫面不離開手機。",
    },
}

NAV = [("index.html", "home"), ("privacy.html", "privacy"), ("terms.html", "terms"), ("delete-account.html", "delete")]


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def arb(lang: str, key: str, **args) -> str:
    """取 App 文案并转义；占位符在转义后替换（值里不含 HTML）。"""
    s = esc(ARB[lang][key])
    for k, v in args.items():
        s = s.replace("{" + k + "}", esc(str(v)))
    return s


def t(key: str, lang: str, **args) -> str:
    """网页独有文案，本身可以带简单 HTML。"""
    s = T[key][lang]
    for k, v in args.items():
        s = s.replace("{" + k + "}", esc(str(v)))
    return s


def each(fn) -> str:
    """把三种语言的同一块内容各渲染一份，用 data-l 切换显示。"""
    return "\n".join(f'<div data-l="{lang}">{fn(lang)}</div>' for lang in LANGS)


def page(file: str, titles: dict, body: str) -> None:
    title_metas = "\n".join(
        f'<meta name="title-{lang}" content="{esc(titles[lang])}">' for lang in LANGS
    )
    nav = " ".join(
        f'<a href="{href}">{each_inline(key)}</a>' for href, key in NAV if href != file
    )
    doc = f"""<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titles["en"])}</title>
{title_metas}
<meta name="description" content="{esc(T["desc"]["en"])}">
<link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="assets/site.css">
<script src="assets/lang.js"></script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="index.html"><img src="assets/icon-512.png" alt="">KINETIC</a>
<div class="langs"><button data-set="en">EN</button><button data-set="zh">简</button><button data-set="hant">繁</button></div>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="bottom"><div class="wrap">
<div class="links">{nav}</div>
{each(lambda l: f"<p>© {YEAR} KINETIC · {t('op', l, n=OPERATOR)} · {t('contact', l, e=EMAIL)}</p>")}
</div></footer>
</body>
</html>
"""
    (ROOT / file).write_text(doc, encoding="utf-8")


def each_inline(key: str) -> str:
    return "".join(f'<span data-l="{lang}">{T[key][lang]}</span>' for lang in LANGS)


def legal_footer(lang: str) -> str:
    return (
        f'<p class="section">{arb(lang, "legalEffective", date=EFFECTIVE_DATE)} · '
        f'{arb(lang, "legalOperator", name=OPERATOR)}</p>'
    )


def privacy(lang: str) -> str:
    sections = []
    for i in range(1, 9):
        body = (
            arb(lang, "prvS8Body", email=EMAIL, days=REPLY_DAYS)
            if i == 8
            else arb(lang, f"prvS{i}Body")
        )
        warn = f'<p class="note-warn">{arb(lang, "prvS6Warn")}</p>' if i == 6 else ""
        extra = f"<p>{t('delete_hint', lang)}</p>" if i == 7 else ""
        sections.append(
            f'<div class="section"><h3>{arb(lang, f"prvS{i}Title")}</h3><p>{body}</p>{warn}{extra}</div>'
        )
    return f"""
<p class="eyebrow">PRIVACY · v{POLICY_VERSION}</p>
<h1>{arb(lang, "prvTitle")}</h1>
<p>{t("same_as_app", lang, v=POLICY_VERSION)}</p>
<div class="card hero"><h3>{arb(lang, "prvHeroTitle")}</h3><p>{arb(lang, "prvHeroBody")}</p></div>
<div class="cols">
<div class="card keep"><h3>{arb(lang, "prvKeepTitle")}</h3><p class="list-lines">{arb(lang, "prvKeepBody")}</p></div>
<div class="card never"><h3>{arb(lang, "prvNeverTitle")}</h3><p class="list-lines">{arb(lang, "prvNeverBody")}</p></div>
</div>
{"".join(sections)}
{legal_footer(lang)}
"""


def terms(lang: str) -> str:
    sections = []
    for i in range(1, 9):
        if i == 6:
            body = arb(lang, "trmS6Body", company=OPERATOR)
        elif i == 8:
            body = arb(lang, "trmS8Body", email=EMAIL)
        else:
            body = arb(lang, f"trmS{i}Body")
        sections.append(
            f'<div class="section"><h3>{arb(lang, f"trmS{i}Title")}</h3><p>{body}</p></div>'
        )
    return f"""
<p class="eyebrow">TERMS · v{POLICY_VERSION}</p>
<h1>{arb(lang, "trmTitle")}</h1>
<p>{t("same_as_app_terms", lang, v=POLICY_VERSION)}</p>
<div class="card warn"><p>{arb(lang, "trmRisk")}</p></div>
{"".join(sections)}
{legal_footer(lang)}
"""


def delete_page(lang: str) -> str:
    return f"""
<p class="eyebrow">ACCOUNT DELETION</p>
<h1>{T["delete"][lang]}</h1>
<p>{t("del_lead", lang, n=OPERATOR)}</p>
<div class="card hero"><p>{t("del_where", lang)}</p></div>
<h2>{t("del_m1", lang)}</h2>
<ol class="steps"><li>{t("del_s1", lang)}</li><li>{t("del_s2", lang)}</li><li>{t("del_s3", lang)}</li></ol>
<div class="card danger"><p>{t("del_what", lang)}</p></div>
<h2>{t("del_m2", lang)}</h2>
<p>{t("del_m2b", lang)}</p>
<p class="note-warn">{arb(lang, "prvS6Warn")}</p>
<h2>{t("del_m3", lang)}</h2>
<p>{t("del_m3b", lang, e=EMAIL, d=REPLY_DAYS)}</p>
<h2>{t("del_stats", lang)}</h2>
<p>{t("del_statsb", lang)}</p>
"""


def home(lang: str) -> str:
    def card(title: str, body: str) -> str:
        return f'<div class="card"><h3>{title}</h3><p>{body}</p></div>'

    return f"""
<div class="hero-block">
<img src="assets/icon-512.png" alt="KINETIC">
<div>
<p class="eyebrow">AI REP COUNTER</p>
<h1>{arb(lang, "onb1Title")}</h1>
<span class="badge">{T["coming"][lang]}</span>
</div>
</div>
<p>{arb(lang, "onb1Body")}</p>
<div class="grid">
{card(t("f1t", lang), t("f1b", lang))}
{card(arb(lang, "prvHeroTitle"), arb(lang, "prvHeroBody"))}
{card(t("f3t", lang), t("f3b", lang))}
{card(t("f4t", lang), t("f4b", lang))}
</div>
<h2 id="support">{t("support", lang)}</h2>
<p>{t("support_body", lang, e=EMAIL, d=REPLY_DAYS)}</p>
<div class="section"><h3>{t("faq1q", lang)}</h3><p>{t("faq1a", lang)}</p></div>
<div class="section"><h3>{t("faq2q", lang)}</h3><p>{t("faq2a", lang)}</p></div>
"""


def titles(key: str) -> dict:
    return {lang: f"{T[key][lang]} · KINETIC" for lang in LANGS}


page("index.html", {lang: "KINETIC" for lang in LANGS}, each(home))
page("privacy.html", titles("privacy"), each(privacy))
page("terms.html", titles("terms"), each(terms))
page("delete-account.html", titles("delete"), each(delete_page))
print("built:", ", ".join(f for f, _ in NAV))
