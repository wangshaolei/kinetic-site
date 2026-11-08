"""网页独有的文案（三种语言）。隐私政策、用户协议的正文不在这里，直接取自 App 的 arb。

动作的角度、关节、摆放方式取自 App：rep-counter/app/lib/domain/models/exercise.dart
（默认角度和注释）和 ui/core/l10n/l10n.dart（每种姿态的引导文字）。App 里改了默认角度，
这里的 EXERCISES 也要改，否则网页写的判定标准和 App 对不上。

英文用直引号 '（和 App 一致）。字符串里可以带简单 HTML。
"""

UI = {
    "nav_how": {"en": "How it counts", "zh": "怎么计数", "hant": "怎麼計數"},
    "nav_ex": {"en": "Exercises", "zh": "动作", "hant": "動作"},
    "nav_privacy": {"en": "Privacy", "zh": "隐私", "hant": "隱私"},
    "nav_guides": {"en": "Guides", "zh": "指南", "hant": "指南"},
    "nav_faq": {"en": "FAQ", "zh": "常见问题", "hant": "常見問題"},
    "home": {"en": "Home", "zh": "首页", "hant": "首頁"},
    "skip": {"en": "Skip to content", "zh": "跳到正文", "hant": "跳到內容"},
    "lang_label": {"en": "Language", "zh": "语言", "hant": "語言"},
    "soon": {"en": "Coming soon to Google Play", "zh": "即将上架 Google Play", "hant": "即將上架 Google Play"},
    "get": {"en": "Get it on Google Play", "zh": "在 Google Play 下载", "hant": "在 Google Play 下載"},
    "cta_line": {
        "en": "Free on Android. Video never leaves your phone.",
        "zh": "Android 免费下载，画面从不离开手机。",
        "hant": "Android 免費下載，畫面從不離開手機。",
    },
    "operated": {"en": "operated by", "zh": "运营方", "hant": "營運方"},
    "privacy": {"en": "Privacy policy", "zh": "隐私政策", "hant": "隱私權政策"},
    "terms": {"en": "Terms of use", "zh": "用户协议", "hant": "使用者條款"},
    "delete": {"en": "Delete account and data", "zh": "删除账号与数据", "hant": "刪除帳號與資料"},
    "updated": {"en": "Last updated", "zh": "最后更新", "hant": "最後更新"},
    "author": {"en": "Author", "zh": "作者", "hant": "作者"},
    "not_medical": {
        "en": "KINETIC is a fitness tool, not a medical device. Talk to a doctor before starting a new exercise program, and stop if anything hurts.",
        "zh": "KINETIC 是健身辅助工具，不是医疗器械。开始新的训练计划前请先咨询医生，练习中感到疼痛请立即停止。",
        "hant": "KINETIC 是健身輔助工具，不是醫療器材。開始新的訓練計畫前請先諮詢醫生，練習中感到疼痛請立即停止。",
    },
    "langbar_zh": {
        "en": "本页为英文版。<a href=\"{u}\">查看简体中文版</a>",
        "zh": "",
        "hant": "",
    },
    "langbar_hant": {
        "en": "本頁為英文版。<a href=\"{u}\">查看繁體中文版</a>",
        "zh": "",
        "hant": "",
    },
    "all_faq": {"en": "All questions →", "zh": "查看全部问题 →", "hant": "查看全部問題 →"},
    "all_placement": {
        "en": "Phone setup for every exercise →",
        "zh": "全部动作的摆放方法 →",
        "hant": "全部動作的擺放方法 →",
    },
    "how_go": {"en": "How it counts →", "zh": "看怎么数 →", "hant": "看怎麼數 →"},
    "single": {"en": "single angle", "zh": "单角度", "hant": "單角度"},
    "nf_title": {"en": "Page not found", "zh": "找不到这个页面", "hant": "找不到這個頁面"},
    "nf_body": {
        "en": "The page may have moved. Try the home page or the exercise list.",
        "zh": "页面可能已经移动。可以回到首页或动作列表。",
        "hant": "頁面可能已經移動。可以回到首頁或動作列表。",
    },
}

DESC = {
    "en": "Free Android app that counts your reps with the phone camera. 11 exercises, pose detection on-device, video never uploaded.",
    "zh": "免费的 Android App，用手机摄像头自动数俯卧撑、深蹲等 11 种动作。姿态识别在手机上完成，画面不上传。",
    "hant": "免費的 Android App，用手機相機自動計算伏地挺身、深蹲等 11 種動作。姿勢辨識在手機上完成，畫面不會上傳。",
}

# 所有地方统一用的一句话介绍（AEO：多处一致，AI 才认得出是同一个东西）
ENTITY = {
    "en": "KINETIC: AI Rep Counter is a free Android app that uses your phone camera to count reps for 11 exercises. Pose detection runs on-device; video is never uploaded.",
    "zh": "KINETIC：AI 运动计数是一款免费的 Android App，用手机摄像头自动计算 11 种动作的次数。姿态识别在手机上完成，画面不会上传。",
    "hant": "KINETIC：AI 運動計數是一款免費的 Android App，用手機相機自動計算 11 種動作的次數。姿勢辨識在手機上完成，畫面不會上傳。",
}

APP_NAME = {"en": "KINETIC: AI Rep Counter", "zh": "KINETIC：AI 运动计数", "hant": "KINETIC：AI 運動計數"}

# ---------------------------------------------------------------- 首页

HOME = {
    "title": {
        "en": "KINETIC – AI Rep Counter for Push-ups, Squats & More",
        "zh": "KINETIC：AI 运动计数，摄像头自动数俯卧撑、深蹲",
        "hant": "KINETIC：AI 運動計數，相機自動計算伏地挺身、深蹲",
    },
    "og_title": {"en": "KINETIC – AI Rep Counter", "zh": "KINETIC：AI 运动计数", "hant": "KINETIC：AI 運動計數"},
    "og_desc": {
        "en": "Your camera counts every rep. Video stays on your phone.",
        "zh": "摄像头帮你数每一次，画面不离开手机。",
        "hant": "相機幫你數每一次，畫面不離開手機。",
    },
    "eyebrow": {"en": "AI Rep Counter · Android", "zh": "AI 运动计数 · Android", "hant": "AI 運動計數 · Android"},
    # 标题逐词出现的动画：第一行、第二行分别切成几块
    "h1": {
        "en": (["Just", "move."], ["AI", "counts", "for", "you."]),
        "zh": (["做就行，"], ["AI", "帮你数"]),
        "hant": (["做就對了，"], ["AI", "幫你數"]),
    },
    "see_how": {"en": "See how it counts ↓", "zh": "看看怎么数 ↓", "hant": "看看怎麼數 ↓"},
    "facts": {
        "en": ["<b>Free</b> · no ads", "<b>11</b> exercises", "<b>0</b> video uploaded", "No sign-in needed"],
        "zh": ["<b>免费</b> · 无广告", "<b>11</b> 种动作", "<b>0</b> 画面上传", "不登录也能用"],
        "hant": ["<b>免費</b> · 無廣告", "<b>11</b> 種動作", "<b>0</b> 畫面上傳", "不登入也能用"],
    },
    "phone_aria": {
        "en": "KINETIC counting squats: a green skeleton overlay tracks the knee angle and the counter goes up with each full squat",
        "zh": "KINETIC 正在数深蹲：绿色骨架跟踪膝角，每完成一次完整深蹲计数 +1",
        "hant": "KINETIC 正在計算深蹲：綠色骨架追蹤膝角，每完成一次完整深蹲計數 +1",
    },
    "tracking": {"en": "Tracking…", "zh": "识别中…", "hant": "辨識中…"},
    "js": {
        "en": {"knee": "KNEE", "deep": "Deep enough ✓", "good": "Good rep · +1", "lower": "Go lower…",
               "guest": "GUEST", "signedIn": "SIGNED IN", "locale": "en-US"},
        "zh": {"knee": "膝角", "deep": "蹲够深了 ✓", "good": "动作标准 · +1", "lower": "再低一点…",
               "guest": "游客", "signedIn": "已登录", "locale": "zh-CN"},
        "hant": {"knee": "膝角", "deep": "蹲夠深了 ✓", "good": "動作標準 · +1", "lower": "再低一點…",
                 "guest": "訪客", "signedIn": "已登入", "locale": "zh-TW"},
    },
    "how_eyebrow": {"en": "01 · How it counts", "zh": "01 · 怎么计数", "hant": "01 · 怎麼計數"},
    "how_h2": {
        "en": "It watches your joint angles, not a stopwatch.",
        "zh": "看的是关节角度，不是秒表。",
        "hant": "看的是關節角度，不是碼錶。",
    },
    "how_lead": {
        "en": "KINETIC counts a squat when your knee angle drops to 110° or less and comes back above 160°. Half reps don't count, and the app tells you to go lower.",
        "zh": "膝角降到 110° 或更小、再站回 160° 以上，记 1 次深蹲。蹲一半不算，App 会提醒你再低一点。",
        "hant": "膝角降到 110° 或更小、再站回 160° 以上，記 1 次深蹲。蹲一半不算，App 會提醒你再低一點。",
    },
    "how_steps": {
        "en": [("Stand tall", "Knee above 160°, ready position."),
               ("Go down to 110° or less", "The frame turns green when the rep is deep enough."),
               ("Stand back up = +1", "Above 160° again, the rep is counted.")],
        "zh": [("站直", "膝角大于 160°，准备姿势。"),
               ("蹲到 110° 以下", "蹲得够深时，取景框变绿。"),
               ("站起来 = +1", "回到 160° 以上，这一次就算数了。")],
        "hant": [("站直", "膝角大於 160°，準備姿勢。"),
                 ("蹲到 110° 以下", "蹲得夠深時，取景框變綠。"),
                 ("站起來 = +1", "回到 160° 以上，這一次就算數了。")],
    },
    "knee_angle": {"en": "KNEE ANGLE", "zh": "膝角", "hant": "膝角"},
    "reps": {"en": "REPS", "zh": "次数", "hant": "次數"},
    "ex_eyebrow": {"en": "02 · Exercises", "zh": "02 · 动作", "hant": "02 · 動作"},
    "ex_h2": {"en": "11 exercises, counted for you.", "zh": "11 种动作，自动计数。", "hant": "11 種動作，自動計數。"},
    "ex_lead": {
        "en": "Each one has its own joint and default angles. Too strict or too loose? Adjust the thresholds right on the skeleton in the app.",
        "zh": "每种动作有自己的判定关节和默认角度。觉得太严或太松，可以在 App 里直接在骨架上调整阈值。",
        "hant": "每種動作有自己的判定關節和預設角度。覺得太嚴或太鬆，可以在 App 裡直接在骨架上調整門檻。",
    },
    "priv_eyebrow": {"en": "03 · Privacy", "zh": "03 · 隐私", "hant": "03 · 隱私"},
    "priv_h2": {
        "en": "Video stays on your phone.<br>Records stay on this device.",
        "zh": "画面不离开手机，<br>记录只存在这台设备上。",
        "hant": "畫面不離開手機，<br>紀錄只存在這台裝置上。",
    },
    "priv_lead": {
        "en": "Pose detection runs on your phone with Google ML Kit. Each frame is turned into joint positions and thrown away. Nothing is recorded, nothing is uploaded.",
        "zh": "姿态识别用 Google ML Kit 在手机上完成。每一帧画面转换成关节位置后立即丢弃，不录像，也不上传。",
        "hant": "姿勢辨識用 Google ML Kit 在手機上完成。每一幀畫面轉換成關節位置後立即丟棄，不錄影，也不上傳。",
    },
    "priv_aria": {
        "en": "Diagram: camera frames are processed on the phone and stopped before they reach any server",
        "zh": "示意图：摄像头画面在手机上处理，到不了任何服务器",
        "hant": "示意圖：相機畫面在手機上處理，到不了任何伺服器",
    },
    "priv_dev": {"en": "Your phone · on-device AI", "zh": "你的手机 · 本机 AI", "hant": "你的手機 · 本機 AI"},
    "priv_cloud": {"en": "Any server", "zh": "任何服务器", "hant": "任何伺服器"},
    "priv_keep": {
        "en": [("Never recorded", "Frames are analysed live and discarded. There is no video file."),
               ("Stored on this phone", "Workouts live in the app's private storage. Uninstalling deletes them."),
               ("Anonymous stats only", "Usage stats and crash reports carry no video, and you can turn them off in Settings.")],
        "zh": [("不录像", "画面实时分析后立即丢弃，不会生成视频文件。"),
               ("存在这台手机上", "训练记录保存在 App 的私有存储里，卸载即删除。"),
               ("只有匿名统计", "使用统计和崩溃报告不含画面，可以在设置里关闭。")],
        "hant": [("不錄影", "畫面即時分析後立即丟棄，不會產生影片檔。"),
                 ("存在這支手機上", "訓練紀錄儲存在 App 的私有空間，解除安裝即刪除。"),
                 ("只有匿名統計", "使用統計和當機報告不含畫面，可以在設定中關閉。")],
    },
    "priv_more": {
        "en": "How on-device pose detection works →",
        "zh": "本机姿态识别是怎么工作的 →",
        "hant": "本機姿勢辨識是怎麼運作的 →",
    },
    "cal_aria": {"en": "Example check-in calendar for October", "zh": "十月打卡日历示例", "hant": "十月打卡日曆範例"},
    "cal_title": {"en": "Check-ins", "zh": "打卡", "hant": "打卡"},
    "cal_streak": {"en": "Streak", "zh": "连续", "hant": "連續"},
    "cal_month": {"en": "This month", "zh": "本月", "hant": "本月"},
    "cal_total": {"en": "Total reps", "zh": "累计次数", "hant": "累計次數"},
    "badge_t": {"en": "Badge unlocked", "zh": "解锁成就", "hant": "解鎖成就"},
    "badge_b": {"en": "2,000 squats", "zh": "深蹲 2,000 次", "hant": "深蹲 2,000 次"},
    "track_eyebrow": {"en": "04 · Progress", "zh": "04 · 进度", "hant": "04 · 進度"},
    "track_h2": {"en": "Check-ins, badges, hero cards.", "zh": "打卡、成就、达人卡片。", "hant": "打卡、成就、達人卡片。"},
    "track_lead": {
        "en": "Hit your daily goal on any exercise and the day is checked in. Keep the streak going, unlock milestones, and share a hero card after every workout.",
        "zh": "任一动作完成每日目标，当天就算打卡。保持连续打卡、解锁里程碑，每次练完都能分享一张达人卡片。",
        "hant": "任一動作完成每日目標，當天就算打卡。保持連續打卡、解鎖里程碑，每次練完都能分享一張達人卡片。",
    },
    "track_feat": {
        "en": [("Calendar heatmap", "See every day you trained at a glance."),
               ("Streaks &amp; badges", "Milestones for each exercise and your longest streak."),
               ("Hero card", "Three styles, exported at 1080 × 1920. Save it or share it.")],
        "zh": [("日历热力图", "哪天练过，一眼就能看到。"),
               ("连续打卡与成就", "每个动作的里程碑，以及最长连续天数。"),
               ("达人卡片", "三种风格，导出 1080 × 1920，可以保存或分享。")],
        "hant": [("日曆熱力圖", "哪天練過，一眼就能看到。"),
                 ("連續打卡與成就", "每個動作的里程碑，以及最長連續天數。"),
                 ("達人卡片", "三種風格，匯出 1080 × 1920，可以儲存或分享。")],
    },
    "guest_eyebrow": {"en": "05 · No sign-in needed", "zh": "05 · 不登录也能用", "hant": "05 · 不登入也能用"},
    "guest_h2": {"en": "Start counting in seconds.", "zh": "几秒钟就能开始计数。", "hant": "幾秒鐘就能開始計數。"},
    "guest_lead": {
        "en": "Guest mode does everything except save. Sign in with Google when you want your history kept on this phone.",
        "zh": "游客模式除了不保存，什么都能用。想把记录留在这台手机上时，再用 Google 账号登录。",
        "hant": "訪客模式除了不儲存，什麼都能用。想把紀錄留在這支手機上時，再用 Google 帳號登入。",
    },
    "guest_t": {"en": "Guest", "zh": "游客", "hant": "訪客"},
    "guest_list": {
        "en": ["Tracking &amp; counting, all 11 exercises", "Hero card for this session",
               "x:Cleared when you close the app", "x:No streaks or badges"],
        "zh": ["识别和计数，11 种动作全部可用", "本次训练的达人卡片", "x:关闭 App 后清空", "x:没有连续打卡和成就"],
        "hant": ["辨識和計數，11 種動作全部可用", "本次訓練的達人卡片", "x:關閉 App 後清空", "x:沒有連續打卡和成就"],
    },
    "in_t": {"en": "Signed in", "zh": "已登录", "hant": "已登入"},
    "in_list": {
        "en": ["Everything in guest mode", "Workouts saved on this phone", "Calendar check-ins &amp; badges", "Daily reminder"],
        "zh": ["游客模式的全部功能", "训练记录保存在这台手机上", "日历打卡和成就", "每日提醒"],
        "hant": ["訪客模式的全部功能", "訓練紀錄儲存在這支手機上", "日曆打卡和成就", "每日提醒"],
    },
    "setup_eyebrow": {"en": "06 · Phone setup", "zh": "06 · 手机摆放", "hant": "06 · 手機擺放"},
    "setup_h2": {"en": "Where to put your phone.", "zh": "手机放哪里。", "hant": "手機放哪裡。"},
    "setup_lead": {
        "en": "Most miscounts come from the camera not seeing your whole body. Good light, full body in frame.",
        "zh": "大多数计数不准，是因为摄像头没拍到全身。光线充足，全身入镜。",
        "hant": "大多數計數不準，是因為相機沒拍到全身。光線充足，全身入鏡。",
    },
    "setup_sq_t": {"en": "Squat · face the camera", "zh": "深蹲 · 正对镜头", "hant": "深蹲 · 正對鏡頭"},
    "setup_sq_aria": {
        "en": "Phone upright about 2 to 3 metres in front of you",
        "zh": "手机竖立在你前方约 2 到 3 米",
        "hant": "手機直立在你前方約 2 到 3 公尺",
    },
    "setup_sq_b": {
        "en": "Phone upright at waist height, 2–3 m away. Head to toe in frame.",
        "zh": "手机竖立在腰部高度，距离 2–3 米，从头到脚都在画面里。",
        "hant": "手機直立在腰部高度，距離 2–3 公尺，從頭到腳都在畫面裡。",
    },
    "setup_pu_t": {"en": "Push-up · side view, low", "zh": "俯卧撑 · 侧面放低", "hant": "伏地挺身 · 側面放低"},
    "setup_pu_aria": {
        "en": "Phone on the floor about 1.5 metres to your side",
        "zh": "手机放在你身体侧面约 1.5 米的地上",
        "hant": "手機放在你身體側面約 1.5 公尺的地上",
    },
    "setup_pu_b": {
        "en": "Phone on the floor beside you, side-on, so it sees you from head to feet.",
        "zh": "手机放在身体侧面的地上，侧对镜头，从头到脚都能拍到。",
        "hant": "手機放在身體側面的地上，側對鏡頭，從頭到腳都能拍到。",
    },
    "shots_eyebrow": {"en": "07 · Inside the app", "zh": "07 · App 内页", "hant": "07 · App 內頁"},
    "shots_h2": {"en": "A cyber-clean workout HUD.", "zh": "干净利落的赛博训练仪表盘。", "hant": "俐落的賽博訓練儀表板。"},
    "shots_aria": {"en": "App screenshots, scroll horizontally", "zh": "App 截图，可横向滑动", "hant": "App 截圖，可橫向滑動"},
    # 宣传视频（YouTube），首页截图下方，点击才加载播放器
    "video_cap": {
        "en": "30-second demo: live push-up counting, the finished set and the shareable hero card.",
        "zh": "30 秒演示：俯卧撑实时计数、练完的结算页和可分享的达人卡。",
        "hant": "30 秒示範：伏地挺身即時計數、練完的結算頁和可分享的達人卡。",
    },
    "video_play": {"en": "Play the 30-second demo video", "zh": "播放 30 秒演示视频", "hant": "播放 30 秒示範影片"},
    "shots": {
        "en": [("Today at a glance", "KINETIC home screen showing today's reps, a 12-day streak and the Start Scan button"),
               ("Live rep counting", "KINETIC counting squats with a green skeleton overlay and a rep counter"),
               ("Check-in calendar", "KINETIC check-in calendar heatmap for October"),
               ("Shareable hero card", "KINETIC hero card in neon, holo and mono styles")],
        "zh": [("今日概览", "KINETIC 首页：今日次数、连续打卡 12 天和开始识别按钮"),
               ("实时计数", "KINETIC 正在数深蹲：绿色骨架和计数器"),
               ("打卡日历", "KINETIC 十月打卡日历热力图"),
               ("达人卡片", "KINETIC 达人卡片的三种风格")],
        "hant": [("今日概覽", "KINETIC 首頁：今日次數、連續打卡 12 天和開始辨識按鈕"),
                 ("即時計數", "KINETIC 正在計算深蹲：綠色骨架和計數器"),
                 ("打卡日曆", "KINETIC 十月打卡日曆熱力圖"),
                 ("達人卡片", "KINETIC 達人卡片的三種風格")],
    },
    "faq_eyebrow": {"en": "08 · FAQ", "zh": "08 · 常见问题", "hant": "08 · 常見問題"},
    "faq_h2": {"en": "Questions, answered.", "zh": "常见问题。", "hant": "常見問題。"},
    "cta_eyebrow": {"en": "Free on Android", "zh": "Android 免费", "hant": "Android 免費"},
    "cta_lead": {
        "en": "11 exercises. On-device pose detection. Video never uploaded.",
        "zh": "11 种动作，本机姿态识别，画面从不上传。",
        "hant": "11 種動作，本機姿勢辨識，畫面從不上傳。",
    },
    "contact": {
        "en": "Questions, problems or ideas? Email <a href=\"mailto:{e}\">{e}</a> and we'll reply within {d} business days.",
        "zh": "使用中遇到问题、想反馈建议，请发邮件到 <a href=\"mailto:{e}\">{e}</a>，我们会在 {d} 个工作日内回复。",
        "hant": "使用時遇到問題、想回饋建議，請寄信到 <a href=\"mailto:{e}\">{e}</a>，我們會在 {d} 個工作天內回覆。",
    },
}

# ---------------------------------------------------------------- 动作

JOINT = {
    "knee": {"en": "Knee", "zh": "膝角", "hant": "膝角"},
    "elbow": {"en": "Elbow", "zh": "肘角", "hant": "肘角"},
    "hip": {"en": "Hip", "zh": "髋角", "hant": "髖角"},
    "shoulder": {"en": "Shoulder", "zh": "肩角", "hant": "肩角"},
}

# 关节角度怎么量（exercise.dart 里的三个关键点，夹角在中间那个点）
JOINT_DEF = {
    "knee": {"en": "the angle at your knee between thigh and shin (hip–knee–ankle)",
             "zh": "膝盖处大腿和小腿的夹角（髋–膝–踝）",
             "hant": "膝蓋處大腿和小腿的夾角（髖–膝–踝）"},
    "elbow": {"en": "the angle at your elbow between upper arm and forearm (shoulder–elbow–wrist)",
              "zh": "手肘处上臂和前臂的夹角（肩–肘–腕）",
              "hant": "手肘處上臂和前臂的夾角（肩–肘–腕）"},
    "hip": {"en": "the angle at your hip between torso and thigh (shoulder–hip–knee)",
            "zh": "髋部躯干和大腿的夹角（肩–髋–膝）",
            "hant": "髖部軀幹和大腿的夾角（肩–髖–膝）"},
    "shoulder": {"en": "the angle at your shoulder between torso and upper arm (hip–shoulder–elbow)",
                 "zh": "肩部躯干和上臂的夹角（髋–肩–肘）",
                 "hant": "肩部軀幹和上臂的夾角（髖–肩–肘）"},
}

# 左右两侧怎么判定（SideRule）
SIDES = {
    "clearest": {"en": "KINETIC uses whichever side of your body the camera sees more clearly.",
                 "zh": "KINETIC 取摄像头看得更清楚的那一侧身体来判定。",
                 "hant": "KINETIC 取相機看得更清楚的那一側身體來判定。"},
    "both": {"en": "Both sides must reach the angle for the rep to count.",
             "zh": "左右两侧都要到位，这一次才算。",
             "hant": "左右兩側都要到位，這一次才算。"},
    "either": {"en": "You can alternate sides: either side reaching the angle counts, and both sides must return to the start before the next rep.",
               "zh": "可以左右交替：任一侧到位就算，两侧都回到起始姿势后才开始下一次。",
               "hant": "可以左右交替：任一側到位就算，兩側都回到起始姿勢後才開始下一次。"},
}

# 每种姿态（Posture）的手机摆放方法，和 App 的引导文字一致
POSTURE = {
    "standing": {
        "short": {"en": "Face the camera", "zh": "正对镜头", "hant": "正對鏡頭"},
        "title": {"en": "Standing, facing the camera", "zh": "站立，正对镜头", "hant": "站立，正對鏡頭"},
        "steps": {
            "en": ["Stand the phone upright at about waist height.", "Step back 2–3 m so your whole body, head to feet, is in frame.", "Face the camera with your feet about shoulder-width apart."],
            "zh": ["手机竖立，高度大约在腰部。", "退后 2–3 米，让从头到脚的全身都在画面里。", "正对镜头站立，双脚与肩同宽。"],
            "hant": ["手機直立，高度大約在腰部。", "退後 2–3 公尺，讓從頭到腳的全身都在畫面裡。", "正對鏡頭站立，雙腳與肩同寬。"],
        },
    },
    "armsUp": {
        "short": {"en": "Face the camera, dumbbells at shoulders", "zh": "正对镜头，哑铃举到肩高", "hant": "正對鏡頭，啞鈴舉到肩高"},
        "title": {"en": "Standing, facing the camera, weights at shoulder height", "zh": "站立正对镜头，哑铃举到肩高", "hant": "站立正對鏡頭，啞鈴舉到肩高"},
        "steps": {
            "en": ["Stand the phone upright at about waist height, 2–3 m away.", "Face the camera with your whole body in frame.", "Start with the dumbbells at shoulder height, wrists above elbows. If your arms hang down, the app waits."],
            "zh": ["手机竖立在腰部高度，距离 2–3 米。", "正对镜头，全身入镜。", "从哑铃举到肩高开始，手腕在手肘上方。手臂自然下垂时 App 会等待，不会计数。"],
            "hant": ["手機直立在腰部高度，距離 2–3 公尺。", "正對鏡頭，全身入鏡。", "從啞鈴舉到肩高開始，手腕在手肘上方。手臂自然下垂時 App 會等待，不會計數。"],
        },
    },
    "standingSide": {
        "short": {"en": "Stand sideways", "zh": "侧对镜头站立", "hant": "側對鏡頭站立"},
        "title": {"en": "Standing, side-on to the camera", "zh": "站立，侧对镜头", "hant": "站立，側對鏡頭"},
        "steps": {
            "en": ["Stand the phone upright at about waist height, 2–3 m away.", "Turn sideways so the camera sees your profile.", "Leave room in front and behind you so your stepping leg stays in frame."],
            "zh": ["手机竖立在腰部高度，距离 2–3 米。", "侧身站立，让摄像头拍到你的侧面。", "前后留出空间，跨步的腿也要一直在画面里。"],
            "hant": ["手機直立在腰部高度，距離 2–3 公尺。", "側身站立，讓相機拍到你的側面。", "前後留出空間，跨步的腿也要一直在畫面裡。"],
        },
    },
    "plank": {
        "short": {"en": "Phone on the floor, side view", "zh": "手机放地上，侧面拍", "hant": "手機放地上，側面拍"},
        "title": {"en": "Plank position, phone low at your side", "zh": "平板支撑姿势，手机放低在身体侧面", "hant": "棒式姿勢，手機放低在身體側面"},
        "steps": {
            "en": ["Put the phone on the floor about 1.5 m to your side, leaning against something so it stands up.", "Turn your body side-on to the camera.", "Check that your head, hands and feet are all in frame."],
            "zh": ["手机放在身体侧面约 1.5 米的地上，靠着东西立起来。", "身体侧对镜头。", "确认头、手、脚都在画面里。"],
            "hant": ["手機放在身體側面約 1.5 公尺的地上，靠著東西立起來。", "身體側對鏡頭。", "確認頭、手、腳都在畫面裡。"],
        },
    },
    "floor": {
        "short": {"en": "Lie down, side view", "zh": "躺在地上，侧对镜头", "hant": "躺在地上，側對鏡頭"},
        "title": {"en": "Lying on the floor, side-on to the camera", "zh": "躺在地上，侧对镜头", "hant": "躺在地上，側對鏡頭"},
        "steps": {
            "en": ["Put the phone on the floor 1.5–2 m to your side, leaning against something so it stands up.", "Lie down with your body side-on to the camera.", "Check that your head, hips and feet are all in frame."],
            "zh": ["手机放在身体侧面 1.5–2 米的地上，靠着东西立起来。", "躺下，身体侧对镜头。", "确认头、髋部和脚都在画面里。"],
            "hant": ["手機放在身體側面 1.5–2 公尺的地上，靠著東西立起來。", "躺下，身體側對鏡頭。", "確認頭、髖部和腳都在畫面裡。"],
        },
    },
    "hanging": {
        "short": {"en": "Face the camera, hands on the bar", "zh": "双手握杠，正对镜头", "hant": "雙手握槓，正對鏡頭"},
        "title": {"en": "Hanging from a bar, facing the camera", "zh": "悬挂在单杠上，正对镜头", "hant": "懸掛在單槓上，正對鏡頭"},
        "steps": {
            "en": ["Place the phone in front of the bar, far enough back (usually 2–3 m) to see your hands on the bar.", "Face the camera.", "Check that your hands, elbows and body are all in frame while you hang."],
            "zh": ["手机放在单杠前方，往后放远一些（一般 2–3 米），能拍到握杠的双手。", "正对镜头。", "悬挂时确认双手、手肘和身体都在画面里。"],
            "hant": ["手機放在單槓前方，往後放遠一些（一般 2–3 公尺），能拍到握槓的雙手。", "正對鏡頭。", "懸掛時確認雙手、手肘和身體都在畫面裡。"],
        },
    },
}
POSTURE["lying"] = POSTURE["floor"]

# two=False：单角度，到位即计 1 次（俯卧撑）。ext=True：夹角变大算到位（RepDirection.extend）。
EXERCISES = [
    {
        "id": "pushup", "slug": "push-up-counter", "code": "PUSH-UP", "joint": "elbow", "two": False, "ext": False,
        "done": 90, "start": None, "sides": "clearest", "posture": "plank", "shot": True,
        "name": {"en": "Push-up", "zh": "俯卧撑", "hant": "伏地挺身"},
        "plural": {"en": "push-ups", "zh": "俯卧撑", "hant": "伏地挺身"},
        "std": {
            "en": "A standard push-up goes down until your upper arms are parallel to the floor, which is an elbow angle of about 90°. That is KINETIC's default.",
            "zh": "标准俯卧撑下压到上臂与地面平行，肘角约 90°，这也是 KINETIC 的默认值。",
            "hant": "標準伏地挺身下壓到上臂與地面平行，肘角約 90°，這也是 KINETIC 的預設值。",
        },
        "tips": {
            "en": ["Keep your body in one straight line from head to heels; don't let your hips sag or pike up.", "Hands slightly wider than your shoulders, elbows about 45° from your body.", "Lower with control and push the floor away. Fast, bouncy reps tend to stop short of 90°."],
            "zh": ["从头到脚跟保持一条直线，臀部不要塌下去，也不要撅起来。", "双手略宽于肩，手肘与身体约成 45°。", "有控制地下放，再把地面推开。太快、弹起来的动作往往压不到 90°。"],
            "hant": ["從頭到腳跟保持一條直線，臀部不要塌下去，也不要翹起來。", "雙手略寬於肩，手肘與身體約成 45°。", "有控制地下放，再把地面推開。太快、彈起來的動作往往壓不到 90°。"],
        },
        "miss": {
            "en": ["You stopped above 90°. A short, quick dip doesn't count.", "The phone is in front of or behind you. From the front, the elbow angle can't be measured well; move the phone to your side."],
            "zh": ["没压到 90°。浅浅地快速点一下不算。", "手机放在头前或脚后。从正面量不准肘角，请把手机挪到身体侧面。"],
            "hant": ["沒壓到 90°。淺淺地快速點一下不算。", "手機放在頭前或腳後。從正面量不準肘角，請把手機移到身體側面。"],
        },
    },
    {
        "id": "squat", "slug": "squat-counter", "code": "SQUAT", "joint": "knee", "two": True, "ext": False,
        "done": 110, "start": 160, "sides": "both", "posture": "standing", "shot": True,
        "name": {"en": "Squat", "zh": "深蹲", "hant": "深蹲"},
        "plural": {"en": "squats", "zh": "深蹲", "hant": "深蹲"},
        "std": {
            "en": "A standard squat goes down until your thighs are parallel to the floor, a knee angle of about 90°. When you face the camera your thighs point towards it and the measured angle reads larger, so the default is 110°.",
            "zh": "标准深蹲蹲到大腿与地面平行，膝角约 90°。正对镜头时大腿朝向镜头，量到的角度会偏大，所以默认值是 110°。",
            "hant": "標準深蹲蹲到大腿與地面平行，膝角約 90°。正對鏡頭時大腿朝向鏡頭，量到的角度會偏大，所以預設值是 110°。",
        },
        "tips": {
            "en": ["Feet about shoulder-width apart, toes turned out slightly.", "Sit your hips back and down; keep your chest up and heels on the floor.", "Stand all the way up between reps. Stopping halfway won't reach 160° and the next rep won't count."],
            "zh": ["双脚与肩同宽，脚尖略微外展。", "臀部向后向下坐，挺胸，脚跟不离地。", "每次都要完全站直。站到一半就往下蹲，到不了 160°，下一次不会计数。"],
            "hant": ["雙腳與肩同寬，腳尖略微外展。", "臀部向後向下坐，挺胸，腳跟不離地。", "每次都要完全站直。站到一半就往下蹲，到不了 160°，下一次不會計數。"],
        },
        "miss": {
            "en": ["Your knees didn't bend to 110°. Go a little lower; the app tells you when you're not deep enough.", "You didn't stand back up past 160° before the next squat."],
            "zh": ["膝角没到 110°。再蹲低一点，蹲得不够深时 App 会提醒你。", "下一次之前没有站回 160° 以上。"],
            "hant": ["膝角沒到 110°。再蹲低一點，蹲得不夠深時 App 會提醒你。", "下一次之前沒有站回 160° 以上。"],
        },
    },
    {
        "id": "lunge", "slug": "lunge-counter", "code": "LUNGE", "joint": "knee", "two": True, "ext": False,
        "done": 100, "start": 160, "sides": "either", "posture": "standingSide",
        "name": {"en": "Lunge", "zh": "弓步蹲", "hant": "弓箭步"},
        "plural": {"en": "lunges", "zh": "弓步蹲", "hant": "弓箭步"},
        "std": {
            "en": "In a standard lunge your front knee bends to about 90°. From the side the angle is measured accurately, so KINETIC leaves a 10° margin and counts at 100°.",
            "zh": "标准弓步蹲前腿膝盖弯到约 90°。侧面拍摄量得准，KINETIC 留了 10° 余量，膝角到 100° 就计数。",
            "hant": "標準弓箭步前腿膝蓋彎到約 90°。側面拍攝量得準，KINETIC 留了 10° 餘量，膝角到 100° 就計數。",
        },
        "tips": {
            "en": ["Take a long enough step that both knees can bend to about 90°.", "Keep your torso upright and your front knee over your ankle.", "Push back to standing tall before switching legs."],
            "zh": ["步子迈得够大，让两个膝盖都能弯到约 90°。", "上身保持直立，前腿膝盖在脚踝正上方。", "换腿前先蹬回站直。"],
            "hant": ["步子跨得夠大，讓兩個膝蓋都能彎到約 90°。", "上身保持直立，前腿膝蓋在腳踝正上方。", "換腳前先蹬回站直。"],
        },
        "miss": {
            "en": ["Your front knee stayed above 100°. Step a little further and drop your back knee towards the floor.", "Your stepping leg left the frame. Move the phone back so there is room in front of you."],
            "zh": ["前腿膝角没到 100°。步子再大一点，后腿膝盖往地面沉。", "跨出去的腿出了画面。把手机往后放，前方留出空间。"],
            "hant": ["前腿膝角沒到 100°。步子再大一點，後腿膝蓋往地面沉。", "跨出去的腿出了畫面。把手機往後放，前方留出空間。"],
        },
    },
    {
        "id": "situp", "slug": "sit-up-counter", "code": "SIT-UP", "joint": "hip", "two": True, "ext": False,
        "done": 70, "start": 120, "sides": "clearest", "posture": "floor",
        "name": {"en": "Sit-up", "zh": "仰卧起坐", "hant": "仰臥起坐"},
        "plural": {"en": "sit-ups", "zh": "仰卧起坐", "hant": "仰臥起坐"},
        "std": {
            "en": "Lying with bent knees, your hip angle is about 130°. When you sit up until your elbows touch your knees, your torso is close to vertical and the hip angle is about 60°. KINETIC counts at 70° and waits for you to lie back past 120°.",
            "zh": "屈膝躺下时髋角约 130°；起身到肘碰膝时躯干接近竖直，髋角约 60°。KINETIC 在髋角到 70° 时计数，躺回 120° 以上才开始下一次。",
            "hant": "屈膝躺下時髖角約 130°；起身到肘碰膝時軀幹接近垂直，髖角約 60°。KINETIC 在髖角到 70° 時計數，躺回 120° 以上才開始下一次。",
        },
        "tips": {
            "en": ["Bend your knees and keep your feet flat on the floor.", "Curl up until your elbows reach your knees.", "Lie back far enough each time; your shoulders should come close to the floor."],
            "zh": ["屈膝，双脚平放在地面。", "卷起上身，直到手肘碰到膝盖。", "每次都要躺回去，肩膀接近地面。"],
            "hant": ["屈膝，雙腳平放在地面。", "捲起上身，直到手肘碰到膝蓋。", "每次都要躺回去，肩膀接近地面。"],
        },
        "miss": {
            "en": ["You didn't sit up far enough to reach 70°.", "You didn't lie back past 120° before the next rep."],
            "zh": ["起身不够高，髋角没到 70°。", "下一次之前没有躺回 120° 以上。"],
            "hant": ["起身不夠高，髖角沒到 70°。", "下一次之前沒有躺回 120° 以上。"],
        },
    },
    {
        "id": "jumping_jack", "slug": "jumping-jack-counter", "code": "JUMPING JACK", "joint": "shoulder", "two": True, "ext": True,
        "done": 150, "start": 40, "sides": "both", "posture": "standing",
        "name": {"en": "Jumping jack", "zh": "开合跳", "hant": "開合跳"},
        "plural": {"en": "jumping jacks", "zh": "开合跳", "hant": "開合跳"},
        "std": {
            "en": "Your arms go from your sides (a shoulder angle of about 15°) to overhead (about 170°), both arms together. KINETIC counts at 150° and waits for your arms to come back below 40°.",
            "zh": "手臂从体侧（肩角约 15°）举过头顶（约 170°），两臂同时。KINETIC 在肩角到 150° 时计数，手臂放回 40° 以下才开始下一次。",
            "hant": "手臂從體側（肩角約 15°）舉過頭頂（約 170°），兩臂同時。KINETIC 在肩角到 150° 時計數，手臂放回 40° 以下才開始下一次。",
        },
        "tips": {
            "en": ["Face the camera so both arms are visible.", "Raise your arms all the way overhead on every rep.", "Bring your arms right back down to your sides."],
            "zh": ["正对镜头，让两只手臂都拍得到。", "每次都把手臂举过头顶。", "手臂要放回到体侧。"],
            "hant": ["正對鏡頭，讓兩隻手臂都拍得到。", "每次都把手臂舉過頭頂。", "手臂要放回到體側。"],
        },
        "miss": {
            "en": ["One arm stopped short of overhead. Both arms must reach 150°.", "Your hands left the top of the frame. Step back a little."],
            "zh": ["有一只手没举过头顶。两只手臂都要到 150°。", "举手时手出了画面上方。往后退一点。"],
            "hant": ["有一隻手沒舉過頭頂。兩隻手臂都要到 150°。", "舉手時手超出畫面上方。往後退一點。"],
        },
    },
    {
        "id": "glute_bridge", "slug": "glute-bridge-counter", "code": "GLUTE BRIDGE", "joint": "hip", "two": True, "ext": True,
        "done": 165, "start": 140, "sides": "clearest", "posture": "lying",
        "name": {"en": "Glute bridge", "zh": "臀桥", "hant": "臀橋"},
        "plural": {"en": "glute bridges", "zh": "臀桥", "hant": "臀橋"},
        "std": {
            "en": "Lying with bent knees your hip angle is about 135°. At the top, your shoulders, hips and knees form a straight line (180°). KINETIC leaves a 15° margin and counts at 165°.",
            "zh": "屈膝躺下时髋角约 135°；顶起到肩、髋、膝成一条直线时是 180°。KINETIC 留了 15° 余量，髋角到 165° 就计数。",
            "hant": "屈膝躺下時髖角約 135°；頂起到肩、髖、膝成一條直線時是 180°。KINETIC 留了 15° 餘量，髖角到 165° 就計數。",
        },
        "tips": {
            "en": ["Feet flat, about hip-width apart, heels close to your hips.", "Squeeze your glutes and lift until shoulders, hips and knees line up.", "Lower your hips back down between reps."],
            "zh": ["双脚平放，与髋同宽，脚跟靠近臀部。", "收紧臀部向上顶，直到肩、髋、膝成一条线。", "每次之间把臀部放回地面。"],
            "hant": ["雙腳平放，與髖同寬，腳跟靠近臀部。", "收緊臀部向上頂，直到肩、髖、膝成一條線。", "每次之間把臀部放回地面。"],
        },
        "miss": {
            "en": ["Your hips didn't lift high enough to reach 165°.", "You didn't lower your hips below 140° before the next rep."],
            "zh": ["臀部顶得不够高，髋角没到 165°。", "下一次之前臀部没有放低到 140° 以下。"],
            "hant": ["臀部頂得不夠高，髖角沒到 165°。", "下一次之前臀部沒有放低到 140° 以下。"],
        },
    },
    {
        "id": "leg_raise", "slug": "leg-raise-counter", "code": "LEG RAISE", "joint": "hip", "two": True, "ext": False,
        "done": 100, "start": 160, "sides": "clearest", "posture": "lying",
        "name": {"en": "Leg raise", "zh": "仰卧抬腿", "hant": "仰臥抬腿"},
        "plural": {"en": "leg raises", "zh": "仰卧抬腿", "hant": "仰臥抬腿"},
        "std": {
            "en": "With your legs straight and flat, your hip angle is about 180°; raised to vertical it is 90°. KINETIC counts at 100° and waits for your legs to lower past 160°.",
            "zh": "双腿伸直平放时髋角约 180°，抬到与地面垂直是 90°。KINETIC 在髋角到 100° 时计数，双腿放低到 160° 以上才开始下一次。",
            "hant": "雙腿伸直平放時髖角約 180°，抬到與地面垂直是 90°。KINETIC 在髖角到 100° 時計數，雙腿放低到 160° 以上才開始下一次。",
        },
        "tips": {
            "en": ["Lie flat and keep your legs as straight as you can.", "Press your lower back into the floor while you lift.", "Lower slowly; you don't need to touch the floor, just get past 160°."],
            "zh": ["平躺，双腿尽量伸直。", "抬腿时下背部贴住地面。", "慢慢放下，不用碰地，放低过 160° 就行。"],
            "hant": ["平躺，雙腿盡量伸直。", "抬腿時下背部貼住地面。", "慢慢放下，不用碰地，放低過 160° 就行。"],
        },
        "miss": {
            "en": ["Your legs didn't rise to 100°.", "You didn't lower your legs past 160° before the next rep."],
            "zh": ["双腿没抬到 100°。", "下一次之前双腿没有放低到 160° 以上。"],
            "hant": ["雙腿沒抬到 100°。", "下一次之前雙腿沒有放低到 160° 以上。"],
        },
    },
    {
        "id": "pullup", "slug": "pull-up-counter", "code": "PULL-UP", "joint": "elbow", "two": True, "ext": False,
        "done": 70, "start": 150, "sides": "both", "posture": "hanging",
        "name": {"en": "Pull-up", "zh": "引体向上", "hant": "引體向上"},
        "plural": {"en": "pull-ups", "zh": "引体向上", "hant": "引體向上"},
        "std": {
            "en": "A full pull-up starts from straight arms (an elbow angle over 160°) and pulls until your chin is over the bar (about 50°–70°). KINETIC counts at 70° and waits for you to lower past 150°.",
            "zh": "完整的引体向上从手臂伸直（肘角 160° 以上）开始，拉到下巴过杠（肘角约 50°~70°）。KINETIC 在肘角到 70° 时计数，放下到 150° 以上才开始下一次。",
            "hant": "完整的引體向上從手臂伸直（肘角 160° 以上）開始，拉到下巴過槓（肘角約 50°~70°）。KINETIC 在肘角到 70° 時計數，放下到 150° 以上才開始下一次。",
        },
        "tips": {
            "en": ["Start each rep from a dead hang with your arms straight.", "Pull until your chin clears the bar.", "Control the way down instead of dropping."],
            "zh": ["每次都从手臂伸直的悬挂开始。", "拉到下巴过杠。", "有控制地下放，不要直接掉下来。"],
            "hant": ["每次都從手臂伸直的懸掛開始。", "拉到下巴過槓。", "有控制地下放，不要直接掉下來。"],
        },
        "miss": {
            "en": ["You didn't pull high enough to reach 70°.", "You didn't lower to straight arms (past 150°) before the next rep. Half reps at the top don't count."],
            "zh": ["拉得不够高，肘角没到 70°。", "下一次之前没有放到手臂伸直（150° 以上）。只在上半程来回不算。"],
            "hant": ["拉得不夠高，肘角沒到 70°。", "下一次之前沒有放到手臂伸直（150° 以上）。只在上半程來回不算。"],
        },
    },
    {
        "id": "bicep_curl", "slug": "bicep-curl-counter", "code": "DB CURL", "joint": "elbow", "two": True, "ext": False,
        "done": 50, "start": 150, "sides": "either", "posture": "standing",
        "name": {"en": "Bicep curl", "zh": "哑铃弯举", "hant": "啞鈴彎舉"},
        "plural": {"en": "bicep curls", "zh": "哑铃弯举", "hant": "啞鈴彎舉"},
        "std": {
            "en": "A full curl goes from a straight arm (about 170°) until your forearm is close to your upper arm (about 40°). KINETIC counts at 50°. Curling both arms together or alternating both count.",
            "zh": "完整的弯举从手臂伸直（约 170°）弯到前臂贴近上臂（约 40°）。KINETIC 在肘角到 50° 时计数，双手同时或左右交替都算。",
            "hant": "完整的彎舉從手臂伸直（約 170°）彎到前臂貼近上臂（約 40°）。KINETIC 在肘角到 50° 時計數，雙手同時或左右交替都算。",
        },
        "tips": {
            "en": ["Keep your elbows close to your sides; don't swing the weight.", "Curl until the dumbbell is near your shoulder.", "Straighten your arm fully at the bottom of each rep."],
            "zh": ["手肘贴近身体两侧，不要甩动哑铃。", "弯举到哑铃接近肩膀。", "每次在底部把手臂完全伸直。"],
            "hant": ["手肘貼近身體兩側，不要甩動啞鈴。", "彎舉到啞鈴接近肩膀。", "每次在底部把手臂完全伸直。"],
        },
        "miss": {
            "en": ["You didn't curl up to 50°.", "You didn't straighten your arm past 150° before the next rep."],
            "zh": ["没弯举到 50°。", "下一次之前手臂没有伸直到 150° 以上。"],
            "hant": ["沒彎舉到 50°。", "下一次之前手臂沒有伸直到 150° 以上。"],
        },
    },
    {
        "id": "lateral_raise", "slug": "lateral-raise-counter", "code": "LATERAL RAISE", "joint": "shoulder", "two": True, "ext": True,
        "done": 80, "start": 30, "sides": "both", "posture": "standing",
        "name": {"en": "Lateral raise", "zh": "侧平举", "hant": "側平舉"},
        "plural": {"en": "lateral raises", "zh": "侧平举", "hant": "側平舉"},
        "std": {
            "en": "Your arms rise from your sides to shoulder height, a shoulder angle of 90°. KINETIC leaves a 10° margin and counts at 80°, then waits for your arms to come back below 30°.",
            "zh": "手臂从体侧抬到与肩同高，肩角 90°。KINETIC 留了 10° 余量，肩角到 80° 就计数，手臂放回 30° 以下才开始下一次。",
            "hant": "手臂從體側抬到與肩同高，肩角 90°。KINETIC 留了 10° 餘量，肩角到 80° 就計數，手臂放回 30° 以下才開始下一次。",
        },
        "tips": {
            "en": ["Use a light weight and lift with a slight bend in your elbows.", "Raise both arms out to the side until they are level with your shoulders.", "Lower slowly all the way back to your sides."],
            "zh": ["用轻一点的哑铃，手肘微屈向上抬。", "两臂向两侧抬起，直到与肩同高。", "慢慢放回到体侧。"],
            "hant": ["用輕一點的啞鈴，手肘微屈向上抬。", "兩臂向兩側抬起，直到與肩同高。", "慢慢放回到體側。"],
        },
        "miss": {
            "en": ["One arm stopped below shoulder height. Both arms must reach 80°.", "You didn't lower your arms below 30° before the next rep."],
            "zh": ["有一只手没抬到肩高。两只手臂都要到 80°。", "下一次之前手臂没有放回 30° 以下。"],
            "hant": ["有一隻手沒抬到肩高。兩隻手臂都要到 80°。", "下一次之前手臂沒有放回 30° 以下。"],
        },
    },
    {
        "id": "overhead_press", "slug": "shoulder-press-counter", "code": "SHOULDER PRESS", "joint": "elbow", "two": True, "ext": True,
        "done": 160, "start": 90, "sides": "both", "posture": "armsUp",
        "name": {"en": "Overhead press", "zh": "肩上推举", "hant": "肩上推舉"},
        "plural": {"en": "overhead presses", "zh": "肩上推举", "hant": "肩上推舉"},
        "std": {
            "en": "Also called the shoulder press: the dumbbells start at shoulder height (an elbow angle of about 80°) and press until your arms are straight (over 170°). KINETIC counts at 160° and waits for you to lower below 90°.",
            "zh": "也叫肩推：哑铃从肩膀高度（肘角约 80°）推到手臂伸直（170° 以上）。KINETIC 在肘角到 160° 时计数，放回 90° 以下才开始下一次。",
            "hant": "也叫肩推：啞鈴從肩膀高度（肘角約 80°）推到手臂伸直（170° 以上）。KINETIC 在肘角到 160° 時計數，放回 90° 以下才開始下一次。",
        },
        "tips": {
            "en": ["Brace your core and avoid leaning back.", "Press straight up until your arms are fully extended.", "Bring the dumbbells all the way back to shoulder height."],
            "zh": ["收紧核心，身体不要后仰。", "垂直向上推，直到手臂完全伸直。", "把哑铃放回到肩膀高度。"],
            "hant": ["收緊核心，身體不要後仰。", "垂直向上推，直到手臂完全伸直。", "把啞鈴放回到肩膀高度。"],
        },
        "miss": {
            "en": ["Your arms didn't straighten to 160°.", "Your arms hung down by your sides. The app only counts when your wrists are above your elbows, so a straight arm hanging down isn't mistaken for a press."],
            "zh": ["手臂没推直到 160°。", "手臂垂在身体两侧。App 只在手腕高于手肘时计数，避免把垂下的直臂误当成推举。"],
            "hant": ["手臂沒推直到 160°。", "手臂垂在身體兩側。App 只在手腕高於手肘時計數，避免把垂下的直臂誤當成推舉。"],
        },
    },
]

# 动作页的通用文案
EXP = {
    "title": {
        "en": "{name} Counter – Count {Plural} Automatically with Your Phone Camera",
        "zh": "{name}计数器：用手机摄像头自动数{name}",
        "hant": "{name}計數器：用手機相機自動計算{name}",
    },
    "h1": {"en": "{name} counter", "zh": "{name}计数器", "hant": "{name}計數器"},
    "desc": {
        "en": "How KINETIC counts {plural} with your phone camera: {joint_l} angle {rule}. Phone setup, common mistakes and how to adjust the threshold.",
        "zh": "KINETIC 怎么用手机摄像头数{name}：{joint}{rule}。手机怎么摆、为什么有时不计数、怎么调整角度。",
        "hant": "KINETIC 怎麼用手機相機計算{name}：{joint}{rule}。手機怎麼擺、為什麼有時不計數、怎麼調整角度。",
    },
    # answer：单角度 / 变小算到位 / 变大算到位
    "ans_single": {
        "en": "KINETIC counts one {name_l} the moment your {joint_l} angle reaches {done}° or less at the bottom. Come back up, and it's ready for the next rep.",
        "zh": "{joint}下压到 {done}° 或更小时，KINETIC 立即记 1 次{name}；撑起后自动等待下一次。",
        "hant": "{joint}下壓到 {done}° 或更小時，KINETIC 立即記 1 次{name}；撐起後自動等待下一次。",
    },
    "ans_flex": {
        "en": "KINETIC counts one {name_l} when your {joint_l} angle drops to {done}° or less and then comes back to {start}° or more.",
        "zh": "{joint}降到 {done}° 或更小、再回到 {start}° 或更大，KINETIC 记 1 次{name}。",
        "hant": "{joint}降到 {done}° 或更小、再回到 {start}° 或更大，KINETIC 記 1 次{name}。",
    },
    "ans_ext": {
        "en": "KINETIC counts one {name_l} when your {joint_l} angle opens to {done}° or more and then comes back to {start}° or less.",
        "zh": "{joint}打开到 {done}° 或更大、再回到 {start}° 或更小，KINETIC 记 1 次{name}。",
        "hant": "{joint}打開到 {done}° 或更大、再回到 {start}° 或更小，KINETIC 記 1 次{name}。",
    },
    "rule_single": {"en": "{done}° or less counts", "zh": " ≤ {done}° 即计 1 次", "hant": " ≤ {done}° 即記 1 次"},
    "rule_flex": {"en": "{done}° or less, then back to {start}°", "zh": " ≤ {done}°、再回到 ≥ {start}°", "hant": " ≤ {done}°、再回到 ≥ {start}°"},
    "rule_ext": {"en": "{done}° or more, then back to {start}°", "zh": " ≥ {done}°、再回到 ≤ {start}°", "hant": " ≥ {done}°、再回到 ≤ {start}°"},
    "spec_joint": {"en": "Joint", "zh": "判定关节", "hant": "判定關節"},
    "spec_done": {"en": "Counts at", "zh": "完成角度", "hant": "完成角度"},
    "spec_start": {"en": "Start angle", "zh": "起始角度", "hant": "起始角度"},
    "spec_phone": {"en": "Phone", "zh": "手机摆放", "hant": "手機擺放"},
    "h_how": {"en": "How KINETIC counts {plural}", "zh": "KINETIC 怎么数{name}", "hant": "KINETIC 怎麼計算{name}"},
    "measured": {
        "en": "The {joint_l} angle is {def}. ",
        "zh": "{joint}指的是{def}。",
        "hant": "{joint}指的是{def}。",
    },
    "single_note": {
        "en": "Push-ups use a single angle: there is no start angle to return to, so fast sets aren't missed.",
        "zh": "俯卧撑用单角度判定：不需要回到起始角度，做得快也不会漏数。",
        "hant": "伏地挺身用單角度判定：不需要回到起始角度，做得快也不會漏數。",
    },
    "h_setup": {"en": "Where to put your phone", "zh": "手机怎么摆", "hant": "手機怎麼擺"},
    "h_form": {"en": "Good form", "zh": "动作要点", "hant": "動作要點"},
    "h_miss": {"en": "Why a rep might not count", "zh": "为什么有时不计数", "hant": "為什麼有時不計數"},
    "miss_common": {
        "en": ["Part of your body is out of frame or hidden. KINETIC pauses and shows a hint; those frames are skipped, and when you're back in view it carries on without counting the same rep twice.",
               "The room is dark or there is a bright window behind you. Turn on a light and face away from the window."],
        "zh": ["身体有一部分出了画面或被挡住。KINETIC 会暂停判定并显示提示，这些画面直接跳过；回到画面后接着数，不会重复计数。",
               "房间太暗，或者身后有明亮的窗户。开灯，并背对窗户。"],
        "hant": ["身體有一部分超出畫面或被擋住。KINETIC 會暫停判定並顯示提示，這些畫面直接略過；回到畫面後接著數，不會重複計數。",
                 "房間太暗，或者身後有明亮的窗戶。開燈，並背對窗戶。"],
    },
    "h_adjust": {"en": "Too strict or too loose?", "zh": "觉得太严或太松？", "hant": "覺得太嚴或太鬆？"},
    "adjust": {
        "en": "Open the angle panel on the tracking screen and drag the thresholds. The defaults follow standard form with a little margin; beginners can loosen them, and you can tighten them as you get stronger. Each exercise keeps its own setting.",
        "zh": "在识别页打开角度面板，拖动阈值即可。默认值按标准动作设定、留了一点余量；刚开始练可以放宽，练得好了再收紧。每种动作单独保存设置。",
        "hant": "在辨識頁打開角度面板，拖動門檻即可。預設值依標準動作設定、留了一點餘量；剛開始練可以放寬，練得好了再收緊。每種動作分別儲存設定。",
    },
    "h_more": {"en": "Other exercises", "zh": "其他动作", "hant": "其他動作"},
    "shot_alt": {
        "en": "KINETIC counting {plural} with a skeleton overlay",
        "zh": "KINETIC 正在数{name}，画面上叠加骨架",
        "hant": "KINETIC 正在計算{name}，畫面上疊加骨架",
    },
    "hub_title": {
        "en": "Exercises KINETIC Counts – 11 Exercises with Joint Angles",
        "zh": "KINETIC 能数的 11 种动作和判定角度",
        "hant": "KINETIC 能計算的 11 種動作和判定角度",
    },
    "hub_h1": {"en": "11 exercises, counted for you", "zh": "11 种动作，自动计数", "hant": "11 種動作，自動計數"},
    "hub_desc": {
        "en": "Every exercise KINETIC counts, with the joint it measures, the default angles and where to put your phone.",
        "zh": "KINETIC 能数的全部动作：判定关节、默认角度和手机摆放方法。",
        "hant": "KINETIC 能計算的全部動作：判定關節、預設角度和手機擺放方法。",
    },
    "hub_lead": {
        "en": "Each exercise is counted from one joint angle. Pick an exercise to see exactly when a rep counts and how to set up your phone.",
        "zh": "每种动作按一个关节角度计数。点开动作，看什么时候算一次、手机怎么摆。",
        "hant": "每種動作依一個關節角度計數。點開動作，看什麼時候算一次、手機怎麼擺。",
    },
}

# ---------------------------------------------------------------- 常见问题

FAQ = [
    ("how", {
        "en": ("How does KINETIC count reps?", "KINETIC tracks your joints with the phone camera and measures joint angles. A squat counts when your knee angle drops to 110° or less and comes back above 160°. Pose detection runs on the phone."),
        "zh": ("KINETIC 怎么计数？", "KINETIC 用手机摄像头识别你的关节位置，计算关节角度。比如膝角降到 110° 或更小、再站回 160° 以上，记 1 次深蹲。姿态识别在手机上完成。"),
        "hant": ("KINETIC 怎麼計數？", "KINETIC 用手機相機辨識你的關節位置，計算關節角度。例如膝角降到 110° 或更小、再站回 160° 以上，記 1 次深蹲。姿勢辨識在手機上完成。"),
    }),
    ("video", {
        "en": ("Is my video uploaded?", "No. Video is processed on your phone and never recorded or uploaded. Workout records are stored only on this device."),
        "zh": ("画面会上传吗？", "不会。画面在手机上处理，不录像也不上传。训练记录只保存在这台设备上。"),
        "hant": ("畫面會上傳嗎？", "不會。畫面在手機上處理，不錄影也不上傳。訓練紀錄只儲存在這台裝置上。"),
    }),
    ("off", {
        "en": ("The count seems off. What can I do?", "Keep your whole body in frame with good lighting. Face the camera for squats; for push-ups, put the phone on the floor beside you so it sees you from the side. You can also adjust the angle thresholds in the app. See <a href=\"{p}/guides/phone-placement/\">phone setup for every exercise</a>."),
        "zh": ("计数不准怎么办？", "让全身入镜、光线充足。深蹲时正对镜头；俯卧撑时把手机放在身体侧面的地上，从侧面拍。也可以在 App 里调整角度阈值。详见<a href=\"{p}/guides/phone-placement/\">各动作的手机摆放方法</a>。"),
        "hant": ("計數不準怎麼辦？", "讓全身入鏡、光線充足。深蹲時正對鏡頭；伏地挺身時把手機放在身體側面的地上，從側面拍。也可以在 App 裡調整角度門檻。詳見<a href=\"{p}/guides/phone-placement/\">各動作的手機擺放方法</a>。"),
    }),
    ("signin", {
        "en": ("Do I need to sign in?", "No. Guest mode counts reps for every exercise but doesn't save workouts. Sign in with Google to save workouts on this phone, track check-ins and earn badges."),
        "zh": ("必须登录吗？", "不用。游客模式下所有动作都能识别计数，只是不保存记录。用 Google 账号登录后，训练记录保存在这台手机上，还能打卡、解锁成就。"),
        "hant": ("一定要登入嗎？", "不用。訪客模式下所有動作都能辨識計數，只是不儲存紀錄。用 Google 帳號登入後，訓練紀錄儲存在這支手機上，還能打卡、解鎖成就。"),
    }),
    ("newphone", {
        "en": ("Will my workouts move to a new phone?", "Workouts are stored only on your phone, with no cloud backup. You can export them from Settings › Data &amp; storage and keep the file yourself."),
        "zh": ("换手机后记录还在吗？", "记录只存在这台手机上，没有云端备份。可以在「设置 › 数据与存储」导出数据，自己保存文件。"),
        "hant": ("換手機後紀錄還在嗎？", "紀錄只存在這支手機上，沒有雲端備份。可以在「設定 › 資料與儲存」匯出資料，自己保存檔案。"),
    }),
    ("which", {
        "en": ("Which exercises can KINETIC count?", "11 exercises: push-ups, squats, lunges, sit-ups, jumping jacks, glute bridges, leg raises, pull-ups, bicep curls, lateral raises and overhead presses. <a href=\"{p}/exercises/\">See how each one is counted</a>."),
        "zh": ("能数哪些动作？", "11 种：俯卧撑、深蹲、弓步蹲、仰卧起坐、开合跳、臀桥、仰卧抬腿、引体向上、哑铃弯举、侧平举、肩上推举。<a href=\"{p}/exercises/\">查看每种动作怎么数</a>。"),
        "hant": ("能計算哪些動作？", "11 種：伏地挺身、深蹲、弓箭步、仰臥起坐、開合跳、臀橋、仰臥抬腿、引體向上、啞鈴彎舉、側平舉、肩上推舉。<a href=\"{p}/exercises/\">查看每種動作怎麼數</a>。"),
    }),
    ("free", {
        "en": ("Is KINETIC free?", "Yes. KINETIC is free to download and has no ads."),
        "zh": ("KINETIC 免费吗？", "免费。KINETIC 可以免费下载，没有广告。"),
        "hant": ("KINETIC 免費嗎？", "免費。KINETIC 可以免費下載，沒有廣告。"),
    }),
    ("offline", {
        "en": ("Does it work offline?", "Yes. Pose detection runs on the phone, so counting works without an internet connection. Signing in with Google needs a connection."),
        "zh": ("没有网络能用吗？", "能。姿态识别在手机上完成，没有网络也能计数。用 Google 账号登录时需要联网。"),
        "hant": ("沒有網路能用嗎？", "能。姿勢辨識在手機上完成，沒有網路也能計數。用 Google 帳號登入時需要連網。"),
    }),
    ("iphone", {
        "en": ("Is there an iPhone version?", "Not yet. KINETIC is currently available on Android only."),
        "zh": ("有 iPhone 版吗？", "暂时没有，目前只有 Android 版。"),
        "hant": ("有 iPhone 版嗎？", "暫時沒有，目前只有 Android 版。"),
    }),
    ("strict", {
        "en": ("Can I make counting stricter or looser?", "Yes. Open the angle panel on the tracking screen and drag the thresholds. Each exercise keeps its own setting."),
        "zh": ("能调整计数的严格程度吗？", "能。在识别页打开角度面板，拖动阈值即可，每种动作单独保存。"),
        "hant": ("能調整計數的嚴格程度嗎？", "能。在辨識頁打開角度面板，拖動門檻即可，每種動作分別儲存。"),
    }),
    ("camera", {
        "en": ("Can I use the front or back camera?", "Both. Switch cameras with the button at the top of the tracking screen. With the front camera you can watch yourself on screen."),
        "zh": ("能用前置或后置摄像头吗？", "都可以，在识别页顶部的按钮切换。用前置摄像头能在屏幕上看到自己。"),
        "hant": ("能用前鏡頭或後鏡頭嗎？", "都可以，在辨識頁頂部的按鈕切換。用前鏡頭能在螢幕上看到自己。"),
    }),
    ("voice", {
        "en": ("Does it call out my reps?", "Yes. Voice feedback calls out your reps, so you don't need to look at the screen."),
        "zh": ("会语音报数吗？", "会。语音报数，练的时候不用盯着屏幕。"),
        "hant": ("會語音報數嗎？", "會。語音報數，練的時候不用盯著螢幕。"),
    }),
    ("export", {
        "en": ("Can I export my workouts?", "Yes. In Settings › Data &amp; storage you can export your workouts as CSV (opens in any spreadsheet app) or JSON (full backup)."),
        "zh": ("能导出训练记录吗？", "能。在「设置 › 数据与存储」可以导出 CSV（表格软件直接打开）或 JSON（完整数据）。"),
        "hant": ("能匯出訓練紀錄嗎？", "能。在「設定 › 資料與儲存」可以匯出 CSV（試算表軟體直接開啟）或 JSON（完整資料）。"),
    }),
    ("delete", {
        "en": ("How do I delete my account and data?", "In the app, go to Settings › Data &amp; storage › Delete account and data. Uninstalling also deletes everything on the phone. <a href=\"{p}/delete-account.html\">More options</a>."),
        "zh": ("怎么删除账号和数据？", "在 App 里进入「设置 › 数据与存储 › 删除账号与数据」。卸载 App 也会删除手机上的全部数据。<a href=\"{p}/delete-account.html\">更多方式</a>。"),
        "hant": ("怎麼刪除帳號和資料？", "在 App 裡進入「設定 › 資料與儲存 › 刪除帳號與資料」。解除安裝 App 也會刪除手機上的全部資料。<a href=\"{p}/delete-account.html\">更多方式</a>。"),
    }),
]

FAQP = {
    "title": {"en": "KINETIC FAQ – AI Rep Counter Questions Answered", "zh": "KINETIC 常见问题", "hant": "KINETIC 常見問題"},
    "h1": {"en": "Frequently asked questions", "zh": "常见问题", "hant": "常見問題"},
    "desc": {
        "en": "How KINETIC counts reps, whether video is uploaded, sign-in, offline use, exporting and deleting data.",
        "zh": "KINETIC 怎么计数、画面会不会上传、要不要登录、能否离线使用、导出和删除数据。",
        "hant": "KINETIC 怎麼計數、畫面會不會上傳、要不要登入、能否離線使用、匯出和刪除資料。",
    },
    "more": {
        "en": "Didn't find your answer? Email <a href=\"mailto:{e}\">{e}</a>.",
        "zh": "没找到答案？请发邮件到 <a href=\"mailto:{e}\">{e}</a>。",
        "hant": "沒找到答案？請寄信到 <a href=\"mailto:{e}\">{e}</a>。",
    },
}
