import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO

def get_cat():
    try:
        btn.setText("Загружаю...")
        btn.setEnabled(False)
        QApplication.processEvents()

        response = requests.get("https://api.thecatapi.com/v1/images/search", timeout=5)
        url = response.json()[0]["url"]

        img_data = requests.get(url, timeout=5).content
        pixmap = QPixmap()
        pixmap.loadFromData(BytesIO(img_data).read())

        pixmap = pixmap.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        tip_label.setText("Мяу! 🐾")
    except:
        tip_label.setText("Ошибка, котик убежал 😿")
    finally:
        btn.setText("🐱 Новый котик!")
        btn.setEnabled(True)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Котики 🐱")
window.setFixedSize(420, 520)
window.setStyleSheet("background-color: #E3F2FD;")

layout = QVBoxLayout()
layout.setSpacing(15)
layout.setContentsMargins(30, 20, 30, 20)

title = QLabel("🐱 Котик дня")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1565C0;")
layout.addWidget(title)

image_label = QLabel()
image_label.setAlignment(Qt.AlignCenter)
image_label.setFixedSize(350, 350)
image_label.setStyleSheet("background: white; border-radius: 12px; border: 2px solid #90CAF9;")
image_label.setText("Нажми кнопку!")
image_label.setStyleSheet("background: white; border-radius: 12px; border: 2px solid #90CAF9; font-size: 14px; color: #90CAF9;")
layout.addWidget(image_label, alignment=Qt.AlignCenter)

tip_label = QLabel("")
tip_label.setAlignment(Qt.AlignCenter)
tip_label.setStyleSheet("font-size: 14px; color: #1976D2;")
layout.addWidget(tip_label)

btn = QPushButton("🐱 Новый котик!")
btn.setStyleSheet("font-size: 15px; font-weight: bold; padding: 12px; border-radius: 8px; background: #1976D2; color: white;")
btn.setCursor(Qt.PointingHandCursor)
btn.clicked.connect(get_cat)
layout.addWidget(btn)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())