from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def window():
    app=QApplication(sys.argv) #know what OS to Run
    win=QMainWindow()
    win.setGeometry(200,200,700,700)
    win.setWindowTitle("SimpleTextEditor")
    win.show()
    sys.exit(app.exec_())

window()