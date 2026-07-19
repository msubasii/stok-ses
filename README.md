# 🎙️ Voice Stock Assistant

> AI-powered voice-based stock tracking system for cooperatives and small businesses.

[![Python](https://img.shields.io/badge/Python-3.11+-3a2b28?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136-3a2b28?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/Gemini_AI-2.5_Flash-3a2b28?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-3a2b28?style=flat-square)](#)

---

## 🧩 Problem

Small businesses and cooperatives still track inventory manually — writing in paper notebooks, missing WhatsApp messages, not knowing when to reorder. Digital tools are either too expensive, too complex, or take too long to learn.

**Voice Stock Assistant solves this:** talk to your phone while walking through the warehouse, and the system takes care of the rest.

---

## 💡 Solution

Voice Stock Assistant analyzes the user's spoken input using Gemini AI, automatically logs stock data, detects critical levels, and drafts a supplier message — all from natural speech.

```
User speaks → Browser converts speech to text → FastAPI backend receives it
→ Gemini AI parses it → Stock is updated → Supplier message is ready
```

---

## 🎬 Demo

**Example input:**
> *"We have 40 kilos of flour, used 4 kilos last week, tomato paste ran out, 12 bottles of sunflower oil left"*

**What the system does:**
- `flour` → logs as 40 kg
- `flour` → subtracts 4 kg (36 kg remaining)
- `tomato paste` → marks as 0, raises critical alert
- `sunflower oil` → logs as 12 bottles
- Prepares a draft WhatsApp message to the supplier

---

## ✨ Features

| Feature               | Description                                             |
| ---------------------- | -------------------------------------------------------- |
| 🎙️ Voice input          | Speech recognition via Web Speech API                    |
| 🤖 AI parsing            | Gemini 2.5 Flash converts natural language → structured data |
| ➕➖ Smart updates        | "used 4 kilos" → automatically subtracted from stock     |
| ⚠️ Critical alerts       | Instant warning when items drop below threshold          |
| 💡 AI suggestions        | Smart recommendations based on stock status               |
| 📤 WhatsApp sharing       | Send supplier message directly to WhatsApp in one click  |
| 📥 CSV export            | Export stock report to Excel                              |
| 📊 Dashboard             | Real-time stock overview and statistics                   |

---

## 🏗️ Architecture

```
voice-stock-assistant/
├── backend/
│   ├── main.py        # FastAPI endpoints
│   ├── gemini.py      # Gemini AI integration
│   ├── storage.py     # JSON-based data management
│   └── requirements.txt
├── frontend/
│   └── index.html     # Single-file SPA (Vanilla JS)
├── data/
│   └── stok.json      # Persistent stock data
└── README.md
```

**Backend:** Python + FastAPI
**AI:** Google Gemini 2.5 Flash
**Frontend:** Vanilla HTML/CSS/JS (no framework)
**Data:** JSON file (no database required)
**Speech:** Web Speech API (built into the browser, free)

---

## 🤖 How the AI Works

AI isn't decorative here — it's the core of the product.

### 1. Natural Language → Structured Data

```
# Input (raw speech transcript):
"We have 40 kg of flour, used 4 kg last week, tomato paste is out"

# Gemini output (JSON):
[
  {"urun_adi": "un",    "miktar": 40, "birim": "kilo", "islem": "mutlak"},
  {"urun_adi": "un",    "miktar": 4,  "birim": "kilo", "islem": "cikar"},
  {"urun_adi": "salça", "miktar": 0,  "birim": "adet", "islem": "mutlak"}
]
```

### 2. Action Types

| Action (`islem`) | Trigger phrases                        | Effect                     |
| ----------------- | ---------------------------------------- | --------------------------- |
| `mutlak`           | "40 kg available", "3 boxes left"       | Sets stock to this value    |
| `cikar`             | "used 4 kg", "2 units gone"             | Subtracts from current stock|
| `ekle`              | "10 kg arrived", "5 boxes added"        | Adds to current stock       |

### 3. AI Suggestions

Generates rule-based + AI-assisted recommendations based on stock data:
- Urgent alerts for critical items
- Reorder suggestions for low stock
- Positive confirmation for healthy stock levels

---

## 🚀 Setup

### Requirements

- Python 3.11+
- Google Gemini API key ([get one for free here](https://aistudio.google.com/apikey))
- Chrome (required for Web Speech API)

### Steps

**1. Clone the repo**
```
git clone https://github.com/msubasii/voice-stock-assistant.git
cd voice-stock-assistant
```

**2. Create and activate a virtual environment**
```
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

**4. Set your API key**

Create a file named `.env` inside the `backend/` folder:
```
GEMINI_API_KEY=your_gemini_api_key
```
Get a free API key at: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

**5. Start the backend**
```
cd backend
uvicorn main:app --reload
```

**6. Open the frontend**

Double-click `frontend/index.html` to open it in Chrome.

---

## 📡 API Endpoints

| Method | Endpoint                 | Description                       |
| ------ | ------------------------- | ----------------------------------- |
| `GET`  | `/`                        | System status                       |
| `POST` | `/stok/isle`               | Parse text and update stock         |
| `GET`  | `/stok`                    | Full stock list                     |
| `GET`  | `/stok/eksikler`           | Critical items                      |
| `GET`  | `/stok/tedarikci-mesaji`   | Generate supplier message           |

**Example request:**
```
curl -X POST http://localhost:8000/stok/isle \
  -H "Content-Type: application/json" \
  -d '{"metin": "40 kilo un var, domates salçası bitti"}'
```

---

## 🎯 Target Users

- **Cooperatives and small producers**
- **Local shops** (butchers, greengrocers, corner stores)
- **Small production workshops**
- **Catering and food businesses**

Common thread: no technical background, no time to spare, but they can talk.

---

## 🔮 Future Plans

- [ ] Multi-user and role management
- [ ] Stock history and trend analysis
- [ ] Voice-based supplier selection
- [ ] Mobile app (PWA)
- [ ] Multi-language support

---

## 👩‍💻 Developer

**Melisa Subasi**
YZTA 5.0 Hackathon
Google Technology Academy
