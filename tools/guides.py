"""指南页正文（三种语言）。

body 里的占位符由 build.py 填：{p} 是当前语言的网址前缀（英文为空、简中 /zh、繁中 /zh-hant），
{table}、{postures} 只在手机摆放指南里用，按 content.EXERCISES 自动生成。
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
}
