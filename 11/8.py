import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(250, 150)
        self.setWindowTitle("Кликер")
        
        button_1 = QPushButton("Нажми меня", self)
        button_2 = QPushButton("Сбросить", self)
        self.lcd = QLCDNumber(self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        self.setLayout(vbox)

        self.counter = 0
        button_1.clicked.connect(self.button_was_clicked)
        button_2.clicked.connect(self.button_was_clicked)


    def button_was_clicked(self):
        sender = self.sender()
        
        if sender.text() == 'Нажми меня':
            self.counter += 1
        elif sender.text() == 'Сбросить':
            self.counter = 0
            
        self.lcd.display(self.counter)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_1:
            self.counter += 1
        elif event.key() == Qt.Key_2:
            self.counter -= 1
            
        self.lcd.display(self.counter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
