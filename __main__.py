import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="SimpleTextEditor"
        self.left=200 #num of pixels from left side of screen
        self.top=200  #num of pixels from top side of screen
        self.width=900
        self.height=700
        self.initUI()

    def initUI(self): 
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.textbox = QLineEdit(self)        
        self.textbox.resize(900,700)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

