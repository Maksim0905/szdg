import sys
import random
from PyQt6 import QtWidgets, QtGui
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
        color = QColor(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(x, y, diameter, diameter)


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Circles")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.pushButton = QtWidgets.QPushButton("Добавить круг")
        self.layout.addWidget(self.pushButton)

        self.canvas = CircleWidget(self)
        self.layout.addWidget(self.canvas)

        self.pushButton.clicked.connect(self.canvas.add_circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
