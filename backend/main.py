from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gemini import parse_stok
from storage import (
    stok_guncelle,
    stok_getir,
    eksikleri_getir,
    tedarikci_mesaji_olustur
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MesajInput(BaseModel):
    metin: str

@app.get("/")
def root():
    return {"mesaj": "StokSes API çalışıyor"}

@app.post("/stok/isle")
async def stok_isle(input: MesajInput):
    urunler = await parse_stok(input.metin)

    stok_guncelle(urunler)

    return {
        "urunler": urunler,
        "stok": stok_getir()
    }

@app.get("/stok")
def stok_listesi():
    return {
        "stok": stok_getir()
    }

@app.get("/stok/eksikler")
def eksikler():
    return {
        "eksikler": eksikleri_getir()
    }

@app.get("/stok/tedarikci-mesaji")
def tedarikci_mesaji():
    mesaj = tedarikci_mesaji_olustur()

    return {
        "mesaj": mesaj
    }