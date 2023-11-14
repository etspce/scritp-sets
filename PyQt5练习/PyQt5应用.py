import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.move(300, 300)
    w.resize(750, 350)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())