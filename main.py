import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Max's Desktop App")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        button = QPushButton("Click me!")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
   window.show()
    sys.exit(app.exec())