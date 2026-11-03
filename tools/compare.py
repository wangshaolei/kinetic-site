"""同类 App 对比页的数据（三种语言）。

每一格都要能在对方的商店页上找到出处：只写商店页上写明的事实，商店页没写的写「未注明」，
不写自己的推测或主观评价。查阅时用美国区商店页（Google Play 加 &hl=en_US&gl=US）。
重新核对后改 CHECKED，以及 build.py 的 UPDATED。对方反馈有误的，核实后当天改。
"""

CHECKED = "2026-11-03"

TH = {
    "app": {"en": "App", "zh": "App", "hant": "App"},
    "platform": {"en": "Platform", "zh": "平台", "hant": "平台"},
    "price": {"en": "Price", "zh": "价格", "hant": "價格"},
    "exercises": {"en": "Exercises counted by camera", "zh": "摄像头能数的动作", "hant": "相機能數的動作"},
    "video": {"en": "Camera video (as stated)", "zh": "画面怎么处理（商店页说法）", "hant": "畫面怎麼處理（商店頁說法）"},
    "data": {"en": "Store privacy declaration", "zh": "商店隐私声明", "hant": "商店隱私聲明"},
    "extras": {"en": "Also offers", "zh": "其他功能", "hant": "其他功能"},
}

# url 为 None 的是 KINETIC 自己，链到首页
APPS = [
    {
        "name": "KINETIC: AI Rep Counter",
        "dev": "shaolei wang",
        "url": None,
        "platform": {"en": "Android", "zh": "Android", "hant": "Android"},
        "price": {
            "en": "Free, no ads, no in-app purchases",
            "zh": "免费，无广告，无应用内购买",
            "hant": "免費，無廣告，無應用程式內購買",
        },
        "exercises": {
            "en": "11: squats, push-ups, lunges, sit-ups, jumping jacks, glute bridges, leg raises, pull-ups, bicep curls, lateral raises, overhead presses",
            "zh": "11 种：深蹲、俯卧撑、弓步蹲、仰卧起坐、开合跳、臀桥、仰卧抬腿、引体向上、哑铃弯举、侧平举、肩上推举",
            "hant": "11 種：深蹲、伏地挺身、弓箭步、仰臥起坐、開合跳、臀橋、仰臥抬腿、引體向上、啞鈴彎舉、側平舉、肩上推舉",
        },
        "video": {
            "en": "Processed on the phone (Google ML Kit); never saved or uploaded",
            "zh": "在手机上识别（Google ML Kit），不保存、不上传",
            "hant": "在手機上辨識（Google ML Kit），不儲存、不上傳",
        },
        "data": {
            "en": "Collects anonymous analytics (approximate location, app activity, crash logs, device IDs); shares none",
            "zh": "收集匿名统计数据（大致位置、应用活动、崩溃日志、设备 ID），不与第三方分享",
            "hant": "收集匿名統計資料（大概位置、應用程式活動、當機記錄、裝置 ID），不與第三方分享",
        },
        "extras": {
            "en": "Adjustable angle thresholds per exercise, use without an account, daily goals and streaks, works offline",
            "zh": "每个动作的判定角度可调，不登录也能用，每日目标和连续打卡，可离线使用",
            "hant": "每個動作的判定角度可調，不登入也能用，每日目標和連續打卡，可離線使用",
        },
    },
    {
        "name": "GoodGYM: AI Rep Counter",
        "dev": "明越 王",
        "url": "https://apps.apple.com/us/app/goodgym-ai-rep-counter/id6761142874",
        "platform": {
            "en": "iPhone, iPad, Apple Watch, Mac (Apple silicon)",
            "zh": "iPhone、iPad、Apple Watch、Mac（Apple 芯片）",
            "hant": "iPhone、iPad、Apple Watch、Mac（Apple 晶片）",
        },
        "price": {
            "en": "Free, in-app purchases (GoodGYM Pro)",
            "zh": "免费，有应用内购买（GoodGYM Pro）",
            "hant": "免費，有應用程式內購買（GoodGYM Pro）",
        },
        "exercises": {
            "en": "14 including squats, sumo squats, push-ups, sit-ups, pull-ups, glute bridges and jump rope, plus plank, squat hold and dead hang timers",
            "zh": "14 种，包括深蹲、相扑深蹲、俯卧撑、仰卧起坐、引体向上、臀桥、跳绳；另有平板支撑、静蹲、悬垂计时",
            "hant": "14 種，包括深蹲、相撲深蹲、伏地挺身、仰臥起坐、引體向上、臀橋、跳繩；另有棒式、靜蹲、懸垂計時",
        },
        "video": {
            "en": "Not stated; offers Privacy Mode and face masking",
            "zh": "未注明；提供隐私模式和人脸遮挡",
            "hant": "未註明；提供隱私模式和臉部遮擋",
        },
        "data": {
            "en": "Data Not Collected (App Store privacy label)",
            "zh": "不收集数据（App Store 隐私标签）",
            "hant": "不收集資料（App Store 隱私標籤）",
        },
        "extras": {
            "en": "Custom exercises, Apple Watch, Apple Health, training plans, streak freezes",
            "zh": "自定义动作、Apple Watch、健康 App、训练计划、连续打卡补签",
            "hant": "自訂動作、Apple Watch、健康 App、訓練計畫、連續打卡補簽",
        },
    },
    {
        "name": "MyRepsCount Workout Tracker",
        "dev": "MyFitCounts",
        "url": "https://play.google.com/store/apps/details?id=com.myrepscount",
        "platform": {"en": "Android", "zh": "Android", "hant": "Android"},
        "price": {
            "en": "Free, contains ads, in-app purchases (Plus subscription removes ads)",
            "zh": "免费，含广告，有应用内购买（Plus 订阅去广告）",
            "hant": "免費，含廣告，有應用程式內購買（Plus 訂閱去廣告）",
        },
        "exercises": {
            "en": "60+, including push-ups, squats, sit-ups, burpees, lunges, pull-ups and dumbbell exercises",
            "zh": "60 种以上，包括俯卧撑、深蹲、仰卧起坐、波比跳、弓步蹲、引体向上和哑铃动作",
            "hant": "60 種以上，包括伏地挺身、深蹲、仰臥起坐、波比跳、弓箭步、引體向上和啞鈴動作",
        },
        "video": {
            "en": "Counted on the device; never recorded, stored or sent",
            "zh": "在设备上计数，不录制、不保存、不发送",
            "hant": "在裝置上計數，不錄製、不儲存、不傳送",
        },
        "data": {
            "en": "Collects location, personal info and 4 other types; shares none",
            "zh": "收集位置、个人信息等 6 类数据，不与第三方分享",
            "hant": "收集位置、個人資訊等 6 類資料，不與第三方分享",
        },
        "extras": {
            "en": "Programs and WODs, games played with your body, manual gym log, Focus Mode",
            "zh": "训练计划和 WOD、用身体玩的游戏、手动记录健身房训练、专注模式",
            "hant": "訓練計畫和 WOD、用身體玩的遊戲、手動記錄健身房訓練、專注模式",
        },
    },
    {
        "name": "Repletic - AI Rep Counter",
        "dev": "MBH LTD",
        "url": "https://play.google.com/store/apps/details?id=com.mbh.repletic",
        "platform": {"en": "Android", "zh": "Android", "hant": "Android"},
        "price": {
            "en": "Free, contains ads, in-app purchases",
            "zh": "免费，含广告，有应用内购买",
            "hant": "免費，含廣告，有應用程式內購買",
        },
        "exercises": {
            "en": "3: push-ups, squats, crunches",
            "zh": "3 种：俯卧撑、深蹲、卷腹",
            "hant": "3 種：伏地挺身、深蹲、捲腹",
        },
        "video": {
            "en": "Processed on the device (Google ML Kit); never uploaded or stored remotely",
            "zh": "在设备上识别（Google ML Kit），不上传、不在远端保存",
            "hant": "在裝置上辨識（Google ML Kit），不上傳、不在遠端儲存",
        },
        "data": {
            "en": "Collects personal info, health and fitness and 3 other types; shares device IDs",
            "zh": "收集个人信息、健康与健身等 5 类数据；与第三方分享设备 ID",
            "hant": "收集個人資訊、健康與健身等 5 類資料；與第三方分享裝置 ID",
        },
        "extras": {
            "en": "Daily challenges, anonymous sign-in with optional Google sync",
            "zh": "每日挑战，匿名登录，可绑定 Google 账号同步",
            "hant": "每日挑戰，匿名登入，可綁定 Google 帳號同步",
        },
    },
    {
        "name": "AI Rep Counter",
        "dev": "QuarkLabs",
        "url": "https://play.google.com/store/apps/details?id=com.thehealthhistory.airepcounter.free",
        "platform": {"en": "Android", "zh": "Android", "hant": "Android"},
        "price": {
            "en": "Free, contains ads (a separate paid Pro app has no ads)",
            "zh": "免费，含广告（另有付费的无广告 Pro 版）",
            "hant": "免費，含廣告（另有付費的無廣告 Pro 版）",
        },
        "exercises": {
            "en": "10+, including push-ups, squats and pull-ups",
            "zh": "10 种以上，包括俯卧撑、深蹲、引体向上",
            "hant": "10 種以上，包括伏地挺身、深蹲、引體向上",
        },
        "video": {
            "en": "All processing on the device; no personal data sent to servers",
            "zh": "全部在设备上处理，不向服务器发送个人数据",
            "hant": "全部在裝置上處理，不向伺服器傳送個人資料",
        },
        "data": {
            "en": "No data collected; shares none",
            "zh": "不收集数据，不与第三方分享",
            "hant": "不收集資料，不與第三方分享",
        },
        "extras": {
            "en": "Custom exercises, form feedback, daily goals, progress charts",
            "zh": "自定义动作、动作反馈、每日目标、进度图表",
            "hant": "自訂動作、動作回饋、每日目標、進度圖表",
        },
    },
    {
        "name": "REP AI: Workout Rep Counter",
        "dev": "DeveloperThings",
        "url": "https://play.google.com/store/apps/details?id=app.posedetector",
        "platform": {"en": "Android", "zh": "Android", "hant": "Android"},
        "price": {
            "en": "Free, contains ads, in-app purchases",
            "zh": "免费，含广告，有应用内购买",
            "hant": "免費，含廣告，有應用程式內購買",
        },
        "exercises": {
            "en": "6: bicep curl, barbell curl, squat, push-up, shoulder press, plank",
            "zh": "6 种：哑铃弯举、杠铃弯举、深蹲、俯卧撑、肩上推举、平板支撑",
            "hant": "6 種：啞鈴彎舉、槓鈴彎舉、深蹲、伏地挺身、肩上推舉、棒式",
        },
        "video": {
            "en": "Processed locally on the device",
            "zh": "在设备本地处理",
            "hant": "在裝置本機處理",
        },
        "data": {
            "en": "No data collected; shares device IDs",
            "zh": "不收集数据；与第三方分享设备 ID",
            "hant": "不收集資料；與第三方分享裝置 ID",
        },
        "extras": {
            "en": "Form detection, movement speed tracking",
            "zh": "动作错误提示、动作速度统计",
            "hant": "動作錯誤提示、動作速度統計",
        },
    },
]
