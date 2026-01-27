from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7523507276:AAGymd8zplnxNNZ95DIgnjd4vC9w5IDMo-E"
LOG_GROUP_ID = -1003781260774

# =====================================================
# KONU ANLATIMLARI (PDF'e Göre Güncellendi)
# =====================================================

topic_explain = {
    "İlkyardım Tanımı": "İlkyardım; olay yerinde, tıbbi araç gereç aranmaksızın mevcut imkanlarla ilaçsız yapılan müdahaledir. Acil tedavi ise profesyonel ekiplerce yapılır.",
    "ABC ve Değerlendirme": "A: Havayolu açıklığı, B: Solunum (Bak-Dinle-Hisset 10sn), C: Dolaşım (Şah damarından nabız 5sn).",
    "Yaşam Bulguları": "Normal Nabız: 60-100 (Yetişkin), 100-120 (Çocuk), 100-140 (Bebek). Normal Solunum: 12-20 (Yetişkin). Vücut Isısı: 36.5 C.",
    "Hayat Kurtarma Zinciri": "1. Halka: Bildirme (112), 2. Halka: Temel Yaşam Desteği, 3. Halka: Ambulans müdahalesi, 4. Halka: Hastane acil servisi.",
    "Kanamalar": "Atardamar: Açık kırmızı-fışkırır. Toplardamar: Koyu kırmızı-sızıntı. Kılcal damar: Küçük kabarcıklar. İlk kural baskıdır.",
    "Şok ve Pozisyonlar": "Şok; hayati organlara yetersiz kan gitmesidir. Ayaklar 30 cm kaldırılır. Bilinci kapalı solunumu olana Koma (Yan yatış) verilir.",
    "Zehirlenme ve Boğulma": "Zehirlenmede temel kural kusturmamaktır (yakıcı madde ise). Suda boğulmalarda ağızdan ağıza yapay solunum hayati önem taşır.",
    "Taşıma ve Genel": "Hasta asla gereksiz yere hareket ettirilmez. Baş-Boyun-Gövde ekseni her zaman korunmalıdır (Rentek manevrası)."
}

# =====================================================
# SORULAR (60 ADET - PDF İÇERİĞİNE GÖRE)
# =====================================================

questions = [
    # --- İLKYARDIM TEMELLERİ ---
    {"q":"İlkyardımda aşağıdakilerden hangisi aranmaz?","options":["A) Tıbbi araç gereç","B) Mevcut imkanlar","C) İlaçsız uygulama","D) Eğitimli müdahale"],"answer":0,"topic":"İlkyardım Tanımı"},
    {"q":"Acil tedavi ünitesinde doktor ve sağlık personeli tarafından yapılan müdahale nedir?","options":["A) İlkyardım","B) Acil Tedavi","C) Rehabilitasyon","D) Triaj"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"İlkyardımın öncelikli amaçlarından hangisi yanlıştır?","options":["A) Hayati tehlikeyi ortadan kaldırmak","B) İlaçla tedavi etmek","C) İyileşmeyi kolaylaştırmak","D) Durumun kötüleşmesini önlemek"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"Olay yerinin güvenliğini sağlama aşamasına ne denir?","options":["A) Bildirme","B) Koruma","C) Kurtarma","D) Sevk"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"112 aranırken verilmesi gereken en kritik bilgi hangisidir?","options":["A) Yaralının ismi","B) Olay yerinin net adresi","C) İlkyardımcının sertifika no","D) Hava durumu"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"Hayat kurtarma zincirinin 1. halkası nedir?","options":["A) Temel yaşam desteği","B) Sağlık kuruluşuna haber verme","C) Ambulans müdahalesi","D) Acil servis müdahalesi"],"answer":1,"topic":"Hayat Kurtarma Zinciri"},
    {"q":"İlkyardımcı tarafından yapılan 'Temel Yaşam Desteği' zincirin kaçıncı halkasıdır?","options":["A) 1","B) 2","C) 3","D) 4"],"answer":1,"topic":"Hayat Kurtarma Zinciri"},
    {"q":"İlkyardımcının müdahale sırasında önceliği nedir?","options":["A) Yaralıya moral vermek","B) Kendi can güvenliğini korumak","C) İlaç temin etmek","D) Kalabalığı dağıtmak"],"answer":1,"topic":"İlkyardım Tanımı"},

    # --- DEĞERLENDİRME & ABC ---
    {"q":"İlkyardımın ABC'sinde 'A' neyi ifade eder?","options":["A) Solunum","B) Dolaşım","C) Havayolu Açıklığı","D) Bilinç Kontrolü"],"answer":2,"topic":"ABC ve Değerlendirme"},
    {"q":"Bebeklerde bilinç kontrolü nasıl yapılır?","options":["A) İsmiyle seslenerek","B) Omuzlarını sarsarak","C) Ayak tabanına hafifçe vurarak","D) Göğsüne bastırarak"],"answer":2,"topic":"ABC ve Değerlendirme"},
    {"q":"Bak-Dinle-Hisset yöntemi kaç saniye uygulanmalıdır?","options":["A) 2 sn","B) 5 sn","C) 10 sn","D) 20 sn"],"answer":2,"topic":"ABC ve Değerlendirme"},
    {"q":"Nabız kontrolü yetişkinlerde hangi bölgeden yapılır?","options":["A) Şah Damarı","B) Bilek","C) Ayak sırtı","D) Şakak"],"answer":0,"topic":"ABC ve Değerlendirme"},
    {"q":"Nabız kontrolü kaç saniye yapılmalıdır?","options":["A) 2 sn","B) 5 sn","C) 10 sn","D) 30 sn"],"answer":1,"topic":"ABC ve Değerlendirme"},
    {"q":"Yetişkin bir kişide normal solunum sayısı dakikada kaçtır?","options":["A) 8-10","B) 12-20","C) 20-30","D) 40-50"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Yetişkinlerde normal nabız sayısı dakikada kaçtır?","options":["A) 60-100","B) 100-120","C) 120-140","D) 40-60"],"answer":0,"topic":"Yaşam Bulguları"},
    {"q":"Bebeklerde normal nabız aralığı nedir?","options":["A) 60-100","B) 80-100","C) 100-140","D) 150-200"],"answer":2,"topic":"Yaşam Bulguları"},
    {"q":"Normal vücut ısısı kaç derecedir?","options":["A) 35.5","B) 36.5","C) 37.5","D) 38.5"],"answer":1,"topic":"Yaşam Bulguları"},

    # --- POZİSYONLAR & MANEVRALAR ---
    {"q":"Bilinci kapalı ama solunumu olan yaralıya hangi pozisyon verilir?","options":["A) Şok","B) Koma (Yan yatış)","C) Sırtüstü","D) Yarı oturuş"],"answer":1,"topic":"Şok ve Pozisyonlar"},
    {"q":"Şok pozisyonunda ayaklar kaç cm kaldırılır?","options":["A) 15 cm","B) 30 cm","C) 45 cm","D) 60 cm"],"answer":1,"topic":"Şok ve Pozisyonlar"},
    {"q":"Havayolunu açmak için kullanılan manevra hangisidir?","options":["A) Rentek","B) Heimlich","C) Baş geri-Çene yukarı","D) Şok"],"answer":2,"topic":"ABC ve Değerlendirme"},
    {"q":"Tam tıkanma (boğaza yabancı cisim) durumunda ne yapılır?","options":["A) Sırtına vurulur","B) Heimlich Manevrası","C) Öksürtülür","D) Su içirilir"],"answer":1,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Kısmi tıkanma yaşayan kişiye ilkyardımcı ne yapar?","options":["A) Sırtına vurur","B) Dokunmaz, öksürmeye teşvik eder","C) Heimlich yapar","D) Kusturur"],"answer":1,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Araç içindeki yaralıyı omuriliğine zarar vermeden çıkarma yöntemi nedir?","options":["A) İtfaiyeci yöntemi","B) Rentek Manevrası","C) Altın beşik","D) Kaşık tekniği"],"answer":1,"topic":"Taşıma ve Genel"},

    # --- KANAMALAR ---
    {"q":"Fışkırır tarzda ve açık kırmızı renkli kanama hangi damara aittir?","options":["A) Atardamar","B) Toplardamar","C) Kılcal damar","D) Kemik iliği"],"answer":0,"topic":"Kanamalar"},
    {"q":"Koyu kırmızı renkli ve sızıntı şeklinde sürekli akan kanama hangisidir?","options":["A) Atardamar","B) Toplardamar","C) Kılcal damar","D) Mide kanaması"],"answer":1,"topic":"Kanamalar"},
    {"q":"Dış kanamalarda ilk yapılması gereken nedir?","options":["A) Turnike uygulamak","B) Yara üzerine temiz bezle baskı yapmak","C) Kolonya sürmek","D) Bölgeyi yıkamak"],"answer":1,"topic":"Kanamalar"},
    {"q":"Kanayan bölge kalp seviyesine göre nasıl tutulmalıdır?","options":["A) Aşağıda","B) Yukarıda","C) Aynı hizada","D) Önemli değildir"],"answer":1,"topic":"Kanamalar"},
    {"q":"Turnike hangi durumda uygulanır?","options":["A) Küçük kesiklerde","B) Uzuv kopması veya baskıyla durmayan kanamada","C) Burun kanamasında","D) Sıyırıklarda"],"answer":1,"topic":"Kanamalar"},
    {"q":"Turnike kaç dakikada bir gevşetilmelidir?","options":["A) 5-10 dk","B) 15-20 dk","C) 30-40 dk","D) Gevşetilmez"],"answer":1,"topic":"Kanamalar"},
    {"q":"Burun kanamasında hangi pozisyon verilmelidir?","options":["A) Baş arkaya atılır","B) Baş hafif öne eğilir, burun kanatları sıkılır","C) Sırtüstü yatırılır","D) Amonyak koklatılır"],"answer":1,"topic":"Kanamalar"},

    # --- SİSTEMLER ---
    {"q":"Hücre ve dokuların oksijenlenmesini sağlayan sistem hangisidir?","options":["A) Sindirim","B) Solunum","C) Hareket","D) Boşaltım"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Beyin ve omurilik hangi sistemin parçasıdır?","options":["A) Sinir","B) Dolaşım","C) Hareket","D) Boşaltım"],"answer":0,"topic":"Yaşam Bulguları"},
    {"q":"Kanı süzerek vücut dışına atılmasını sağlayan sistem hangisidir?","options":["A) Sindirim","B) Dolaşım","C) Boşaltım","D) Hareket"],"answer":2,"topic":"Yaşam Bulguları"},
    {"q":"Vücudun en küçük yapı taşına ne denir?","options":["A) Doku","B) Organ","C) Hücre","D) Sistem"],"answer":2,"topic":"Yaşam Bulguları"},

    # --- CPR (TEMEL YAŞAM DESTEĞİ) ---
    {"q":"Yetişkinlerde kalp masajı bası derinliği ne kadar olmalıdır?","options":["A) 1-2 cm","B) 5 cm","C) 8 cm","D) 10 cm"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Yetişkinlerde kalp masajı / suni solunum oranı kaçtır?","options":["A) 15/2","B) 30/2","C) 30/5","D) 10/1"],"answer":1,"topic":"ABC ve Değerlendirme"},
    {"q":"Kalp masajı dakikada kaç bası olacak şekilde uygulanır?","options":["A) 60","B) 80","C) 100-120","D) 150"],"answer":2,"topic":"Yaşam Bulguları"},
    {"q":"Bebeklerde suni solunum nasıl yapılır?","options":["A) Sadece ağıza","B) Sadece buruna","C) Ağız ve burun birlikte ağız içine alınarak","D) Şiddetli üfleyerek"],"answer":2,"topic":"ABC ve Değerlendirme"},

    # --- DİĞER ACİL DURUMLAR ---
    {"q":"Suda boğulmada temel neden nedir?","options":["A) Korku","B) Nefes borusunun kasılarak havanın girmesini engellemesi","C) Midenin su dolması","D) Kulak delinmesi"],"answer":1,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Gözde yabancı bir cisim batmışsa ne yapılır?","options":["A) Hemen çıkarılır","B) Bol suyla yıkanır","C) Cisim sabitlenir, iki göz kapatılıp hastaneye sevk edilir","D) Ovuşturulur"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Sara (Epilepsi) krizi geçiren birine ne yapılmalıdır?","options":["A) Ağzı zorla açılır","B) Kolonya dökülür","C) Kendi haline bırakılır, başı korunur, zarar görmesi önlenir","D) Kolları bağlanır"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Sıcak çarpmasında hasta hangi pozisyona alınır?","options":["A) Yüzüstü","B) Sırtüstü yatırılır, kol ve bacaklar kaldırılır","C) Yan yatış","D) Oturur"],"answer":1,"topic":"Şok ve Pozisyonlar"},
    {"q":"Donma vakalarında hangisi yapılmaz?","options":["A) Ilık ortama alınır","B) Islak giysiler çıkarılır","C) Bölge karla ovulur","D) Şekerli içecek verilir"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Akrep/Yılan sokmasında ilk yardım hangisidir?","options":["A) Bölge kesilir ve emilir","B) Hareket ettirilmez, soğuk uygulanır","C) Sıcak suyla yıkanır","D) Yakılır"],"answer":1,"topic":"Taşıma ve Genel"},
    {"q":"Kulağa kaçan böcekte ne yapılır?","options":["A) Cımbızla çekilir","B) Su fışkırtılır","C) Işık tutulur veya yağ damlatılır","D) Kulak çöpüyle itilir"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Hayvan ısırmalarında yara kaç dakika sabunlu suyla yıkanmalıdır?","options":["A) 1 dk","B) 2 dk","C) 5 dk","D) Hiç yıkanmaz"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Hangisi bir ilkyardımcı özelliğidir?","options":["A) Telaşlı olmak","B) Sağlık personeli olmak","C) Sakin ve özgüvenli olmak","D) Her zaman ilaç kullanmak"],"answer":2,"topic":"İlkyardım Tanımı"},
    {"q":"Göğüs ağrısı olan (kalp krizi şüphesi) hastaya hangi pozisyon verilir?","options":["A) Şok","B) Koma","C) Yarı oturuş","D) Yüzüstü"],"answer":2,"topic":"Şok ve Pozisyonlar"},
    {"q":"Bilinci açık, karın bölgesinde saplanmış cisim olan yaralıya ne yapılır?","options":["A) Cisim çıkarılır","B) Cisim çıkarılmaz, etrafı desteklenerek sabitlenir","C) Yaralı yürütülür","D) Bölgeye alkol dökülür"],"answer":1,"topic":"Taşıma ve Genel"},
    {"q":"Kırık şüphesinde bölge nasıl sabitlenir?","options":["A) Sıkıca sarılarak","B) Bir üst ve bir alt eklemi de içine alacak şekilde","C) Sadece kırık noktasından","D) Hareket ettirilerek"],"answer":1,"topic":"Taşıma ve Genel"},
    {"q":"Kafaya darbe almış bir yaralı kaç saat gözlem altında tutulmalıdır?","options":["A) 2 saat","B) 6 saat","C) 12-24 saat","D) 48 saat"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"Boğazına yabancı cisim kaçan bebekte Heimlich nasıl uygulanır?","options":["A) Karna baskı yaparak","B) Kol üzerine yüzüstü yatırılıp sırtına vurularak","C) Ayaklarından asılarak","D) Su içirerek"],"answer":1,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Kopmuş uzuv (parmak vb.) nasıl taşınır?","options":["A) Doğrudan buzun içinde","B) Su dolu kapta","C) Temiz bezle sarılıp poşete, o poşet de buzlu su dolu kaba konularak","D) Tuzlu suda"],"answer":2,"topic":"Kanamalar"},
    {"q":"Şeker komasında nefes nasıl kokar?","options":["A) Alkol","B) Aseton/Çürük Elma","C) Sarımsak","D) Kokmaz"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Rentek manevrası hangi yaralıyı taşımak içindir?","options":["A) Kırığı olan","B) Suda boğulan","C) Araçtan çıkarılması gereken","D) Merdivenden düşen"],"answer":2,"topic":"Taşıma ve Genel"},
    {"q":"114 numaralı telefon hangi merkeze aittir?","options":["A) Polis","B) İtfaiye","C) Ulusal Zehir Danışma Merkezi (UZEM)","D) Sahil Güvenlik"],"answer":2,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Asit veya baz gibi yakıcı madde içen kişi neden kusturulmaz?","options":["A) Midesi bulanmasın diye","B) Yemek borusu ikinci kez zarar görmesin diye","C) İlaç etkisiz kalır","D) Kusturmak zordur"],"answer":1,"topic":"Zehirlenme ve Boğulma"},
    {"q":"Yaralı bir kişinin ikinci değerlendirmesinde aşağıdakilerden hangisi yapılır?","options":["A) 112 aranır","B) Baştan aşağı kontrol edilir","C) Suni solunum yapılır","D) Turnike uygulanır"],"answer":1,"topic":"ABC ve Değerlendirme"},
    {"q":"Elektrik çarpmasında ilk yardımın birinci adımı nedir?","options":["A) Hastaya su içirmek","B) Akımı kesmek","C) Kalp masajı","D) Yarayı sarmak"],"answer":1,"topic":"Taşıma ve Genel"},
    {"q":"İlkyardım müdahalesinde triaj nedir?","options":["A) Yaralı taşıma yöntemi","B) Öncelikli yaralıyı belirleme","C) Sargı çeşidi","D) Haberleşme sistemi"],"answer":1,"topic":"İlkyardım Tanımı"}
]

# =====================================================
# BOT FONKSİYONLARI
# =====================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🩺 Sağlık Soruları", callback_data="start_test")],
        [InlineKeyboardButton("📊 Durumum", callback_data="status")],
        [InlineKeyboardButton("👥 Teste Katılanlar", callback_data="users")]
    ]
    await update.message.reply_text("🚢 *Sahil Güvenlik Sağlık Test Sistemi*\n\nPDF içeriğine göre hazırlanan 60 soru ile bilginizi test edin.", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    context.user_data["index"] = 0
    context.user_data["correct"] = 0
    context.user_data["wrong"] = []
    await send_question(update, context)

async def send_question(update, context):
    current_idx = context.user_data["index"]
    total_q = len(questions)
    q = questions[current_idx]
    
    keyboard = [[InlineKeyboardButton(opt, callback_data=str(i))] for i, opt in enumerate(q["options"])]
    
    message_text = (
        f"🩺 *Sahil Güvenlik Sağlık Soruları*\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📝 *Soru:* {current_idx + 1} / {total_q}\n"
        f"📌 *Konu:* {q['topic']}\n"
        f"━━━━━━━━━━━━━━━\n\n"
        f"*{q['q']}*"
    )
    
    if update.callback_query:
        await update.callback_query.message.reply_text(message_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    else:
        await update.message.reply_text(message_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.delete()

    idx = context.user_data["index"]
    user_ans = int(query.data)
    correct = questions[idx]["answer"]
    topic = questions[idx]["topic"]
    uid = query.from_user.id

    if "stats" not in context.bot_data: context.bot_data["stats"] = {}
    if uid not in context.bot_data["stats"]: context.bot_data["stats"][uid] = {}
    if topic not in context.bot_data["stats"][uid]: context.bot_data["stats"][uid][topic] = {"correct":0,"total":0}

    context.bot_data["stats"][uid][topic]["total"] += 1

    if user_ans == correct:
        context.user_data["correct"] += 1
        context.bot_data["stats"][uid][topic]["correct"] += 1
    else:
        wrong_q = questions[idx].copy()
        wrong_q["your"] = questions[idx]["options"][user_ans]
        wrong_q["correct_text"] = questions[idx]["options"][correct]
        context.user_data["wrong"].append(wrong_q)

    context.user_data["index"] += 1

    if context.user_data["index"] < len(questions):
        await send_question(update, context)
    else:
        await finish(query, context)

async def finish(query, context):
    correct = context.user_data["correct"]
    total = len(questions)
    wrong = total - correct
    user = query.from_user.full_name

    if "users" not in context.bot_data: context.bot_data["users"] = []
    context.bot_data["users"].append(f"{user} → ✅ {correct} | ❌ {wrong}")

    await context.bot.send_message(LOG_GROUP_ID, f"🩺 TEST TAMAMLANDI\n👤 {user}\n✅ Doğru: {correct}\n❌ Yanlış: {wrong}\n📊 Başarı: %{int((correct/total)*100)}")

    await query.message.reply_text(
        f"📋 *Test Tamamlandı*\n\n"
        f"👤 Katılımcı: {user}\n"
        f"✅ Doğru Sayısı: {correct}\n"
        f"❌ Yanlış Sayısı: {wrong}\n"
        f"📈 Başarı Oranı: %{int((correct/total)*100)}",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Yanlışları İncele", callback_data="show_wrong")]]),
        parse_mode="Markdown"
    )

async def show_wrong(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if not context.user_data.get("wrong"):
        await query.message.reply_text("🎉 Muazzam! Tüm soruları doğru cevapladın.")
        return
    for i, q in enumerate(context.user_data["wrong"]):
        await query.message.reply_text(
            f"❌ *Yanlış Cevaplanan Soru*\n\n"
            f"{q['q']}\n\n"
            f"👉 Senin Cevabın: {q['your']}\n"
            f"✅ Doğru Cevap: {q['correct_text']}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📘 Konu Özeti", callback_data=f"topic_{i}")]]),
            parse_mode="Markdown"
        )

async def show_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    idx = int(query.data.split("_")[1])
    topic = context.user_data["wrong"][idx]["topic"]
    await query.message.reply_text(f"📘 *{topic} Konu Bilgisi*\n\n{topic_explain.get(topic, 'Bilgi bulunamadı.')}", parse_mode="Markdown")

async def show_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if "users" not in context.bot_data or not context.bot_data["users"]:
        await query.message.reply_text("Henüz listelenecek bir veri yok.")
        return
    await query.message.reply_text("👥 *Son Test Skorları*\n\n" + "\n".join(context.bot_data["users"][-20:]), parse_mode="Markdown")

async def show_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    uid = query.from_user.id
    if "stats" not in context.bot_data or uid not in context.bot_data["stats"]:
        await query.message.reply_text("📊 Henüz istatistik oluşmadı.")
        return
    text = "📊 *Konu Bazlı Başarı Analizin*\n\n"
    for topic, data in context.bot_data["stats"][uid].items():
        percent = int((data["correct"]/data["total"])*100)
        text += f"📌 {topic}: %{percent} ({data['correct']}/{data['total']})\n"
    await query.message.reply_text(text, parse_mode="Markdown")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(start_test, pattern="start_test"))
app.add_handler(CallbackQueryHandler(show_users, pattern="users"))
app.add_handler(CallbackQueryHandler(show_wrong, pattern="show_wrong"))
app.add_handler(CallbackQueryHandler(show_topic, pattern="topic_"))
app.add_handler(CallbackQueryHandler(show_status, pattern="status"))
app.add_handler(CallbackQueryHandler(handle_answer))

print("Bot aktif... Sahil Güvenlik Serdümen Sağlık Soruları (60 Soru) çalışıyor.")
app.run_polling()