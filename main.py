import sys
import random
from PyQt6 import QtWidgets, uic, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor("yellow"))
        painter.setPen(Qt.PenStyle.NoPen)

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        # Создаём виджет для рисования и добавляем его в layout
        self.canvas = CircleWidget(self)
        self.verticalLayout.addWidget(self.canvas)

        # Подключаем кнопку
        self.pushButton.clicked.connect(self.canvas.add_circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
