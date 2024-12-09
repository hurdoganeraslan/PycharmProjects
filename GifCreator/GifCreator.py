from PIL import Image


def gif_olustur(dosya_listesi, cikis_dosyasi, gecikme=100, dongu=0):
    """
    Birden fazla görüntüyü birleştirerek animasyonlu bir GIF oluşturur.

    :param dosya_listesi: GIF'te kullanılacak görüntü dosyalarının listesi
    :param cikis_dosyasi: Oluşturulan GIF dosyasının adı
    :param gecikme: Her kare arasındaki gecikme süresi (milisaniye)
    :param dongu: GIF'in tekrarlanma sayısı (0 sonsuz döngü için)
    """
    # Görüntüleri yükle
    img_listesi = [Image.open(dosya) for dosya in dosya_listesi]

    # İlk görüntüyü al ve diğerlerini ekleyerek GIF oluştur
    img_listesi[0].save(
        cikis_dosyasi,
        save_all=True,
        append_images=img_listesi[1:],
        duration=gecikme,
        loop=dongu,
    )
    print(f"{cikis_dosyasi} başarıyla oluşturuldu!")


# Örnek kullanım
if __name__ == "__main__":
    dosyalar = [
        "at1.jpg",  # Kullanılacak görüntü dosyalarını buraya ekleyin
        "at2.jpg",
        "at3.jpg",
        "at4.jpg",
        "at5.jpg",
    ]
    gif_olustur(dosyalar, "cikis.gif", gecikme=500, dongu=0)
