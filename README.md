# 🎙️ StokSes — Sesli Stok Yönetim Asistanı

> Kooperatifler ve KOBİ'ler için yapay zeka destekli, sesli stok takip sistemi.

![Python](https://img.shields.io/badge/Python-3.11+-3a2b28?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-3a2b28?style=flat-square&logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_AI-2.5_Flash-3a2b28?style=flat-square&logo=google&logoColor=white)
![License](https://img.shields.io/badge/Lisans-MIT-3a2b28?style=flat-square)

---

## 🧩 Problem

Küçük işletmeler ve kooperatifler stok takibini hâlâ elle yapıyor. Kâğıt deftere yazıyorlar, WhatsApp mesajlarını kaçırıyorlar, ne zaman sipariş vereceklerini bilmiyorlar. Dijital araçlar ya çok pahalı, ya çok karmaşık, ya da öğrenmesi çok zaman alıyor.

**StokSes bu sorunu çözüyor:** Depoda yürürken telefona konuşuyorsun, sistem gerisini hallediyor.

---

## 💡 Çözüm

StokSes, kullanıcının sesli konuşmasını Gemini AI ile analiz ederek stok bilgilerini otomatik olarak kaydeden, kritik seviyeleri tespit eden ve tedarikçiye mesaj taslağı hazırlayan bir web uygulamasıdır.

```
Kullanıcı konuşur → Tarayıcı sesi metne çevirir → FastAPI backend alır
→ Gemini AI parse eder → Stok güncellenir → Tedarikçi mesajı hazır
```

---

## 🎬 Demo

**Örnek kullanım:**

> *"40 kilo un var, geçen hafta 4 kilo kullandık, domates salçası bitti, 12 şişe ayçiçek yağı kaldı"*

**Sistem ne yapıyor:**
- `un` → 40 kilo olarak kaydeder
- `un` → 4 kilo düşer (36 kilo)
- `domates salçası` → 0 olarak işaretler, kritik uyarı verir
- `ayçiçek yağı` → 12 şişe olarak kaydeder
- Tedarikçiye WhatsApp mesajı taslağı hazırlar

---

## ✨ Özellikler

| Özellik | Açıklama |
|---|---|
| 🎙️ Sesli giriş | Web Speech API ile Türkçe ses tanıma |
| 🤖 AI parse | Gemini 2.5 Flash ile doğal dil → yapılandırılmış veri |
| ➕➖ Akıllı güncelleme | "4 kilo kullandık" → stoktan otomatik düşer |
| ⚠️ Kritik uyarı | Eşik altına düşen ürünler için anlık uyarı |
| 💡 AI önerisi | Stok durumuna göre akıllı öneri üretimi |
| 📤 WhatsApp paylaşımı | Tedarikçi mesajını tek tıkla WhatsApp'a aktar |
| 📥 CSV export | Stok raporunu Excel'e aktarma |
| 📊 Dashboard | Gerçek zamanlı stok durumu ve istatistikler |

---

## 🏗️ Mimari

```
stok-ses/
├── backend/
│   ├── main.py        # FastAPI endpoints
│   ├── gemini.py      # Gemini AI entegrasyonu
│   ├── storage.py     # JSON tabanlı veri yönetimi
│   └── requirements.txt
├── frontend/
│   └── index.html     # Tek dosya SPA (Vanilla JS)
├── data/
│   └── stok.json      # Kalıcı stok verisi
└── README.md
```

**Backend:** Python + FastAPI  
**AI:** Google Gemini 2.5 Flash  
**Frontend:** Vanilla HTML/CSS/JS (framework yok)  
**Veri:** JSON dosyası (veritabanı gerektirmez)  
**Ses:** Web Speech API (tarayıcıda yerleşik, ücretsiz)

---

## 🤖 AI Nasıl Çalışıyor?

StokSes'teki AI kullanımı dekoratif değil, ürünün çekirdeği:

### 1. Doğal Dil → Yapılandırılmış Veri

```python
# Giriş (ham ses metni):
"40 kilo un var, geçen hafta 4 kilo kullandık, salça bitti"

# Gemini çıktısı (JSON):
[
  {"urun_adi": "un",    "miktar": 40, "birim": "kilo", "islem": "mutlak"},
  {"urun_adi": "un",    "miktar": 4,  "birim": "kilo", "islem": "cikar"},
  {"urun_adi": "salça", "miktar": 0,  "birim": "adet", "islem": "mutlak"}
]
```

### 2. İşlem Tipleri

| İşlem | Tetikleyen ifadeler | Etki |
|---|---|---|
| `mutlak` | "40 kilo var", "3 kutu kaldı" | Stoku bu değere eşitle |
| `cikar` | "4 kilo kullandık", "2 tane azaldı" | Mevcut stoktan düş |
| `ekle` | "10 kilo geldi", "5 kutu eklendi" | Mevcut stoğa ekle |

### 3. AI Önerileri

Stok verisine bakarak kural tabanlı + AI destekli yorumlar üretir:

- Kritik ürünler için acil uyarı
- Düşük stokta sipariş önerisi
- Yeterli stokta pozitif bildirim

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.11+
- Google Gemini API key ([buradan ücretsiz alın](https://aistudio.google.com/apikey))
- Chrome (Web Speech API için)

### Adımlar

**1. Repoyu klonla**
```bash
git clone https://github.com/msubasii/stok-ses.git
cd stok-ses
```

**2. Sanal ortam oluştur ve aktif et**
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Bağımlılıkları yükle**
```bash
pip install -r requirements.txt
```

**4. API key'ini tanımla**

`backend/` klasörünün içine `.env` adında bir dosya oluştur ve şunu yaz:
```
GEMINI_API_KEY=kendi_gemini_api_keyin
```
API key almak için: [aistudio.google.com/apikey](https://aistudio.google.com/apikey) (ücretsiz)

**5. Backend'i başlat**
```bash
cd backend
uvicorn main:app --reload
```

**6. Frontend'i aç**

`frontend/index.html` dosyasını Chrome ile çift tıklayarak aç.

---

## 📡 API Endpoints

| Method | Endpoint | Açıklama |
|---|---|---|
| `GET` | `/` | Sistem durumu |
| `POST` | `/stok/isle` | Metin parse et ve stoğu güncelle |
| `GET` | `/stok` | Tüm stok listesi |
| `GET` | `/stok/eksikler` | Kritik ürünler |
| `GET` | `/stok/tedarikci-mesaji` | Tedarikçi mesajı oluştur |

**Örnek istek:**
```bash
curl -X POST http://localhost:8000/stok/isle \
  -H "Content-Type: application/json" \
  -d '{"metin": "40 kilo un var, domates salçası bitti"}'
```

---

## 🎯 Hedef Kullanıcı

- **Kooperatifler ve küçük üreticiler**
- **Mahalle esnafı** (kasap, manav, bakkal)
- **Küçük üretim atölyeleri**
- **Catering ve yemek işletmeleri**

Bu gruplara ortak özellik: teknik bilgi yok, zaman yok, ama konuşabiliyorlar.

---

## 🔮 Gelecek Planlar

- [ ] Çoklu kullanıcı ve rol yönetimi
- [ ] Stok geçmişi ve trend analizi
- [ ] Ses komutlarıyla tedarikçi seçimi
- [ ] Mobil uygulama (PWA)
- [ ] Çoklu dil desteği

---

## 👩‍💻 Geliştirici

**Melisa Subaşı**  
YZTA 5.0 Hackathon
Google Teknoloji Akademisi

---