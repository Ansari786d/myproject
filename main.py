import time
from plyer import notification

if __name__ == "__main__":
    while True:

        notification.notify(
            title="Please drink water",
            message="Water is must for healthy body ! please drink ",
            app_icon="C:\\Users\\ansar\\pythonprogr\\harry_project//desktopnotification/icon.ico",
            timeout=12)

        time.sleep(60*60)
