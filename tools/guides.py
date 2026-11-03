"""指南页正文（三种语言）。

body 里的占位符由 build.py 填：{p} 是当前语言的网址前缀（英文为空、简中 /zh、繁中 /zh-hant），
{table}、{postures} 只在手机摆放指南里用，按 content.EXERCISES 自动生成；
{plan} 是 30 天深蹲表，{beginner} 是新手计划表（数据在下面的 BEGINNER_PLAN）；{compare}、{checked}、{e} 用在对比页（数据在 compare.py）。
"""

GUIDES = [
    {
        "slug": "phone-placement",
        "title": {
            "en": "Where to Put Your Phone for Rep Counting – Setup for Every Exercise",
            "zh": "数次数时手机怎么摆：每种动作的摆放方法",
            "hant": "計算次數時手機怎麼擺：每種動作的擺放方法",
        },
        "h1": {"en": "Where to put your phone", "zh": "手机怎么摆", "hant": "手機怎麼擺"},
        "card": {
            "en": "Phone setup for all 11 exercises, plus lighting tips.",
            "zh": "11 种动作的手机摆放方法和光线建议。",
            "hant": "11 種動作的手機擺放方法和光線建議。",
        },
        "desc": {
            "en": "Where to place your phone so KINETIC counts every rep: distance, height and angle for squats, push-ups, sit-ups, pull-ups and 7 more exercises.",
            "zh": "手机怎么摆，KINETIC 才能数准：深蹲、俯卧撑、仰卧起坐、引体向上等 11 种动作的距离、高度和角度。",
            "hant": "手機怎麼擺，KINETIC 才能數準：深蹲、伏地挺身、仰臥起坐、引體向上等 11 種動作的距離、高度和角度。",
        },
        "answer": {
            "en": "Keep your whole body in frame with good light. Stand the phone upright 2–3 m away for standing exercises; for floor exercises like push-ups and sit-ups, put it on the floor beside you so it sees you from the side.",
            "zh": "全身入镜、光线充足。站立的动作把手机竖立在 2–3 米外；俯卧撑、仰卧起坐这类地面动作，把手机放在身体侧面的地上，从侧面拍。",
            "hant": "全身入鏡、光線充足。站立的動作把手機直立在 2–3 公尺外；伏地挺身、仰臥起坐這類地面動作，把手機放在身體側面的地上，從側面拍。",
        },
        "body": {
            "en": """
<h2>Rules for every exercise</h2>
<ul>
<li><b>Whole body in frame.</b> KINETIC measures joint angles, so the joints it uses must stay visible for the whole rep. Most miscounts come from a hand, foot or head leaving the frame.</li>
<li><b>Good, even light.</b> Turn on a light and don't stand with a bright window behind you.</li>
<li><b>One person in frame.</b> If someone walks behind you, the app may track them instead.</li>
<li><b>A steady phone.</b> Lean it against a wall, a water bottle or a stand. If the phone moves, the angles jump.</li>
<li><b>Fitted clothes help.</b> Very loose clothing can hide where your knees and elbows are.</li>
</ul>
<h2>Exercise by exercise</h2>
{table}
{postures}
<h2>Still not counting?</h2>
<p>Watch the hint on the tracking screen: it tells you whether you're out of frame, facing the wrong way or not going deep enough. If your form is fine but reps are missed, open the angle panel and loosen the threshold a little.</p>
""",
            "zh": """
<h2>所有动作通用</h2>
<ul>
<li><b>全身入镜。</b>KINETIC 按关节角度计数，用到的关节在整个动作过程中都要拍得到。大多数计数不准，是因为手、脚或头出了画面。</li>
<li><b>光线充足均匀。</b>开灯，不要背对明亮的窗户。</li>
<li><b>画面里只有一个人。</b>有人从你身后走过时，App 可能会去识别那个人。</li>
<li><b>手机放稳。</b>靠在墙上、水瓶上或支架上。手机一晃，角度就会跳。</li>
<li><b>衣服别太宽松。</b>太宽松的衣服会挡住膝盖和手肘的位置。</li>
</ul>
<h2>每种动作怎么摆</h2>
{table}
{postures}
<h2>还是不计数？</h2>
<p>看识别页上的提示：它会告诉你是出了画面、方向不对，还是动作幅度不够。动作没问题却还是漏数，就打开角度面板，把阈值放宽一点。</p>
""",
            "hant": """
<h2>所有動作通用</h2>
<ul>
<li><b>全身入鏡。</b>KINETIC 依關節角度計數，用到的關節在整個動作過程中都要拍得到。大多數計數不準，是因為手、腳或頭超出畫面。</li>
<li><b>光線充足均勻。</b>開燈，不要背對明亮的窗戶。</li>
<li><b>畫面裡只有一個人。</b>有人從你身後走過時，App 可能會去辨識那個人。</li>
<li><b>手機放穩。</b>靠在牆上、水瓶上或支架上。手機一晃，角度就會跳。</li>
<li><b>衣服別太寬鬆。</b>太寬鬆的衣服會擋住膝蓋和手肘的位置。</li>
</ul>
<h2>每種動作怎麼擺</h2>
{table}
{postures}
<h2>還是不計數？</h2>
<p>看辨識頁上的提示：它會告訴你是超出畫面、方向不對，還是動作幅度不夠。動作沒問題卻還是漏數，就打開角度面板，把門檻放寬一點。</p>
""",
        },
    },
    {
        "slug": "on-device-pose-detection",
        "title": {
            "en": "Rep Counting Without Uploading Video – How On-device Pose Detection Works",
            "zh": "不上传画面也能计数：本机姿态识别是怎么工作的",
            "hant": "不上傳畫面也能計數：本機姿勢辨識是怎麼運作的",
        },
        "h1": {"en": "How on-device pose detection works", "zh": "本机姿态识别是怎么工作的", "hant": "本機姿勢辨識是怎麼運作的"},
        "card": {
            "en": "What happens to each camera frame, and what (little) leaves your phone.",
            "zh": "每一帧画面经历了什么，哪些数据会离开手机。",
            "hant": "每一幀畫面經歷了什麼，哪些資料會離開手機。",
        },
        "desc": {
            "en": "KINETIC counts reps without uploading video. Here is what happens to each camera frame on your phone, and exactly what data leaves the device.",
            "zh": "KINETIC 不上传画面也能计数。这里说明每一帧画面在手机上怎么处理，以及哪些数据会离开手机。",
            "hant": "KINETIC 不上傳畫面也能計數。這裡說明每一幀畫面在手機上怎麼處理，以及哪些資料會離開手機。",
        },
        "answer": {
            "en": "Each camera frame is analysed on your phone by Google ML Kit, turned into body landmark positions and then discarded. KINETIC counts reps from joint angles calculated from those landmarks. No video is recorded or uploaded, and workout records stay on the phone.",
            "zh": "每一帧画面都由 Google ML Kit 在手机上分析，转换成身体关键点的位置后立即丢弃。KINETIC 用这些关键点算出关节角度来计数。不录像、不上传，训练记录也只留在手机上。",
            "hant": "每一幀畫面都由 Google ML Kit 在手機上分析，轉換成身體關鍵點的位置後立即丟棄。KINETIC 用這些關鍵點算出關節角度來計數。不錄影、不上傳，訓練紀錄也只留在手機上。",
        },
        "body": {
            "en": """
<h2>What happens to each frame</h2>
<ol>
<li><b>The camera captures a frame.</b> Frames that arrive while the phone is still busy are skipped rather than queued, so counting never lags behind you.</li>
<li><b>ML Kit finds your body.</b> Google ML Kit's pose detection model, which ships inside the app, locates 33 body landmarks such as shoulders, elbows, hips, knees and ankles.</li>
<li><b>The frame is discarded.</b> Only the landmark positions are kept, as numbers. The picture itself is never written to storage.</li>
<li><b>Joint angles are calculated.</b> For a squat, KINETIC measures the angle at your knee between thigh and shin. Positions are smoothed to reduce jitter.</li>
<li><b>A rep is counted.</b> When the angle passes the completion threshold and comes back to the start position, the counter goes up by one.</li>
</ol>
<h2>What leaves your phone</h2>
<div class="tbl-wrap"><table class="tbl">
<tr><th>Data</th><th>Leaves the phone?</th></tr>
<tr><td>Camera video and images</td><td>Never</td></tr>
<tr><td>Workout records</td><td>Never. Stored on this phone only, per account</td></tr>
<tr><td>Google account name, email, photo</td><td>Never sent to our servers. Stored on this phone after you sign in</td></tr>
<tr><td>Anonymous usage stats and crash reports (Google Firebase)</td><td>Yes, unless you turn them off in Settings. No video, account or email</td></tr>
<tr><td>ML Kit anonymous usage stats (model version, run time)</td><td>Yes, sent to Google by ML Kit. Never images</td></tr>
</table></div>
<p>Because detection runs on the phone, counting also works without an internet connection.</p>
<p>The full details are in the <a href="{p}/privacy.html">privacy policy</a>.</p>
""",
            "zh": """
<h2>每一帧画面经历了什么</h2>
<ol>
<li><b>摄像头拍下一帧。</b>手机还在处理上一帧时送来的画面直接跳过、不排队，所以计数不会落后于你的动作。</li>
<li><b>ML Kit 找到你的身体。</b>Google ML Kit 的姿态识别模型内置在 App 里，会找出肩、肘、髋、膝、踝等 33 个身体关键点。</li>
<li><b>画面被丢弃。</b>只留下关键点的位置（一串数字），画面本身从不写入存储。</li>
<li><b>计算关节角度。</b>比如深蹲，KINETIC 测量膝盖处大腿和小腿的夹角。位置会做平滑处理，减少抖动。</li>
<li><b>计数。</b>角度越过完成阈值、再回到起始姿势，计数 +1。</li>
</ol>
<h2>哪些数据会离开手机</h2>
<div class="tbl-wrap"><table class="tbl">
<tr><th>数据</th><th>会离开手机吗</th></tr>
<tr><td>摄像头画面和图片</td><td>永不</td></tr>
<tr><td>训练记录</td><td>永不。按账号只保存在这台手机上</td></tr>
<tr><td>Google 账号的昵称、邮箱、头像</td><td>不会发到我们的服务器。登录后保存在这台手机上</td></tr>
<tr><td>匿名使用统计和崩溃报告（Google Firebase）</td><td>会，除非在设置里关闭。不含画面、账号或邮箱</td></tr>
<tr><td>ML Kit 匿名使用统计（模型版本、运行时间）</td><td>会，由 ML Kit 发给 Google。从不包含画面</td></tr>
</table></div>
<p>识别在手机上完成，所以没有网络也能计数。</p>
<p>完整说明见<a href="{p}/privacy.html">隐私政策</a>。</p>
""",
            "hant": """
<h2>每一幀畫面經歷了什麼</h2>
<ol>
<li><b>相機拍下一幀。</b>手機還在處理上一幀時送來的畫面直接略過、不排隊，所以計數不會落後於你的動作。</li>
<li><b>ML Kit 找到你的身體。</b>Google ML Kit 的姿勢辨識模型內建在 App 裡，會找出肩、肘、髖、膝、踝等 33 個身體關鍵點。</li>
<li><b>畫面被丟棄。</b>只留下關鍵點的位置（一串數字），畫面本身從不寫入儲存空間。</li>
<li><b>計算關節角度。</b>例如深蹲，KINETIC 測量膝蓋處大腿和小腿的夾角。位置會做平滑處理，減少抖動。</li>
<li><b>計數。</b>角度越過完成門檻、再回到起始姿勢，計數 +1。</li>
</ol>
<h2>哪些資料會離開手機</h2>
<div class="tbl-wrap"><table class="tbl">
<tr><th>資料</th><th>會離開手機嗎</th></tr>
<tr><td>相機畫面和圖片</td><td>永不</td></tr>
<tr><td>訓練紀錄</td><td>永不。依帳號只儲存在這支手機上</td></tr>
<tr><td>Google 帳號的暱稱、電子郵件、頭像</td><td>不會傳到我們的伺服器。登入後儲存在這支手機上</td></tr>
<tr><td>匿名使用統計和當機報告（Google Firebase）</td><td>會，除非在設定中關閉。不含畫面、帳號或電子郵件</td></tr>
<tr><td>ML Kit 匿名使用統計（模型版本、執行時間）</td><td>會，由 ML Kit 傳給 Google。從不包含畫面</td></tr>
</table></div>
<p>辨識在手機上完成，所以沒有網路也能計數。</p>
<p>完整說明請見<a href="{p}/privacy.html">隱私權政策</a>。</p>
""",
        },
    },
    {
        "slug": "100-push-ups-a-day",
        "title": {
            "en": "100 Push-ups a Day Challenge – How to Build Up and Track It",
            "zh": "每天 100 个俯卧撑挑战：怎么循序渐进、怎么记录",
            "hant": "每天 100 下伏地挺身挑戰：怎麼循序漸進、怎麼記錄",
        },
        "h1": {"en": "100 push-ups a day", "zh": "每天 100 个俯卧撑", "hant": "每天 100 下伏地挺身"},
        "card": {
            "en": "Split it into sets, build up week by week, track it automatically.",
            "zh": "拆成几组，按周加量，自动记录。",
            "hant": "拆成幾組，按週加量，自動記錄。",
        },
        "desc": {
            "en": "How to do 100 push-ups a day: split them into sets, build up week by week if you can't yet, and let your phone camera count and log every rep.",
            "zh": "每天 100 个俯卧撑怎么做：拆成几组完成，做不到就按周加量，用手机摄像头自动计数和记录。",
            "hant": "每天 100 下伏地挺身怎麼做：拆成幾組完成，做不到就按週加量，用手機相機自動計數和記錄。",
        },
        "answer": {
            "en": "You don't need to do 100 in a row. Split them into sets you can finish with good form, such as 5 sets of 20 or 10 sets of 10 across the day. If that's too many for now, start with a smaller daily total and add about 10 a week.",
            "zh": "不用一口气做完 100 个。拆成能保持标准动作的几组，比如 5 组 × 20 个，或者一天里分 10 组、每组 10 个。现在做不到 100，就从较小的每日总数开始，每周加 10 个左右。",
            "hant": "不用一口氣做完 100 下。拆成能保持標準動作的幾組，例如 5 組 × 20 下，或者一天裡分 10 組、每組 10 下。現在做不到 100，就從較小的每日總數開始，每週加 10 下左右。",
        },
        "body": {
            "en": """
<h2>Find your starting point</h2>
<p>Do as many push-ups as you can with good form and note the number. A rep counts when your elbows bend to about 90°; that is also <a href="{p}/exercises/push-up-counter/">KINETIC's default</a>, so the app's count is an honest test.</p>
<div class="tbl-wrap"><table class="tbl">
<tr><th>Max in one set</th><th>Start with a daily total of</th><th>Sets</th></tr>
<tr><td>Under 10</td><td>30</td><td>6 × 5, spread across the day</td></tr>
<tr><td>10–19</td><td>50</td><td>5 × 10</td></tr>
<tr><td>20–29</td><td>70</td><td>5 × 14</td></tr>
<tr><td>30 or more</td><td>100</td><td>5 × 20</td></tr>
</table></div>
<p>Add about 10 to the daily total each week until you reach 100. If your form slips, keep the total the same for another week.</p>
<h2>Rules that keep it sustainable</h2>
<ul>
<li>Quality first: full range, straight body. Ten good reps beat twenty half reps.</li>
<li>Rest between sets as long as you need. The goal is the daily total, not speed.</li>
<li>Take a day off when your shoulders, elbows or wrists ache. A streak isn't worth an injury.</li>
<li>Easier variations, like hands on a bench or knees on the floor, are fine while you build up.</li>
</ul>
<h2>Track it with KINETIC</h2>
<ol>
<li>Set your daily goal for push-ups to your current total (100 when you get there).</li>
<li>Put the phone on the floor beside you and do each set. Every rep that reaches 90° is counted and added to today's total.</li>
<li>When you hit the goal, the day is checked in on your calendar and your streak grows.</li>
</ol>
""",
            "zh": """
<h2>先测出起点</h2>
<p>用标准动作一口气能做多少个，记下来。手肘弯到约 90° 才算一个，这也是 <a href="{p}/exercises/push-up-counter/">KINETIC 的默认值</a>，所以用 App 测出来的数是实打实的。</p>
<div class="tbl-wrap"><table class="tbl">
<tr><th>一组最多能做</th><th>每日总数从多少开始</th><th>分组</th></tr>
<tr><td>不到 10 个</td><td>30</td><td>6 组 × 5 个，分散在一天里</td></tr>
<tr><td>10–19 个</td><td>50</td><td>5 组 × 10 个</td></tr>
<tr><td>20–29 个</td><td>70</td><td>5 组 × 14 个</td></tr>
<tr><td>30 个以上</td><td>100</td><td>5 组 × 20 个</td></tr>
</table></div>
<p>每周把每日总数加 10 个左右，直到 100。动作开始变形，就把总数再保持一周。</p>
<h2>能坚持下去的几条规矩</h2>
<ul>
<li>质量第一：做满幅度、身体保持直线。10 个标准的胜过 20 个做一半的。</li>
<li>组间想休息多久就休息多久，目标是每日总数，不是速度。</li>
<li>肩、肘、手腕疼的时候就休息一天。连续打卡不值得拿受伤换。</li>
<li>还在打基础时，可以用更容易的变式，比如手撑在长凳上，或者跪姿。</li>
</ul>
<h2>用 KINETIC 记录</h2>
<ol>
<li>把俯卧撑的每日目标设成现在的总数（做到了就设成 100）。</li>
<li>把手机放在身体侧面的地上，一组一组做。每个压到 90° 的动作都会被计数，并累计到今日总数。</li>
<li>完成目标后，日历上自动打卡，连续天数 +1。</li>
</ol>
""",
            "hant": """
<h2>先測出起點</h2>
<p>用標準動作一口氣能做幾下，記下來。手肘彎到約 90° 才算一下，這也是 <a href="{p}/exercises/push-up-counter/">KINETIC 的預設值</a>，所以用 App 測出來的數字是實打實的。</p>
<div class="tbl-wrap"><table class="tbl">
<tr><th>一組最多能做</th><th>每日總數從多少開始</th><th>分組</th></tr>
<tr><td>不到 10 下</td><td>30</td><td>6 組 × 5 下，分散在一天裡</td></tr>
<tr><td>10–19 下</td><td>50</td><td>5 組 × 10 下</td></tr>
<tr><td>20–29 下</td><td>70</td><td>5 組 × 14 下</td></tr>
<tr><td>30 下以上</td><td>100</td><td>5 組 × 20 下</td></tr>
</table></div>
<p>每週把每日總數加 10 下左右，直到 100。動作開始變形，就把總數再維持一週。</p>
<h2>能堅持下去的幾條規矩</h2>
<ul>
<li>品質第一：做滿幅度、身體保持直線。10 下標準的勝過 20 下做一半的。</li>
<li>組間想休息多久就休息多久，目標是每日總數，不是速度。</li>
<li>肩、肘、手腕痛的時候就休息一天。連續打卡不值得拿受傷換。</li>
<li>還在打基礎時，可以用更容易的變化式，例如手撐在長凳上，或者跪姿。</li>
</ul>
<h2>用 KINETIC 記錄</h2>
<ol>
<li>把伏地挺身的每日目標設成現在的總數（做到了就設成 100）。</li>
<li>把手機放在身體側面的地上，一組一組做。每個壓到 90° 的動作都會被計數，並累計到今日總數。</li>
<li>完成目標後，日曆上自動打卡，連續天數 +1。</li>
</ol>
""",
        },
    },
    {
        "slug": "30-day-squat-challenge",
        "title": {
            "en": "30-Day Squat Challenge – Day-by-day Plan with Rest Days",
            "zh": "30 天深蹲挑战：每天做多少、哪天休息",
            "hant": "30 天深蹲挑戰：每天做多少、哪天休息",
        },
        "h1": {"en": "30-day squat challenge", "zh": "30 天深蹲挑战", "hant": "30 天深蹲挑戰"},
        "card": {
            "en": "A day-by-day plan from 20 to 130 squats, with a rest day every fourth day.",
            "zh": "从 20 个到 130 个的逐日计划，每 4 天休息一天。",
            "hant": "從 20 下到 130 下的逐日計畫，每 4 天休息一天。",
        },
        "desc": {
            "en": "A 30-day squat challenge for beginners: 20 squats on day 1, 130 on day 30, a rest day every fourth day, and automatic counting with your phone camera.",
            "zh": "适合新手的 30 天深蹲挑战：第 1 天 20 个、第 30 天 130 个，每 4 天休息一天，用手机摄像头自动计数。",
            "hant": "適合新手的 30 天深蹲挑戰：第 1 天 20 下、第 30 天 130 下，每 4 天休息一天，用手機相機自動計數。",
        },
        "answer": {
            "en": "Start with 20 squats on day 1, add 5 each training day and rest every fourth day. You finish with 130 squats on day 30. Split each day into sets of 10–20 and go down until your thighs are about parallel to the floor.",
            "zh": "第 1 天 20 个，之后每个训练日加 5 个，每 4 天休息一天，第 30 天做到 130 个。每天的量分成每组 10–20 个，蹲到大腿大约与地面平行。",
            "hant": "第 1 天 20 下，之後每個訓練日加 5 下，每 4 天休息一天，第 30 天做到 130 下。每天的量分成每組 10–20 下，蹲到大腿大約與地面平行。",
        },
        "body": {
            "en": """
<h2>The plan</h2>
{plan}
<h2>How to do each squat</h2>
<p>Feet shoulder-width apart, sit your hips back, chest up, heels down. Go down until your thighs are about parallel to the floor and stand all the way up. KINETIC counts a rep at a knee angle of 110° or less (the default when you face the camera) and waits for you to stand back up past 160°. <a href="{p}/exercises/squat-counter/">More on how squats are counted</a>.</p>
<h2>Tips</h2>
<ul>
<li>Split each day into sets of 10–20 with a short rest in between.</li>
<li>Rest days matter. Muscles get stronger while you recover.</li>
<li>Missed a day? Pick up where you left off instead of doubling up.</li>
<li>Knee pain is a signal to stop and check your form, not to push through.</li>
</ul>
<h2>Track it with KINETIC</h2>
<p>Set your squat daily goal to the day's number, stand the phone upright 2–3 m in front of you, and squat. Every counted rep adds to today's total, and hitting the goal checks the day in on your calendar.</p>
""",
            "zh": """
<h2>计划表</h2>
{plan}
<h2>每个深蹲怎么做</h2>
<p>双脚与肩同宽，臀部向后坐，挺胸，脚跟不离地。蹲到大腿大约与地面平行，再完全站直。KINETIC 在膝角到 110° 或更小时计数（正对镜头时的默认值），站回 160° 以上才开始下一次。<a href="{p}/exercises/squat-counter/">深蹲怎么计数</a>。</p>
<h2>几点建议</h2>
<ul>
<li>每天的量分成每组 10–20 个，组间稍作休息。</li>
<li>休息日很重要，肌肉是在恢复的时候变强的。</li>
<li>漏了一天？接着做，不要把两天的量加在一起补。</li>
<li>膝盖疼是让你停下来检查动作，不是让你硬撑。</li>
</ul>
<h2>用 KINETIC 记录</h2>
<p>把深蹲的每日目标设成当天的数字，手机竖立在你前方 2–3 米，开始蹲。每次计数都会累计到今日总数，完成目标后日历自动打卡。</p>
""",
            "hant": """
<h2>計畫表</h2>
{plan}
<h2>每個深蹲怎麼做</h2>
<p>雙腳與肩同寬，臀部向後坐，挺胸，腳跟不離地。蹲到大腿大約與地面平行，再完全站直。KINETIC 在膝角到 110° 或更小時計數（正對鏡頭時的預設值），站回 160° 以上才開始下一次。<a href="{p}/exercises/squat-counter/">深蹲怎麼計數</a>。</p>
<h2>幾點建議</h2>
<ul>
<li>每天的量分成每組 10–20 下，組間稍作休息。</li>
<li>休息日很重要，肌肉是在恢復的時候變強的。</li>
<li>漏了一天？接著做，不要把兩天的量加在一起補。</li>
<li>膝蓋痛是要你停下來檢查動作，不是要你硬撐。</li>
</ul>
<h2>用 KINETIC 記錄</h2>
<p>把深蹲的每日目標設成當天的數字，手機直立在你前方 2–3 公尺，開始蹲。每次計數都會累計到今日總數，完成目標後日曆自動打卡。</p>
""",
        },
    },
    {
        "slug": "beginner-bodyweight-plan",
        "title": {
            "en": "Beginner Bodyweight Workout Plan – 4 Weeks, 3 Days a Week, No Equipment",
            "zh": "新手自重训练计划：4 周、每周 3 练、不用器械",
            "hant": "新手自體重訓練計畫：4 週、每週 3 練、不用器材",
        },
        "h1": {"en": "Beginner bodyweight plan", "zh": "新手自重训练计划", "hant": "新手自體重訓練計畫"},
        "card": {
            "en": "4 weeks, 3 short sessions a week, five exercises, no equipment.",
            "zh": "4 周，每周 3 次、每次 20 分钟左右，5 个动作，不用器械。",
            "hant": "4 週，每週 3 次、每次 20 分鐘左右，5 個動作，不用器材。",
        },
        "desc": {
            "en": "A 4-week bodyweight plan for complete beginners: 3 sessions a week of squats, glute bridges, push-ups, jumping jacks and lunges, with sets and reps for every week and automatic counting with your phone camera.",
            "zh": "给完全新手的 4 周自重训练计划：每周 3 次，深蹲、臀桥、俯卧撑、开合跳、弓步蹲，每周的组数和次数都列好了，用手机摄像头自动计数。",
            "hant": "給完全新手的 4 週自體重訓練計畫：每週 3 次，深蹲、臀橋、伏地挺身、開合跳、弓箭步，每週的組數和次數都列好了，用手機相機自動計數。",
        },
        "answer": {
            "en": "Train 3 days a week with a rest day in between, for example Monday, Wednesday and Friday. In week 1 do 2 sets each of 15 jumping jacks, 8 squats, 5 push-ups (on your knees is fine) and 10 glute bridges. Add a set or a few reps each week, and add lunges from week 3. Each session takes about 20 minutes.",
            "zh": "每周练 3 天，中间隔一天休息，比如周一、周三、周五。第 1 周每个动作做 2 组：开合跳 15 个、深蹲 8 个、俯卧撑 5 个（跪姿也行）、臀桥 10 个。之后每周加一组或加几个，第 3 周加入弓步蹲。每次大约 20 分钟。",
            "hant": "每週練 3 天，中間隔一天休息，例如週一、週三、週五。第 1 週每個動作做 2 組：開合跳 15 下、深蹲 8 下、伏地挺身 5 下（跪姿也可以）、臀橋 10 下。之後每週加一組或加幾下，第 3 週加入弓箭步。每次大約 20 分鐘。",
        },
        "body": {
            "en": """
<h2>The plan</h2>
<p>Each cell is sets × reps. The number below it is the total for that session, which is what you set as the daily goal in KINETIC.</p>
{beginner}
<h2>One session, step by step</h2>
<ol>
<li><b>Warm up for 3 minutes:</b> march in place, roll your shoulders, swing your arms.</li>
<li><b>Standing exercises first.</b> Stand the phone upright 2–3 m away, facing you, and do the jumping jacks and squats. For lunges, turn sideways to the phone.</li>
<li><b>Then the floor exercises.</b> Move the phone to the floor beside you and do the push-ups and glute bridges.</li>
<li><b>Rest 60–90 seconds between sets.</b> Take longer if you need to; the goal is good reps, not speed.</li>
<li><b>Cool down:</b> walk around for a minute and stretch your legs, hips and chest.</li>
</ol>
<h2>If push-ups are too hard</h2>
<p>Do them on your knees, keeping a straight line from shoulders to knees. KINETIC still counts a rep when your elbows bend to about 90°, as long as your body stays close to horizontal. Push-ups against a wall or a high bench won't be counted. <a href="{p}/exercises/push-up-counter/">How push-ups are counted</a>.</p>
<h2>How to move on</h2>
<ul>
<li>Finished every set with good form? Go to the next week.</li>
<li>Couldn't finish, or your form fell apart in the last reps? Repeat the week. Taking 6 weeks instead of 4 is fine.</li>
<li>Mild muscle soreness for a day or two is normal in the first weeks. Sharp pain or joint pain is not: stop and rest.</li>
<li>Missed a session? Just do the next one. Don't squeeze two into one day.</li>
<li>If you have a health condition or an injury, or haven't exercised in a long time, check with a doctor first.</li>
</ul>
<h2>After week 4</h2>
<p>Keep going with week 4 and add reps, or pick a challenge: the <a href="{p}/guides/30-day-squat-challenge/">30-day squat challenge</a> or <a href="{p}/guides/100-push-ups-a-day/">100 push-ups a day</a>.</p>
<h2>Track it with KINETIC</h2>
<p>At the start of each week, set the daily goal for each exercise to the total in the table (for week 1: 30 jumping jacks, 16 squats, 10 push-ups, 20 glute bridges). Every counted rep adds to today's total, and hitting a goal checks the day in on your calendar. See <a href="{p}/guides/phone-placement/">where to put your phone</a> for each exercise.</p>
""",
            "zh": """
<h2>计划表</h2>
<p>每格是「组数 × 每组次数」，下面的数字是这一次训练的总数，也就是在 KINETIC 里要设的每日目标。</p>
{beginner}
<h2>一次训练怎么做</h2>
<ol>
<li><b>热身 3 分钟：</b>原地踏步、绕肩、摆臂。</li>
<li><b>先做站立的动作。</b>手机竖立在前方 2–3 米，正对你，做开合跳和深蹲。弓步蹲时侧对手机。</li>
<li><b>再做地面的动作。</b>把手机放到身体侧面的地上，做俯卧撑和臀桥。</li>
<li><b>组间休息 60–90 秒。</b>需要就多歇一会儿，要的是动作标准，不是快。</li>
<li><b>放松：</b>走动一分钟，拉伸腿、髋和胸。</li>
</ol>
<h2>俯卧撑做不起来怎么办</h2>
<p>改成跪姿俯卧撑，肩膀到膝盖保持一条直线。只要身体接近水平，手肘弯到约 90° KINETIC 照样计数。扶墙或撑在高凳上的俯卧撑不会被计数。<a href="{p}/exercises/push-up-counter/">俯卧撑怎么计数</a>。</p>
<h2>怎么进阶</h2>
<ul>
<li>每组都用标准动作做完了？进入下一周。</li>
<li>没做完，或者最后几个动作变形了？这一周再练一遍。用 6 周练完也没关系。</li>
<li>头几周肌肉酸一两天是正常的。刺痛或关节痛不正常，要停下来休息。</li>
<li>漏了一次？接着做下一次，不要一天练两次补。</li>
<li>有慢性病、伤病，或者很久没运动了，先问问医生。</li>
</ul>
<h2>4 周以后</h2>
<p>可以继续按第 4 周练并慢慢加次数，或者挑一个挑战：<a href="{p}/guides/30-day-squat-challenge/">30 天深蹲挑战</a>、<a href="{p}/guides/100-push-ups-a-day/">每天 100 个俯卧撑</a>。</p>
<h2>用 KINETIC 记录</h2>
<p>每周开始时，把每个动作的每日目标设成表里的总数（第 1 周：开合跳 30、深蹲 16、俯卧撑 10、臀桥 20）。每次计数都会累计到今日总数，完成目标后日历自动打卡。每个动作手机怎么摆见<a href="{p}/guides/phone-placement/">手机怎么摆</a>。</p>
""",
            "hant": """
<h2>計畫表</h2>
<p>每格是「組數 × 每組次數」，下面的數字是這一次訓練的總數，也就是在 KINETIC 裡要設的每日目標。</p>
{beginner}
<h2>一次訓練怎麼做</h2>
<ol>
<li><b>熱身 3 分鐘：</b>原地踏步、繞肩、擺臂。</li>
<li><b>先做站立的動作。</b>手機直立在前方 2–3 公尺，正對你，做開合跳和深蹲。弓箭步時側對手機。</li>
<li><b>再做地面的動作。</b>把手機放到身體側面的地上，做伏地挺身和臀橋。</li>
<li><b>組間休息 60–90 秒。</b>需要就多休息一下，要的是動作標準，不是快。</li>
<li><b>放鬆：</b>走動一分鐘，伸展腿、髖和胸。</li>
</ol>
<h2>伏地挺身做不起來怎麼辦</h2>
<p>改成跪姿伏地挺身，肩膀到膝蓋保持一直線。只要身體接近水平，手肘彎到約 90° KINETIC 照樣計數。扶牆或撐在高凳上的伏地挺身不會被計數。<a href="{p}/exercises/push-up-counter/">伏地挺身怎麼計數</a>。</p>
<h2>怎麼進階</h2>
<ul>
<li>每組都用標準動作做完了？進入下一週。</li>
<li>沒做完，或者最後幾下動作變形了？這一週再練一遍。用 6 週練完也沒關係。</li>
<li>頭幾週肌肉痠一兩天是正常的。刺痛或關節痛不正常，要停下來休息。</li>
<li>漏了一次？接著做下一次，不要一天練兩次補。</li>
<li>有慢性病、傷病，或者很久沒運動了，先問問醫師。</li>
</ul>
<h2>4 週以後</h2>
<p>可以繼續按第 4 週練並慢慢加次數，或者挑一個挑戰：<a href="{p}/guides/30-day-squat-challenge/">30 天深蹲挑戰</a>、<a href="{p}/guides/100-push-ups-a-day/">每天 100 下伏地挺身</a>。</p>
<h2>用 KINETIC 記錄</h2>
<p>每週開始時，把每個動作的每日目標設成表裡的總數（第 1 週：開合跳 30、深蹲 16、伏地挺身 10、臀橋 20）。每次計數都會累計到今日總數，完成目標後日曆自動打卡。每個動作手機怎麼擺見<a href="{p}/guides/phone-placement/">手機怎麼擺</a>。</p>
""",
        },
    },
    {
        "slug": "rep-counter-apps-compared",
        "title": {
            "en": "Rep Counter Apps Compared (2026): KINETIC, GoodGYM, MyRepsCount and More",
            "zh": "AI 运动计数 App 对比（2026）：KINETIC、GoodGYM、MyRepsCount 等 6 款",
            "hant": "AI 運動計數 App 比較（2026）：KINETIC、GoodGYM、MyRepsCount 等 6 款",
        },
        "h1": {"en": "Rep counter apps compared", "zh": "运动计数 App 对比", "hant": "運動計數 App 比較"},
        "card": {
            "en": "Six camera rep counters side by side: platform, price, exercises and privacy.",
            "zh": "6 款摄像头计数 App 的平台、价格、动作数和隐私对比。",
            "hant": "6 款相機計數 App 的平台、價格、動作數和隱私比較。",
        },
        "desc": {
            "en": "Six apps that count reps with your phone camera, compared from their store pages: platform, price, ads, number of exercises, how camera video is handled and what data they declare.",
            "zh": "6 款用手机摄像头自动计数的 App，按商店页信息对比：平台、价格、广告、能数的动作、画面怎么处理、声明收集哪些数据。",
            "hant": "6 款用手機相機自動計數的 App，依商店頁資訊比較：平台、價格、廣告、能數的動作、畫面怎麼處理、聲明收集哪些資料。",
        },
        "answer": {
            "en": "On iPhone, GoodGYM is the closest match. On Android, MyRepsCount counts the most exercises (60+) but has ads; KINETIC counts 11 exercises with no ads, no in-app purchases and no account required, and lets you adjust the angle each rep must reach.",
            "zh": "用 iPhone 选 GoodGYM。用 Android：要动作最多选 MyRepsCount（60 种以上，有广告）；KINETIC 能数 11 种动作，没有广告、没有应用内购买、不登录也能用，而且每个动作的判定角度可以自己调。",
            "hant": "用 iPhone 選 GoodGYM。用 Android：要動作最多選 MyRepsCount（60 種以上，有廣告）；KINETIC 能數 11 種動作，沒有廣告、沒有應用程式內購買、不登入也能用，而且每個動作的判定角度可以自己調。",
        },
        "body": {
            "en": """
<h2>At a glance</h2>
<p>Everything below comes from each app's US store page, checked on {checked}. Scroll the table sideways on a phone.</p>
{compare}
<h2>Which one fits you</h2>
<ul>
<li><b>You use an iPhone:</b> GoodGYM. KINETIC doesn't have an iOS version yet.</li>
<li><b>You want the most exercises, programs or gym logging:</b> MyRepsCount.</li>
<li><b>You want form and tempo feedback for curls and presses:</b> REP AI.</li>
<li><b>You want daily push-up, squat and crunch challenges:</b> Repletic.</li>
<li><b>You want an app with no ads, no purchases and no sign-up, and you want to set how deep each rep must go:</b> KINETIC.</li>
</ul>
<h2>Where KINETIC falls short</h2>
<ul>
<li>Android only for now.</li>
<li>11 exercises and no custom exercises. MyRepsCount and GoodGYM count more.</li>
<li>It checks range of motion (the joint angle), not form errors or tempo.</li>
<li>No training programs, games or smartwatch support.</li>
</ul>
<h2>How this comparison was made</h2>
<ul>
<li>Only facts written on each store page are used. Where a page doesn't say something, the table says "Not stated".</li>
<li>Privacy entries are what each developer declares in Google Play's Data safety section or Apple's privacy label. Stores don't verify them.</li>
<li>We didn't test how accurately the other apps count, so there's no accuracy column.</li>
<li>Prices and features change. Check the store page before you install. If something here is wrong, email <a href="mailto:{e}">{e}</a> and we'll fix it.</li>
</ul>
<h2>Whichever app you pick</h2>
<p>Every camera rep counter needs the same setup: your whole body in frame, good light and a steady phone. See <a href="{p}/guides/phone-placement/">where to put your phone</a>, and <a href="{p}/guides/on-device-pose-detection/">how on-device pose detection works</a>.</p>
""",
            "zh": """
<h2>一览表</h2>
<p>下表信息全部来自各 App 的美国区商店页，查阅日期 {checked}。手机上可以左右滑动表格。</p>
{compare}
<h2>怎么选</h2>
<ul>
<li><b>用 iPhone：</b>GoodGYM。KINETIC 暂时没有 iOS 版。</li>
<li><b>想要动作最多、有训练计划、能记健身房训练：</b>MyRepsCount。</li>
<li><b>练弯举、推举，想要动作错误和速度提示：</b>REP AI。</li>
<li><b>只练俯卧撑、深蹲、卷腹，想要每日挑战：</b>Repletic。</li>
<li><b>不想看广告、不想付费、不想注册，还想自己定每个动作做到多深才算：</b>KINETIC。</li>
</ul>
<h2>KINETIC 做不到的</h2>
<ul>
<li>目前只有 Android 版。</li>
<li>11 种动作，不能自定义动作。MyRepsCount 和 GoodGYM 能数的更多。</li>
<li>只判断动作幅度（关节角度）够不够，不提示动作错误，也不统计速度。</li>
<li>没有训练计划、游戏，不支持手表。</li>
</ul>
<h2>这份对比怎么做的</h2>
<ul>
<li>只用各 App 商店页上写明的信息。商店页没写的，表里写「未注明」。</li>
<li>隐私一栏是开发者在 Google Play「数据安全」或 App Store「App 隐私」里自己填的，商店不做核实。</li>
<li>我们没有实测其他 App 数得准不准，所以没有准确度一栏。</li>
<li>价格和功能会变，安装前以商店页为准。发现写错了，请发邮件到 <a href="mailto:{e}">{e}</a>，我们核实后修改。</li>
</ul>
<h2>不管用哪款</h2>
<p>摄像头计数 App 都要全身入镜、光线充足、手机放稳。具体见<a href="{p}/guides/phone-placement/">手机怎么摆</a>和<a href="{p}/guides/on-device-pose-detection/">本机姿态识别的原理</a>。</p>
""",
            "hant": """
<h2>一覽表</h2>
<p>下表資訊全部來自各 App 的美國區商店頁，查閱日期 {checked}。手機上可以左右滑動表格。</p>
{compare}
<h2>怎麼選</h2>
<ul>
<li><b>用 iPhone：</b>GoodGYM。KINETIC 暫時沒有 iOS 版。</li>
<li><b>想要動作最多、有訓練計畫、能記健身房訓練：</b>MyRepsCount。</li>
<li><b>練彎舉、推舉，想要動作錯誤和速度提示：</b>REP AI。</li>
<li><b>只練伏地挺身、深蹲、捲腹，想要每日挑戰：</b>Repletic。</li>
<li><b>不想看廣告、不想付費、不想註冊，還想自己定每個動作做到多深才算：</b>KINETIC。</li>
</ul>
<h2>KINETIC 做不到的</h2>
<ul>
<li>目前只有 Android 版。</li>
<li>11 種動作，不能自訂動作。MyRepsCount 和 GoodGYM 能數的更多。</li>
<li>只判斷動作幅度（關節角度）夠不夠，不提示動作錯誤，也不統計速度。</li>
<li>沒有訓練計畫、遊戲，不支援手錶。</li>
</ul>
<h2>這份比較怎麼做的</h2>
<ul>
<li>只用各 App 商店頁上寫明的資訊。商店頁沒寫的，表裡寫「未註明」。</li>
<li>隱私一欄是開發者在 Google Play「資料安全性」或 App Store「App 隱私權」裡自己填的，商店不做核實。</li>
<li>我們沒有實測其他 App 數得準不準，所以沒有準確度一欄。</li>
<li>價格和功能會變，安裝前以商店頁為準。發現寫錯了，請寄信到 <a href="mailto:{e}">{e}</a>，我們核實後修改。</li>
</ul>
<h2>不管用哪款</h2>
<p>相機計數 App 都要全身入鏡、光線充足、手機放穩。詳見<a href="{p}/guides/phone-placement/">手機怎麼擺</a>和<a href="{p}/guides/on-device-pose-detection/">本機姿勢辨識的原理</a>。</p>
""",
        },
    },
]

# 新手计划：(动作 id, 第 1～4 周的 (组数, 每组次数))，None 表示这一周还不做。
# 依据：完全新手每周 3 练、每个动作 2～3 组、每组 5～15 次，每周只加一组或每组加 1～3 次；
# 弓步蹲对平衡要求高，第 3 周再加。顺序按手机摆放分：先站立（正对、侧对），再地面
BEGINNER_PLAN = [
    ("jumping_jack", [(2, 15), (2, 20), (3, 20), (3, 25)]),
    ("squat", [(2, 8), (3, 8), (3, 10), (3, 12)]),
    ("lunge", [None, None, (2, 8), (3, 8)]),
    ("pushup", [(2, 5), (3, 5), (3, 6), (3, 8)]),
    ("glute_bridge", [(2, 10), (3, 10), (3, 12), (3, 15)]),
]

GUIDE_UI = {
    "hub_title": {"en": "KINETIC Guides – Phone Setup, Privacy and Challenges", "zh": "KINETIC 指南", "hant": "KINETIC 指南"},
    "hub_h1": {"en": "Guides", "zh": "指南", "hant": "指南"},
    "hub_desc": {
        "en": "Guides for counting reps with your phone camera: phone setup, how on-device pose detection works, and workout challenges.",
        "zh": "用手机摄像头计数的指南：手机摆放、本机姿态识别原理和训练挑战。",
        "hant": "用手機相機計數的指南：手機擺放、本機姿勢辨識原理和訓練挑戰。",
    },
    "day": {"en": "Day", "zh": "第几天", "hant": "第幾天"},
    "squats": {"en": "Squats", "zh": "深蹲次数", "hant": "深蹲次數"},
    "rest": {"en": "Rest", "zh": "休息", "hant": "休息"},
    "th_ex": {"en": "Exercise", "zh": "动作", "hant": "動作"},
    "th_phone": {"en": "Phone", "zh": "手机摆放", "hant": "手機擺放"},
    "th_rule": {"en": "Counts at", "zh": "判定", "hant": "判定"},
    "used_by": {"en": "Used for", "zh": "适用动作", "hant": "適用動作"},
    "week": {"en": "Week {n}", "zh": "第 {n} 周", "hant": "第 {n} 週"},
    "lunge_note": {"en": "alternate legs, each counts", "zh": "左右交替，每次都算", "hant": "左右交替，每次都算"},
}
