import pyqrcode

# Kullanıcıdan URL al
url = input("Enter URL to generate QR code: ")

# QR kodu oluştur (UTF-8 encoding ile)
qr_code = pyqrcode.create(url, encoding='utf-8')

# QR kodunu SVG dosyası olarak kaydet
qr_code.svg('qrcode.svg', scale=5)

print("QR kodu başarıyla oluşturuldu ve 'qrcode.svg' olarak kaydedildi!")