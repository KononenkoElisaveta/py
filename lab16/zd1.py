import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def convert():
    try:
        amount = float(input_field.text())
        from_cur = from_combo.currentText()
        to_cur = to_combo.currentText()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
        data = requests.get(url, timeout=5).json()
        rate = data["rates"][to_cur]
        result = amount * rate
        result_label.setText(f"{amount} {from_cur} = {result:.2f} {to_cur}")
        result_label.setStyleSheet("color: #1565C0; font-size: 16px; font-weight: bold;")
    except:
        result_label.setText("Ошибка!")
        result_label.setStyleSheet("color: red;")
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Конвертор валют")
window.setFixedSize(400, 350)
window.setStyleSheet("background-color: #E3F2FD;")

layout = QVBoxLayout()
layout.setSpacing(15)
layout.setContentsMargins(40, 30, 40, 30)

title = QLabel("Конвертор валют")
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("font-size: 20px; font-weight: bold; color: #1565C0;")
layout.addWidget(title)

input_field = QLineEdit()
input_field.setPlaceholderText("Введите сумму")
input_field.setStyleSheet("font-size: 14px; padding: 8px; border-radius: 8px; border: 2px solid #90CAF9; background: white;")
layout.addWidget(input_field)

currencies = ["RUB", "USD", "EUR", "GBP", "CNY", "JPY"]

from_combo = QComboBox()
from_combo.addItems(currencies)
from_combo.setStyleSheet("font-size: 13px; padding: 6px; border-radius: 8px; background: white; border: 2px solid #90CAF9;")
layout.addWidget(from_combo)

arrow = QLabel(">")
arrow.setAlignment(Qt.AlignCenter)
arrow.setStyleSheet("font-size: 16px; color: #1976D2;")
layout.addWidget(arrow)

to_combo = QComboBox()
to_combo.addItems(currencies)
to_combo.setCurrentIndex(1)
to_combo.setStyleSheet("font-size: 13px; padding: 6px; border-radius: 8px; background: white; border: 2px solid #90CAF9;")
layout.addWidget(to_combo)

btn = QPushButton("Конвертировать")
btn.setStyleSheet("font-size: 14px; font-weight: bold; padding: 10px; border-radius: 8px; background: #1976D2; color: white;")
btn.setCursor(Qt.PointingHandCursor)
btn.clicked.connect(convert)
layout.addWidget(btn)

result_label = QLabel("")
result_label.setAlignment(Qt.AlignCenter)
result_label.setStyleSheet("font-size: 16px; color: #1565C0;")
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())