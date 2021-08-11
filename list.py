from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        # lets work on our app
        self.setWindowTitle("list")
        self.resize(1280, 720)

        layout = QVBoxLayout()
        list1 = QListWidget()
        
        list1.addItems(["komal",'singh', 'priya','singh'])
        list1.currentItemChanged.connect(lambda x: print(x.text()))
        layout.addWidget(list1)


        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





app =QApplication([])
window= MainWindow()
window.show()
app.exec()        