from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Introduction to pyqt5 ")
        self.resize(500,600)
        label= QLabel("Hell I am a label")
        font = label.font()
        font.setPointSize(39)
        label.setFont(font)
        self.setCentralWidget(label)

app=QApplication([])
window =MyMainWindow()
window.show()
app.exec()
          