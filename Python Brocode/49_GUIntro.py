# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(750, 350, 500, 500) #(x, y, width, height)
        self.setWindowIcon(QIcon("photo.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()