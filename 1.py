import os
import sys
import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

SHIRINA_OKNA = 600
VISOTA_OKNA = 450

class MapApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.dolgota = "37.620070"
        self.shirota = "55.753630"
        self.masshtab = "0.002"
        self.tip_karty = "map"

        self.zagruzit_kartu()
        self.pokazat_interfey()

    def zagruzit_kartu(self):
        koordinaty = f"{self.dolgota},{self.shirota}"
        razmer_oblasti = f"{self.masshtab},{self.masshtab}"

        params = {
            "ll": koordinaty,
            "spn": razmer_oblasti,
            "l": self.tip_karty
        }

        api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(api_server, params=params)

        if not response:
            sys.exit(1)

        self.imya_faila = "temp_map.png"
        with open(self.imya_faila, "wb") as file:
            file.write(response.content)

    def pokazat_interfey(self):
        self.setGeometry(100, 100, SHIRINA_OKNA, VISOTA_OKNA)
        self.setWindowTitle('Map API')

        kartinka = QPixmap(self.imya_faila)
        
        self.label_karty = QLabel(self)
        self.label_karty.move(0, 0)
        self.label_karty.resize(SHIRINA_OKNA, VISOTA_OKNA)
        self.label_karty.setPixmap(kartinka)

    def closeEvent(self, event):
        os.remove(self.imya_faila)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapApp()
    ex.show()
    sys.exit(app.exec())