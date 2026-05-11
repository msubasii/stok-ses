import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

async def parse_stok(metin: str):
    prompt = f"""
Sen bir stok takip asistanısın. Aşağıdaki Türkçe sesli notu analiz et ve ürünleri JSON formatında çıkar.

Sesli not: "{metin}"

Şu kurallara uy:
- Sadece JSON döndür, başka hiçbir şey yazma
- Her ürün için: urun_adi, miktar, birim alanları olsun
- Miktar sayısal olsun
- Birim: adet, kilo, litre, şişe, kutu, paket gibi olsun
- Eğer birim belirtilmemişse "adet" yaz

Örnek çıktı:
[
  {{"urun_adi": "un", "miktar": 40, "birim": "kilo"}},
  {{"urun_adi": "ayçiçek yağı", "miktar": 12, "birim": "şişe"}}
]

Sadece JSON listesi döndür:
"""
    
    response = model.generate_content(prompt)
    text = response.text.strip()
    
    # Gemini bazen ```json ``` ekliyor, temizle
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    
    urunler = json.loads(text)
    return urunler