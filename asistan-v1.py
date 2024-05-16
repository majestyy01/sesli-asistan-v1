import speech_recognition as sr
import requests
import webbrowser
import wikipedia
import datetime
"""
WoxicDEV - 2024 
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
medium : mrtalikyaa
İlk sürüm olduğundan arayüz eklemedim ikinci sürümde yeni seçimler ile beraber getireceğim.
Aklınıza eklenebilecek herhangi bir şey gelirse belirttiğim sosyal medya hesaplarından bana ulaşabilirsiniz.
Kütüphane bilgisi ReadMe dosyasında belirtilmiştir.

"""
def komut_al_sesli():
  """
  Mikrofon üzerinden sesli komut alma ve metine dönüştürme bölümü
  """
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Sesli komut dinleniyor...")
    audio = r.listen(source)

  try:
    # Sesli komutu metne dönüştür
    komut = r.recognize_google(audio)
    print(f"Anlaşılan Komut: {komut}")
  except sr.UnknownValueError:
    print("Sesli komut anlaşılamadı.")
  except sr.RequestError as e:
    print("Sesli komut işlenirken bir hata oluştu: {e}")
  return komut

  
def komut_al_metin():
    #metinle komut alma
  komut = input("Komut giriniz: ")
  return komut

def komutu_cevapla(komut):
    #cevaplama kısmı
  if komut.lower() == "zaman":
    simdiki_zaman = datetime.datetime.now()
    saat = simdiki_zaman.strftime("%H:%M")
    print(f"Saat: {saat}")
  elif komut.lower() == "hava":
    hava_durumu = webbrowser.open_new_tab("https://www.accuweather.com/")
    print("Hava durumunu kontrol etmek için AccuWeather sitesi açılıyor.")
  elif komut.lower().startswith("ara"):
    aramak_icerik = komut[4:].strip()
    bilgi_kaynagi = "wikipedia"  # Bilgi Kaynağı Ayarlama Kısmı
    if bilgi_kaynagi == "wikipedia":
      wikipedia.set_lang("tr")
      sonuc = wikipedia.summary(aramak_icerik, sentences=1)
      print(f"{aramak_icerik} hakkındaki bilgi: {sonuc}")
    elif bilgi_kaynagi == "google":
      url = f"https://www.google.com/search?q={aramak_icerik}" #üst kısımndan bilgi kaynağını değiştirirseniz  googledan arama yapar.
      response = requests.get(url)
      if response.status_code == 200:
        print(f"{aramak_icerik} hakkındaki bilgi şunlardır: {response.text}")
      else:
        print(f"Arama başarısız oldu. Hata kodunuz: {response.status_code}")
    else:
      print(f"Geçersiz bilgi kaynağı: {bilgi_kaynagi}")
  else:
    print("Komutunuzu anlamadım lütfen tekrar söyleyin")


while True:
  # Hangi komut seçeneğini seçeceksin bölümü
  secim = input("Komut nasıl gireceksiniz? (sesli arama/metinsel arama): ")

  if secim.lower() == "sesli arama":  #sesli komut seçeneği
    komut = komut_al_sesli()
  elif secim.lower() == "metinsel arama": #metinsel komut seçeneği
    komut = komut_al_metin()
  else:
    print("Geçersiz seçim. Lütfen 'sesli arama' veya 'metinsel arama' yazın.") #geçersiz komut kısmı.
    continue

  komutu_cevapla(komut)

