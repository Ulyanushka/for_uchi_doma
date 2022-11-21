import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        self.setWindowTitle("Кликер")
        button = QPushButton("Нажми меня!", self)
        button.setGeometry(100, 100, 100, 23)

        self.counter = 1 
        button.clicked.connect(self.button_was_clicked)


    def button_was_clicked(self):
        print(self.counter)
        self.counter += 1


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
