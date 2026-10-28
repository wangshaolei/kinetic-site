# KINETIC 主站

KINETIC（AI 运动计数 App）的公开网页，部署在 GitHub Pages：

| 页面 | 用途 |
|---|---|
| `index.html` | 首页，兼做技术支持页（App Store「技术支持网址」） |
| `privacy.html` | 隐私政策（Google Play、App Store、Google 登录品牌信息） |
| `terms.html` | 用户协议 |
| `delete-account.html` | 删除账号与数据（Google Play 账号删除政策要求的网页） |

每页都有英文、简体、繁体三种语言，按浏览器语言自动选择，也可以用 `?lang=en|zh|hant` 指定。

## 更新

隐私政策和用户协议的正文取自 App 的多语言文件，App 里改了文案后重新生成：

```bash
python3 tools/build.py ../rep-counter/app/lib/l10n
```

运营方、联系邮箱、生效日期在 `tools/build.py` 顶部，要和 App 里的 `AppLegal` 保持一致。
