from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Main():
    def __init__(self):
        super().__init__()
        self.FormPassword()
    def FormPassword():
        print('Форма для паролей')

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()