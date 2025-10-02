#PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 350, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #241c4f;"
                            "background-color: #f0f250;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #AlignTop = Vertically Top / AlignBottom = Vertically Bottom / AlignVCenter = Vertically Center
        #AlignRight = Horizontally Right / AlignHCenter = Horizontally Center / AlignLeft

       # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) We can combine two flag with |
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
