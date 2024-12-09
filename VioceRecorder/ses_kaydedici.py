import sounddevice as sd
from scipy.io.wavfile import write
import os

class SesKaydedici:
    def __init__(self, ornekleme_orani=44100, dosya_adi="kayit.wav"):
        self.ornekleme_orani = ornekleme_orani
        self.dosya_adi = dosya_adi
        self.ses_verisi = None

    def kayit_baslat(self, sure):
        """
        Kaydı başlatır ve belirtilen süre boyunca ses kaydeder.

        :param sure: Kaydetme süresi (saniye)
        """
        print(f"{sure} saniye boyunca kayıt yapılıyor...")
        self.ses_verisi = sd.rec(int(sure * self.ornekleme_orani), samplerate=self.ornekleme_orani, channels=2, dtype="int16")
        sd.wait()
        print("Kayıt tamamlandı.")

    def kayit_dosyaya_yaz(self):
        """
        Kaydedilen sesi bir dosyaya yazar.
        """
        if self.ses_verisi is not None:
            write(self.dosya_adi, self.ornekleme_orani, self.ses_verisi)
            print(f"Kayıt {self.dosya_adi} dosyasına kaydedildi.")
        else:
            print("Henüz bir kayıt yapılmadı!")

def menu():
    """
    Kullanıcı menüsü
    """
    print("\nSes Kaydedici Programı")
    print("1. Ses kaydet")
    print("2. Çıkış")
    return input("Seçiminizi yapın (1-2): ")

if __name__ == "__main__":
    kaydedici = SesKaydedici()
    while True:
        secim = menu()
        if secim == "1":
            try:
                sure = int(input("Kaç saniye boyunca kayıt yapmak istiyorsunuz? "))
                kaydedici.kayit_baslat(sure)
                kaydedici.kayit_dosyaya_yaz()
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "2":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")