from google import genai
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def parse_stok(metin: str):
    prompt = f"""
Sen bir stok takip asistanısın. Aşağıdaki Türkçe sesli notu analiz et ve ürünleri JSON formatında çıkar.

Sesli not: "{metin}"

Şu kurallara uy:
- Sadece JSON döndür, başka hiçbir şey yazma
- Her ürün için: urun_adi, miktar, birim, islem alanları olsun
- islem 3 değer alabilir:
  * "mutlak" → mevcut stoku bu değere eşitle ("40 kilo un var", "3 kutu kaldı")
  * "cikar" → mevcut stoktan düş ("4 kilo kullandık", "2 tane azaldı", "5 tane çıktı")
  * "ekle" → mevcut stoka ekle ("10 kilo daha geldi", "5 kutu eklendi", "yeni sipariş geldi")
- Miktar her zaman pozitif sayı olsun
- Birim: adet, kilo, litre, şişe, kutu, paket
- Eğer birim belirtilmemişse "adet" yaz

Örnek:
"40 kilo un var, geçen hafta 4 kilo kullandık, 10 şişe yağ geldi"
[
  {{"urun_adi": "un", "miktar": 40, "birim": "kilo", "islem": "mutlak"}},
  {{"urun_adi": "un", "miktar": 4, "birim": "kilo", "islem": "cikar"}},
  {{"urun_adi": "yağ", "miktar": 10, "birim": "şişe", "islem": "ekle"}}
]

Sadece JSON listesi döndür:
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    
    text = response.text.strip()
    
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()
    
    urunler = json.loads(text)
    return urunler