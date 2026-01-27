from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7523507276:AAGymd8zplnxNNZ95DIgnjd4vC9w5IDMo-E"
LOG_GROUP_ID = -1003781260774

# =====================================================
# SORU HAVUZLARI
# =====================================================

gk_questions = [
{"q":"Aşağıdaki cümlelerin hangisinde yazım yanlışı vardır?","options":["A) Hiçbir şey söylemedi.","B) Bugün ki sınav çok zordu.","C) Ankara’ya gideceğim.","D) Pek çok kişi geldi."],"answer":1,"topic":"Türkçe"},
{"q":"Aşağıdakilerden hangisi zarf değildir?","options":["A) Hızlıca","B) Dün","C) Güzellik","D) Yukarı"],"answer":2,"topic":"Türkçe"},
{"q":"“Kitap okumayı severim.” cümlesindeki fiilin türü nedir?","options":["A) Oluş","B) Durum","C) İş (kılış)","D) Yardımcı fiil"],"answer":2,"topic":"Türkçe"},
{"q":"Aşağıdaki sözcüklerden hangisi türemiştir?","options":["A) Ev","B) Kalem","C) Mutluluk","D) Taş"],"answer":2,"topic":"Türkçe"},
{"q":"Aşağıdakilerden hangisi birleşik kelimedir?","options":["A) Başkent","B) Akşamüstü","C) Mavi","D) Deniz"],"answer":1,"topic":"Türkçe"},
{"q":"“Ne…ne de” bağlacı aşağıdakilerden hangisini ifade eder?","options":["A) Sebep","B) Olumsuzluk","C) Karşıtlık","D) Açıklama"],"answer":1,"topic":"Türkçe"},
{"q":"Aşağıdakilerden hangisi isim tamlamasıdır?","options":["A) Güzel ev","B) Evler","C) Okul bahçesi","D) Çalışıyor"],"answer":2,"topic":"Türkçe"},
{"q":"“Koşarak geldi.” cümlesinde hangi öge vurgulanmıştır?","options":["A) Zaman","B) Yer","C) Durum","D) Kişi"],"answer":2,"topic":"Türkçe"},
{"q":"Aşağıdakilerden hangisi mecaz anlamlıdır?","options":["A) Taş kalpli insan","B) Taş ev","C) Taş yol","D) Taş duvar"],"answer":0,"topic":"Türkçe"},
{"q":"Aşağıdaki kelimelerden hangisi eş seslidir?","options":["A) Yüz","B) Kalem","C) Kitap","D) Defter"],"answer":0,"topic":"Türkçe"},

# ======================
# İNKILAP TARİHİ (10)
# ======================
{"q":"Mustafa Kemal Atatürk’ün doğduğu şehir hangisidir?","options":["A) İstanbul","B) Selanik","C) Sofya","D) Manastır"],"answer":1,"topic":"İnkılap Tarihi"},
{"q":"Milli Mücadele’yi fiilen başlatan olay hangisidir?","options":["A) Erzurum Kongresi","B) Havza Genelgesi","C) Samsun’a çıkış","D) Amasya Genelgesi"],"answer":2,"topic":"İnkılap Tarihi"},
{"q":"TBMM hangi tarihte açılmıştır?","options":["A) 19 Mayıs 1919","B) 23 Nisan 1920","C) 29 Ekim 1923","D) 30 Ağustos 1922"],"answer":1,"topic":"İnkılap Tarihi"},
{"q":"Cumhuriyet hangi tarihte ilan edilmiştir?","options":["A) 23 Nisan 1920","B) 30 Ağustos 1922","C) 29 Ekim 1923","D) 3 Mart 1924"],"answer":2,"topic":"İnkılap Tarihi"},
{"q":"Saltanatın kaldırılması hangi tarihte olmuştur?","options":["A) 1920","B) 1921","C) 1922","D) 1923"],"answer":2,"topic":"İnkılap Tarihi"},
{"q":"Aşağıdakilerden hangisi Atatürk ilkelerinden biridir?","options":["A) Monarşi","B) Laiklik","C) Teokrasi","D) Oligarşi"],"answer":1,"topic":"İnkılap Tarihi"},
{"q":"Medeni Kanun hangi ülkeden alınmıştır?","options":["A) Fransa","B) Almanya","C) İsviçre","D) İtalya"],"answer":2,"topic":"İnkılap Tarihi"},
{"q":"Harf İnkılabı hangi yıl yapılmıştır?","options":["A) 1923","B) 1925","C) 1928","D) 1930"],"answer":2,"topic":"İnkılap Tarihi"},
{"q":"Atatürk’ün “Yurtta sulh, cihanda sulh” sözü hangi ilkeyi vurgular?","options":["A) Devletçilik","B) Milliyetçilik","C) Halkçılık","D) Barışçılık"],"answer":3,"topic":"İnkılap Tarihi"},
{"q":"Halifelik hangi yıl kaldırılmıştır?","options":["A) 1922","B) 1923","C) 1924","D) 1928"],"answer":2,"topic":"İnkılap Tarihi"},

# ======================
# COĞRAFYA (10)
# ======================
{"q":"Türkiye’nin en uzun nehri hangisidir?","options":["A) Fırat","B) Kızılırmak","C) Dicle","D) Sakarya"],"answer":1,"topic":"Coğrafya"},
{"q":"Türkiye’nin en yüksek dağı hangisidir?","options":["A) Erciyes","B) Kaçkar","C) Ağrı","D) Süphan"],"answer":2,"topic":"Coğrafya"},
{"q":"Ege Bölgesi’nin kıyı tipi hangisidir?","options":["A) Dalmaçya","B) Ria","C) Boyuna","D) Enine"],"answer":3,"topic":"Coğrafya"},
{"q":"Türkiye’de en fazla nüfusa sahip il hangisidir?","options":["A) Ankara","B) İzmir","C) İstanbul","D) Bursa"],"answer":2,"topic":"Coğrafya"},
{"q":"Karadeniz Bölgesi’nin en belirgin iklim özelliği nedir?","options":["A) Yazları kurak","B) Ilıman ve her mevsim yağışlı","C) Sert karasal","D) Muson"],"answer":1,"topic":"Coğrafya"},
{"q":"Türkiye kaç coğrafi bölgeye ayrılır?","options":["A) 5","B) 6","C) 7","D) 8"],"answer":2,"topic":"Coğrafya"},
{"q":"Dünyanın en büyük okyanusu hangisidir?","options":["A) Atlas","B) Hint","C) Büyük (Pasifik)","D) Kuzey Buz"],"answer":2,"topic":"Coğrafya"},
{"q":"Aşağıdakilerden hangisi Türkiye’de yetişmez?","options":["A) Muz","B) Çay","C) Zeytin","D) Kahve"],"answer":3,"topic":"Coğrafya"},
{"q":"Türkiye’nin üç tarafının denizlerle çevrili olması neyi etkiler?","options":["A) İklimi","B) Tarımı","C) Ulaşımı","D) Hepsini"],"answer":3,"topic":"Coğrafya"},
{"q":"Enlem etkisine bağlı olarak hangisi değişir?","options":["A) Bitki örtüsü","B) Gece-gündüz süresi","C) Sıcaklık","D) Hepsi"],"answer":3,"topic":"Coğrafya"},

# ======================
# ANAYASA (10)
# ======================
{"q":"Türkiye Cumhuriyeti’nin yönetim şekli nedir?","options":["A) Monarşi","B) Cumhuriyet","C) Oligarşi","D) Teokrasi"],"answer":1,"topic":"Anayasa"},
{"q":"Anayasaya göre egemenlik kime aittir?","options":["A) Cumhurbaşkanına","B) TBMM’ye","C) Millete","D) Anayasa Mahkemesine"],"answer":2,"topic":"Anayasa"},
{"q":"Türkiye Cumhuriyeti’nin resmi dili nedir?","options":["A) Arapça","B) İngilizce","C) Türkçe","D) Osmanlıca"],"answer":2,"topic":"Anayasa"},
{"q":"Türkiye Cumhuriyeti’nin başkenti neresidir?","options":["A) İstanbul","B) Ankara","C) İzmir","D) Bursa"],"answer":1,"topic":"Anayasa"},
{"q":"Yasama yetkisi kime aittir?","options":["A) Cumhurbaşkanı","B) Bakanlar","C) TBMM","D) Anayasa Mahkemesi"],"answer":2,"topic":"Anayasa"},
{"q":"Anayasa Mahkemesi’nin temel görevi nedir?","options":["A) Yasa yapmak","B) Denetim yapmak","C) Hükümet kurmak","D) Seçim yapmak"],"answer":1,"topic":"Anayasa"},
{"q":"Temel hak ve özgürlükler hangi durumda sınırlandırılabilir?","options":["A) Keyfi olarak","B) Anayasa ve kanunlarla","C) Valilik kararıyla","D) Basın yoluyla"],"answer":1,"topic":"Anayasa"},
{"q":"Türkiye Cumhuriyeti hangi devlet şekline sahiptir?","options":["A) Üniter","B) Federal","C) Konfederal","D) Krallık"],"answer":0,"topic":"Anayasa"},
{"q":"Cumhurbaşkanı kaç yılda bir seçilir?","options":["A) 4","B) 5","C) 6","D) 7"],"answer":1,"topic":"Anayasa"},
{"q":"Türkiye Büyük Millet Meclisi kaç üyeden oluşur?","options":["A) 500","B) 550","C) 600","D) 650"],"answer":2,"topic":"Anayasa"},

# ======================
# GÜNCEL & GENEL KÜLTÜR (10)
# ======================
{"q":"Türkiye NATO’ya hangi yıl üye olmuştur?","options":["A) 1949","B) 1950","C) 1952","D) 1955"],"answer":2,"topic":"Genel Kültür"},
{"q":"Birleşmiş Milletler’in merkezi nerededir?","options":["A) Cenevre","B) Paris","C) New York","D) Brüksel"],"answer":2,"topic":"Genel Kültür"},
{"q":"İstiklal Marşı’nın yazarı kimdir?","options":["A) Yahya Kemal","B) Mehmet Akif Ersoy","C) Tevfik Fikret","D) Ziya Gökalp"],"answer":1,"topic":"Genel Kültür"},
{"q":"Türkiye’nin milli para birimi nedir?","options":["A) Dinar","B) Euro","C) Türk Lirası","D) Dolar"],"answer":2,"topic":"Genel Kültür"},
{"q":"Dünya Sağlık Örgütü’nün kısaltması nedir?","options":["A) UNICEF","B) WHO","C) NATO","D) UNESCO"],"answer":1,"topic":"Genel Kültür"},
{"q":"2024 Yaz Olimpiyatları hangi şehirde yapılmıştır?","options":["A) Tokyo","B) Paris","C) Londra","D) Roma"],"answer":1,"topic":"Genel Kültür"},
{"q":"Türkiye’nin uluslararası telefon kodu kaçtır?","options":["A) +80","B) +88","C) +90","D) +99"],"answer":2,"topic":"Genel Kültür"},
{"q":"En uzun yaşayan hayvan türlerinden biri hangisidir?","options":["A) Fil","B) Kaplumbağa","C) Köpek","D) Aslan"],"answer":1,"topic":"Genel Kültür"},
{"q":"Dünyanın en kalabalık ülkesi hangisidir?","options":["A) ABD","B) Çin","C) Hindistan","D) Rusya"],"answer":2,"topic":"Genel Kültür"},
{"q":"Ay’a ayak basan ilk insan kimdir?","options":["A) Yuri Gagarin","B) Neil Armstrong","C) Buzz Aldrin","D) Elon Musk"],"answer":1,"topic":"Genel Kültür"},
]

health_questions = [
    {"q":"İlkyardımda aşağıdakilerden hangisi aranmaz?","options":["A) Tıbbi araç gereç","B) Mevcut imkanlar","C) İlaçsız uygulama","D) Eğitimli müdahale"],"answer":0,"topic":"İlkyardım Tanımı"},
    {"q":"Acil tedavi ünitesinde doktor ve sağlık personeli tarafından yapılan müdahale nedir?","options":["A) İlkyardım","B) Acil Tedavi","C) Rehabilitasyon","D) Triaj"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"İlkyardımın öncelikli amaçlarından hangisi yanlıştır?","options":["A) Hayati tehlikeyi ortadan kaldırmak","B) İlaçla tedavi etmek","C) İyileşmeyi kolaylaştırmak","D) Durumun kötüleşmesini önlemek"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"Olay yerinin güvenliğini sağlama aşamasına ne denir?","options":["A) Bildirme","B) Koruma","C) Kurtarma","D) Sevk"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"112 aranırken verilmesi gereken en kritik bilgi hangisidir?","options":["A) Yaralının ismi","B) Olay yerinin net adresi","C) İlkyardımcının sertifika no","D) Hava durumu"],"answer":1,"topic":"İlkyardım Tanımı"},
    {"q":"Hayat kurtarma zincirinin 1. halkası nedir?","options":["A) Temel yaşam desteği","B) Sağlık kuruluşuna haber verme","C) Ambulans müdahalesi","D) Acil servis müdahalesi"],"answer":1,"topic":"Hayat Kurtarma Zinciri"},
    {"q":"İlkyardımcı tarafından yapılan 'Temel Yaşam Desteği' zincirin kaçıncı halkasıdır?","options":["A) 1","B) 2","C) 3","D) 4"],"answer":1,"topic":"Hayat Kurtarma Zinciri"},
    {"q":"İlkyardımcının önceliği ne olmalıdır?","options":["A) Yaralıya moral vermek","B) Kendi can güvenliğini korumak","C) İlaç temin etmek","D) Kalabalığı dağıtmak"],"answer":1,"topic":"İlkyardım Tanımı"},

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
    {"q":"Turnike kaç dakikada bir gevşetilmelidir?","options":["A) 5-15 dk","B) 15-30 dk","C) 30-40 dk","D) Gevşetilmez"],"answer":1,"topic":"Kanamalar"},
    {"q":"Burun kanamasında hangi pozisyon verilmelidir?","options":["A) Baş arkaya atılır","B) Baş hafif öne eğilir, burun kanatları sıkılır","C) Sırtüstü yatırılır","D) Amonyak koklatılır"],"answer":1,"topic":"Kanamalar"},

    # --- SİSTEMLER ---
    {"q":"Hücre ve dokuların oksijenlenmesini sağlayan sistem hangisidir?","options":["A) Sindirim","B) Solunum","C) Hareket","D) Boşaltım"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Beyin ve omurilik hangi sistemin parçasıdır?","options":["A) Sinir","B) Dolaşım","C) Hareket","D) Boşaltım"],"answer":0,"topic":"Yaşam Bulguları"},
    {"q":"Kanı süzerek vücut dışına atılmasını sağlayan sistem hangisidir?","options":["A) Sindirim","B) Dolaşım","C) Boşaltım","D) Hareket"],"answer":2,"topic":"Yaşam Bulguları"},
    {"q":"Vücudun en küçük yapı taşına ne denir?","options":["A) Doku","B) Organ","C) Hücre","D) Sistem"],"answer":2,"topic":"Yaşam Bulguları"},

    # --- CPR (TEMEL YAŞAM DESTEĞİ) ---
    {"q":"Yetişkinlerde kalp masajı bası derinliği ne kadar olmalıdır?","options":["A) 1-2 cm","B) 5 cm","C) 8 cm","D) 10 cm"],"answer":1,"topic":"Yaşam Bulguları"},
    {"q":"Yetişkinlerde kalp masajı / suni solunum oranı kaçtır?","options":["A) 15/2","B) 30/2","C) 30/5","D) 10/1"],"answer":1,"topic":"ABC ve Değerlendirme"},
    {"q":"Kalp masajı dakikada kaç bası olacak şekilde uygulanır?","options":["A) 60","B) 80","C) 100","D) 150"],"answer":2,"topic":"Yaşam Bulguları"},
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

    if update.effective_chat.type != "private":

        await update.message.reply_text("⚠️ Botu özel sohbetten başlatabilirsiniz. @SgSaglik_bot ' a tıklayarak özel sohbet üzerinden devam edin.")

        return

    keyboard = [
        [InlineKeyboardButton("💊 Sağlık Soruları", callback_data="start_health"),
         InlineKeyboardButton("🌍 Genel Kültür Soruları", callback_data="start_gk")],
        [InlineKeyboardButton("📊 Sağlık Sonuçlarım", callback_data="status_health"),
         InlineKeyboardButton("📈 GK Sonuçlarım", callback_data="status_gk")],
        [InlineKeyboardButton("👥 Teste Katılanlar", callback_data="users")]
    ]
    text = "🚢 *Sahil Güvenlik Sınav Hazırlık Sistemi*\n\nLütfen katılmak istediğiniz testi seçin. Sonuçlarınız test bittikten sonra hem size hem gruba iletilecektir."

    if update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    else:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    mode = "gk" if query.data == "start_gk" else "health"
    context.user_data.clear()
    context.user_data["mode"] = mode
    context.user_data["questions"] = gk_questions if mode == "gk" else health_questions
    context.user_data["index"] = 0
    context.user_data["correct"] = 0
    context.user_data["wrong_list"] = [] # Yanlışları kaydetmek için

    await send_question(update, context)

async def send_question(update, context):
    data = context.user_data
    q = data["questions"][data["index"]]

    mode_text = "🌍 Genel Kültür" if data["mode"] == "gk" else "💊 Sağlık"
    keyboard = [[InlineKeyboardButton(opt, callback_data=f"ans_{i}")] for i, opt in enumerate(q["options"])]

    msg = (f"*{mode_text} Testi*\n━━━━━━━━━━━━━━━\n"
           f"📝 Soru: {data['index'] + 1} / {len(data['questions'])}\n"
           f"📌 Konu: {q['topic']}\n━━━━━━━━━━━━━━━\n\n"
           f"*{q['q']}*")

    await update.callback_query.message.edit_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_ans = int(query.data.split("_")[1])
    data = context.user_data
    q = data["questions"][data["index"]]
    uid = str(query.from_user.id)
    mode = data["mode"]

    if "stats" not in context.bot_data: context.bot_data["stats"] = {}
    if uid not in context.bot_data["stats"]: context.bot_data["stats"][uid] = {"health": {}, "gk": {}, "name": query.from_user.full_name}

    topic = q["topic"]
    if topic not in context.bot_data["stats"][uid][mode]:
        context.bot_data["stats"][uid][mode][topic] = {"correct": 0, "total": 0}

    context.bot_data["stats"][uid][mode][topic]["total"] += 1

    if user_ans == q["answer"]:
        data["correct"] += 1
        context.bot_data["stats"][uid][mode][topic]["correct"] += 1
    else:
        # Yanlış detayı kaydet
        data["wrong_list"].append({
            "no": data["index"] + 1,
            "topic": q["topic"],
            "q": q["q"],
            "user_choice": q["options"][user_ans],
            "correct_choice": q["options"][q["answer"]]
        })

    data["index"] += 1
    if data["index"] < len(data["questions"]):
        await send_question(update, context)
    else:
        await finish_test(update, context)

async def finish_test(update, context):
    query = update.callback_query
    data = context.user_data
    user = query.from_user
    correct = data["correct"]
    total = len(data["questions"])
    wrong_count = total - correct
    percent = int((correct/total)*100)
    mode_name = "Genel Kültür" if data["mode"] == "gk" else "Sağlık"

    # Gruba Log Gönder
    log_msg = (f"🔔 *TEST TAMAMLANDI*\n\n"
               f"👤 *İsim:* {user.full_name}\n"
               f"📝 *Test:* {mode_name}\n"
               f"✅ *Doğru:* {correct}\n"
               f"❌ *Yanlış:* {wrong_count}\n"
               f"📊 *Başarı:* %{percent}")
    try:
        await context.bot.send_message(chat_id=LOG_GROUP_ID, text=log_msg, parse_mode="Markdown")
    except: pass

    # Katılanlar Listesi Kaydı
    if "global_users" not in context.bot_data: context.bot_data["global_users"] = []
    record = f"👤 {user.full_name} | {mode_name}: %{percent} (✅{correct}/❌{wrong_count})"
    context.bot_data["global_users"].append(record)

    # Yanlışları Göster Butonu Ekleme
    keyboard = []
    if data["wrong_list"]:
        keyboard.append([InlineKeyboardButton("❌ Yanlışlarımı Göster", callback_data="show_wrongs")])
    keyboard.append([InlineKeyboardButton("🏠 Ana Menü", callback_data="back_to_main")])

    await query.message.edit_text(
        f"✅ *{mode_name} Testi Bitti!*\n\n"
        f"📊 Doğru: {correct}\n"
        f"❌ Yanlış: {wrong_count}\n"
        f"📈 Başarı: %{percent}\n\n"
        f"📍Sonuçlarınız kayıt altına alındı.Kaydınız @Sgbotbilgi Grubuna iletildi. Yanlışlarınızı görüntülemek için butona tıklayın. ",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def show_wrong_answers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = context.user_data

    if "wrong_list" not in data or not data["wrong_list"]:
        await query.message.reply_text("Hiç yanlışınız bulunmuyor! Tebrikler.")
        return

    report = "❌ *YANLIŞ YAPTIĞINIZ SORULAR*\n━━━━━━━━━━━━━━━\n\n"
    for w in data["wrong_list"]:
        report += (f"📍 *Soru No:* {w['no']}\n"
                   f"📌 *Konu:* {w['topic']}\n"
                   f"❓ *Soru:* {w['q']}\n"
                   f"🔴 *Senin Cevabın:* {w['user_choice']}\n"
                   f"🟢 *Doğru Cevap:* {w['correct_choice']}\n"
                   f"━━━━━━━━━━━━━━━\n")

        if len(report) > 3000: # Karakter sınırı kontrolü
            await query.message.reply_text(report, parse_mode="Markdown")
            report = ""

    if report:
        await query.message.reply_text(report, parse_mode="Markdown")

async def show_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    users = context.bot_data.get("global_users", [])
    if not users:
        await query.message.reply_text("📭Henüz kimse teste katılmadı.")
        return
    list_text = "👥 *Teste Katılanlar ve Başarıları*\n━━━━━━━━━━━━━━━\n" + "\n".join(users[-20:])
    await query.message.reply_text(list_text, parse_mode="Markdown")

async def show_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mode = "gk" if "gk" in query.data else "health"
    uid = str(query.from_user.id)

    if "stats" not in context.bot_data or uid not in context.bot_data["stats"] or not context.bot_data["stats"][uid][mode]:
        await query.message.reply_text("📊 Henüz yeterli veriniz bulunmuyor.")
        return

    res_text = f"📊 *{('Genel Kültür' if mode=='gk' else 'Sağlık')} Analizi*\n\n"
    for topic, s in context.bot_data["stats"][uid][mode].items():
        p = int((s["correct"]/s["total"])*100)
        res_text += f"📌 {topic}: %{p} ({s['correct']}/{s['total']})\n"

    await query.message.reply_text(res_text, parse_mode="Markdown")

# =====================================================
# ÇALIŞTIRMA
# =====================================================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(start_test, pattern="^start_"))
app.add_handler(CallbackQueryHandler(show_status, pattern="^status_"))
app.add_handler(CallbackQueryHandler(show_users, pattern="^users$"))
app.add_handler(CallbackQueryHandler(show_wrong_answers, pattern="^show_wrongs$"))
app.add_handler(CallbackQueryHandler(start, pattern="^back_to_main$"))
app.add_handler(CallbackQueryHandler(handle_answer, pattern="^ans_"))

print("Bot aktif... Sahil Güvenlik Sistemi çalışıyor.")

# --- Render için mini web server ---
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
# --- bitti ---

app.run_polling()
# --- Render için mini web server ---
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server).start()
# --- bitti ---

