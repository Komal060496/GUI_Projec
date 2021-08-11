from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        # lets work on our app
        self.setWindowTitle("button Window")
        self.resize(1280, 720)


        layout = QVBoxLayout()
        

        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.addTab(QLabel("this is tab 1\n1\n1"),'TAB one')
        tabs.addTab(QLabel("this is tab 2\n2\n2"),'TAB two')
        tabs.addTab(QLabel("this is tab 3tres\n3tres\n3tres"),'TAB three')
        # tabs.addTab()
         
        layout.addWidget(tabs) 
        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app =QApplication([])
window= MainWindow()
window.show()
app.exec()
