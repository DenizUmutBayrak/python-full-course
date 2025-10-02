import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 350, 500, 500) #(x, y, width, height)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("photo.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry(self.width() - label.width(), #right  if 0 left    if //2
                          self.height() - label.height(), #bottom if 0 top             //2  centered middle
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()