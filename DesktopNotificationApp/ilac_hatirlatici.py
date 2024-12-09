from plyer import notification
import schedule
import time

def bildirim_gonder(baslik, mesaj):
    notification.notify(
        title=baslik,
        message=mesaj,
        app_name="İlaç Hatırlatma Uygulaması",
        timeout=10
    )

def ilac_hatirlatici():
    bildirim_gonder("İlaç Zamanı!", "Şimdi ilacınızı içme zamanı. Lütfen unutmayın!")

def planlama():
    schedule.every().day.at("09:00").do(ilac_hatirlatici)
    schedule.every().day.at("13:00").do(ilac_hatirlatici)
    schedule.every().day.at("19:00").do(ilac_hatirlatici)
    print("İlaç hatırlatıcı uygulaması çalışıyor.")

planlama()

while True:
    schedule.run_pending()
    time.sleep(1)

