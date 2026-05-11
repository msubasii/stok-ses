import json
import os

STOK_DOSYA = "../data/stok.json"

def stok_getir():
    if not os.path.exists(STOK_DOSYA):
        return {}
    with open(STOK_DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

def stok_guncelle(urunler: list):
    stok = stok_getir()
    for urun in urunler:
        ad = urun["urun_adi"].lower().strip()
        stok[ad] = {
            "urun_adi": urun["urun_adi"],
            "miktar": urun["miktar"],
            "birim": urun["birim"]
        }
    with open(STOK_DOSYA, "w", encoding="utf-8") as f:
        json.dump(stok, f, ensure_ascii=False, indent=2)

def eksikleri_getir():
    stok = stok_getir()
    eksikler = []
    for ad, bilgi in stok.items():
        if bilgi["miktar"] <= 5:
            eksikler.append(bilgi)
    return eksikler

def tedarikci_mesaji_olustur():
    eksikler = eksikleri_getir()
    if not eksikler:
        return "Kritik stok durumu yok, tüm ürünler yeterli."
    
    mesaj = "Merhaba,\n\nAşağıdaki ürünleri acilen sipariş etmemiz gerekmektedir:\n\n"
    for urun in eksikler:
        mesaj += f"- {urun['urun_adi']}: {urun['miktar']} {urun['birim']} (kritik seviye)\n"
    mesaj += "\nEn kısa sürede dönüşünüzü bekliyoruz.\nSaygılarımızla"
    
    return mesaj