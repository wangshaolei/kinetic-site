"""隐私政策、用户协议、删除账号页里网页独有的文案（App 里没有的）。从原 build.py 原样搬出。"""

LEGAL = {
    'same_as_app': {
        'en': 'This is the same privacy policy shown in the app (v{v}).',
        'zh': '本页与 App 内的隐私政策（v{v}）内容相同。',
        'hant': '本頁與 App 內的隱私權政策（v{v}）內容相同。',
    },
    'same_as_app_terms': {
        'en': 'These are the same terms shown in the app (v{v}).',
        'zh': '本页与 App 内的用户协议（v{v}）内容相同。',
        'hant': '本頁與 App 內的使用者條款（v{v}）內容相同。',
    },
    'delete_hint': {
        'en': 'To delete your account and data, see <a href="delete-account.html">Delete account and data</a>.',
        'zh': '删除账号与数据的方法见<a href="delete-account.html">删除账号与数据</a>页面。',
        'hant': '刪除帳號與資料的方法請見<a href="delete-account.html">刪除帳號與資料</a>頁面。',
    },
    'del_lead': {
        'en': 'This page explains how to delete your account and data in KINETIC (developer: {n}).',
        'zh': '本页说明如何删除你在 KINETIC（开发者：{n}）中的账号与数据。',
        'hant': '本頁說明如何刪除你在 KINETIC（開發者：{n}）中的帳號與資料。',
    },
    'del_where': {
        'en': "Your workouts and account details are stored only on your phone. We don't keep your account data on any server.",
        'zh': '你的训练记录和账号资料只保存在你的手机上，我们的服务器上没有你的账号数据。',
        'hant': '你的訓練紀錄和帳號資料只儲存在你的手機上，我們的伺服器上沒有你的帳號資料。',
    },
    'del_m1': {
        'en': 'Option 1: Delete in the app (recommended)',
        'zh': '方法一：在 App 内删除（推荐）',
        'hant': '方法一：在 App 內刪除（建議）',
    },
    'del_s1': {
        'en': 'Open KINETIC and sign in to the account you want to delete.',
        'zh': '打开 KINETIC，登录要删除的账号。',
        'hant': '開啟 KINETIC，登入要刪除的帳號。',
    },
    'del_s2': {
        'en': 'Go to <span class="path">Settings › Data & storage</span>.',
        'zh': '进入<span class="path">「设置 › 数据与存储」</span>。',
        'hant': '進入<span class="path">「設定 › 資料與儲存」</span>。',
    },
    'del_s3': {
        'en': 'Tap <span class="path">Delete account and data</span> and confirm.',
        'zh': '点<span class="path">「删除账号与数据」</span>，确认删除。',
        'hant': '點<span class="path">「刪除帳號與資料」</span>，確認刪除。',
    },
    'del_what': {
        'en': "What gets deleted: all workouts, daily goals and settings for that account on this phone, plus the Google photo, name, email and account ID stored on the phone. The app's Google access is revoked at the same time. Deletion is immediate and can't be undone.",
        'zh': '会删除：这台手机上该账号的全部训练记录、每日目标和设置，以及本机保存的 Google 头像、昵称、邮箱和账号 ID；同时撤销本 App 的 Google 授权。删除立即生效，无法恢复。',
        'hant': '會刪除：這台手機上該帳號的全部訓練紀錄、每日目標和設定，以及本機儲存的 Google 頭像、暱稱、電子郵件和帳號 ID；同時撤銷本 App 的 Google 授權。刪除立即生效，無法復原。',
    },
    'del_m2': {
        'en': 'Option 2: Uninstall the app',
        'zh': '方法二：卸载 App',
        'hant': '方法二：解除安裝 App',
    },
    'del_m2b': {
        'en': 'Uninstalling KINETIC deletes all of its data on the phone, for every account. You can also remove KINETIC\'s access in your Google Account under <a href="https://myaccount.google.com/connections">Third-party apps & services</a>.',
        'zh': '卸载 KINETIC 会删除手机上它的全部数据（所有账号）。也可以在 Google 账号的<a href="https://myaccount.google.com/connections">「第三方应用和服务」</a>里移除 KINETIC 的访问权限。',
        'hant': '解除安裝 KINETIC 會刪除手機上它的全部資料（所有帳號）。也可以在 Google 帳戶的<a href="https://myaccount.google.com/connections">「第三方應用程式和服務」</a>中移除 KINETIC 的存取權。',
    },
    'del_m3': {
        'en': 'Option 3: Ask us by email',
        'zh': '方法三：发邮件申请',
        'hant': '方法三：寄信申請',
    },
    'del_m3b': {
        'en': 'If you can no longer open the app, or want us to confirm, email <a href="mailto:{e}?subject=Delete%20KINETIC%20account">{e}</a> with the subject "Delete KINETIC account" and the Google email you signed in with. We\'ll reply within {d} business days.',
        'zh': '如果已经打不开 App，或者想让我们确认，请发邮件到 <a href="mailto:{e}?subject=%E5%88%A0%E9%99%A4%20KINETIC%20%E8%B4%A6%E5%8F%B7">{e}</a>，标题写「删除 KINETIC 账号」，附上登录用的 Google 邮箱。我们会在 {d} 个工作日内回复。',
        'hant': '如果已經無法開啟 App，或想請我們確認，請寄信到 <a href="mailto:{e}?subject=%E5%88%AA%E9%99%A4%20KINETIC%20%E5%B8%B3%E8%99%9F">{e}</a>，主旨寫「刪除 KINETIC 帳號」，並附上登入用的 Google 電子郵件。我們會在 {d} 個工作天內回覆。',
    },
    'del_stats': {
        'en': 'Anonymous usage stats',
        'zh': '匿名使用统计',
        'hant': '匿名使用統計',
    },
    'del_statsb': {
        'en': 'Unless you turned off "Usage stats and crash reports", the app sends anonymous usage stats and crash reports through Google Firebase. They contain no account, email or video and can\'t be linked to your account, so they can\'t be deleted per account; they are removed automatically when Firebase\'s retention period ends. You can turn them off at any time in Settings.',
        'zh': '如果你没有关闭「使用统计与崩溃报告」，App 会通过 Google Firebase 发送匿名的使用统计和崩溃报告。这些数据不包含账号、邮箱或画面，无法和你的账号对应，所以不能按账号删除；它们按 Firebase 的保存期限到期后自动删除。你可以随时在「设置 › 使用统计与崩溃报告」关闭。',
        'hant': '如果你沒有關閉「使用統計與當機報告」，App 會透過 Google Firebase 傳送匿名的使用統計和當機報告。這些資料不包含帳號、電子郵件或畫面，無法和你的帳號對應，所以無法依帳號刪除；它們依 Firebase 的保存期限到期後自動刪除。你可以隨時在「設定 › 使用統計與當機報告」關閉。',
    },
}
