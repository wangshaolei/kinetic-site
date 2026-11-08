# KINETIC 主站

KINETIC（AI 运动计数 App）的公开网站 https://kinetic.lencoder.com/ ，部署在 GitHub Pages（main 分支根目录，推送即发布）。

## 页面

英文在根目录，简体中文在 `/zh/`，繁体中文在 `/zh-hant/`，三种语言的页面一一对应（hreflang 互相标注）。

| 页面 | 网址（英文） | 说明 |
|---|---|---|
| 首页 | `/` | 设计稿见 rep-counter 仓库 `docs/site-redesign/index.html`；兼做技术支持页 |
| 动作 | `/exercises/`、`/exercises/<动作>-counter/` | 11 个动作的判定角度、手机摆放、常见问题 |
| 指南 | `/guides/`、`/guides/<slug>/` | 手机摆放、本机识别原理、俯卧撑和深蹲挑战、同类 App 对比 |
| 常见问题 | `/faq/` | |
| 隐私政策 | `/privacy.html` | Google Play、Google 登录品牌信息引用，**不能改名** |
| 用户协议 | `/terms.html` | |
| 删除账号与数据 | `/delete-account.html` | Google Play 账号删除政策要求，**不能改名** |
| 其他 | `404.html`、`robots.txt`、`sitemap.xml`、`llms.txt` | 都由脚本生成 |

旧网址的 `?lang=zh` / `?lang=hant` 会自动跳到对应的中文网址。

## 更新

除 `assets/` 里的图片和 `CNAME`、`googlef04c3ff81c2cd3a7.html`（Search Console 验证文件，别删）外，所有页面都由脚本生成，不要手改 HTML：

```bash
python3 tools/build.py ../rep-counter/app/lib/l10n
```

| 要改什么 | 改哪里 |
|---|---|
| 隐私政策、用户协议正文 | App 的 `app/lib/l10n/app_*.arb`，改完重新生成 |
| 首页、动作页、常见问题文案 | `tools/content.py` |
| 指南正文 | `tools/guides.py` |
| 对比页的表格（同类 App 的商店信息、查阅日期） | `tools/compare.py`，只写对方商店页上写明的事实 |
| 删除账号页文案 | `tools/legal_text.py` |
| 运营方、邮箱、生效日期 | `tools/build.py` 顶部，要和 App 的 `AppLegal` 一致 |
| 「最后更新」日期、sitemap 日期 | `tools/build.py` 的 `UPDATED` |
| 下载按钮（已开启，用 `assets/badges/` 里的 Google 官方徽章）；改回「即将上架」 | `tools/build.py` 的 `PLAY_LIVE` |
| 首页宣传视频 | 视频文件 `assets/kinetic-demo.mp4`、封面 `assets/video-poster.jpg`；YouTube 外链 ID 和上传日期在 `tools/build.py` 的 `YT_ID`、`YT_UPLOADED` |
| 样式 / 首页动效 | `assets/site.css` / `assets/home.js` |

App 里改了动作的默认角度（`app/lib/domain/models/exercise.dart`），`tools/content.py` 的 `EXERCISES` 要同步改。

## 图片

| 文件 | 用途 | 来源 |
|---|---|---|
| `assets/shot-1~4.jpg` | 英文首页截图、结构化数据 | rep-counter `docs/store/listing/screenshots/en-US/`，缩到 540×960 |
| `assets/zh/shot-1~4.jpg`、`assets/zh-hant/shot-1~4.jpg` | 中文首页截图 | 同上 `zh-CN/`、`zh-TW/` |
| `assets/og-1200x630.png`、`assets/zh/og-1200x630.png`、`assets/zh-hant/og-1200x630.png` | 分享卡片图（某种语言没有时退回简中、英文） | 英文是设计稿；简中由商店置顶大图加边得到；繁中是 rep-counter `docs/store/listing/feature-graphic/og-zh-hant-1200x630.png` |
| `assets/kinetic-demo.mp4`、`assets/video-poster.jpg` | 首页宣传视频和封面（不嵌 YouTube：大陆打不开，代理 IP 会被要求登录验证） | rep-counter `docs/store/listing/video/kinetic-promo-30s.mp4` 压成 720p（crf 26）；封面是第 7.5 秒截图 |
| `assets/badges/google-play-{en,zh,hant}.png` | Google Play 官方下载徽章（删掉则显示文字按钮） | https://play.google.com/intl/en_us/badges/ |

## 本地预览

```bash
python3 -m http.server 8765
```

打开 http://localhost:8765/ 。
