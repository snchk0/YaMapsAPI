import sys
import os
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MapApp(QWidget):
    def __init__(self):
        super().__init__()

        self.dolgota = 37.620070
        self.shirota = 55.753630
        self.masshtab = 15
        self.tip_karty = "map"

        self.initUI()
        self.pokazat_kartu()

    def initUI(self):
        self.setGeometry(100, 100, 600, 450)
        self.setWindowTitle('Map API')

        self.label_karty = QLabel(self)
        self.label_karty.move(0, 0)
        self.label_karty.resize(600, 450)

    def pokazat_kartu(self):
        server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": f"{self.dolgota},{self.shirota}",
            "z": self.masshtab,
            "l": self.tip_karty,
            "size": "600,450"
        }

        try:
            response = requests.get(server, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            sys.exit(1)

        self.imya_faila = "map.png"
        with open(self.imya_faila, "wb") as file:
            file.write(response.content)

        pixmap = QPixmap(self.imya_faila)
        self.label_karty.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        
        if key == Qt.Key.Key_PageUp:
            if self.masshtab < 17:
                self.masshtab += 1
        elif key == Qt.Key.Key_PageDown:
            if self.masshtab > 0:
                self.masshtab -= 1
        else:
            shag = 360 / (2 ** self.masshtab) 
            
            if key == Qt.Key.Key_Left:
                self.dolgota -= shag
                if self.dolgota < -180:
                    self.dolgota = -180
            elif key == Qt.Key.Key_Right:
                self.dolgota += shag
                if self.dolgota > 180:
                    self.dolgota = 180
            elif key == Qt.Key.Key_Up:
                self.shirota += shag
                if self.shirota > 85:
                    self.shirota = 85
            elif key == Qt.Key.Key_Down:
                self.shirota -= shag
                if self.shirota < -85:
                    self.shirota = -85
        
        self.pokazat_kartu()

    def closeEvent(self, event):
        if os.path.exists("map.png"):
            os.remove("map.png")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapApp()
    ex.show()
    sys.exit(app.exec())
