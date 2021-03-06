from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setStyleSheet("QPushButton { margin: 10ex; }")
app.setPalette(palette)
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Bottom'))
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))


window.setLayout(layout)
window.show()
app.exec()
