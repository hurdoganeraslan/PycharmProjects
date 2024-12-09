import time

def geri_sayim(saniye):
    """
    Geri sayım fonksiyonu, belirtilen saniyeye kadar geri sayar.
    """
    while saniye:
        dakika, saniye_kalan = divmod(saniye, 60)
        zaman_format = '{:02d}:{:02d}'.format(dakika, saniye_kalan)
        print(zaman_format, end='\r')  # Geri sayımı ekranda aynı satırda gösterir
        time.sleep(1)  # Her saniye bekler
        saniye -= 1  # Saniyeyi bir azalt
    print("Zaman doldu!")  # Geri sayım bittiğinde mesaj

# Kullanıcıdan geri sayım süresi alalım (örneğin 5 dakikalık bir geri sayım)
dakika = int(input("Kaç dakika geri saymak istersiniz? "))
saniye = dakika * 60

geri_sayim(saniye)
