from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        # lets work on our app
        self.setWindowTitle("button Window")
        self.resize(1280, 720)
        #layout
        # hbox =QHBoxLayout()
    
        layout =QHBoxLayout()
        # layout =QVBoxLayout()
        # btn0 = QPushButton("Python 0") 
        btn1 = QPushButton('Button  1')
        # self.btn1group.addButton(btn1,1)
        # btn1.setIcon(QtGui.QIcon("pythonicom.png"))
        btn2 = QPushButton('Button 2')
        self.label= QLabel("click button 1")
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        # add action
        
        # btn0.clicked.connect(lambda x :self.label .setText("It can also done by lambda fuction"))
        btn1.clicked.connect(self.btn_1_clicked)
        btn2.clicked.connect(self.btn_2_clicked)


        layout.addWidget(self.label)


        # layout.addWidget(btn0)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

       
        self.buttongroup = QButtonGroup()

        button =QPushButton("Python")
        self.buttongroup.addButton(button,1)
        # hbox.addWidget(button)
    def btn_1_clicked(self):
        self.label.setText('You clicked button 1')
    def btn_2_clicked(self):
        self.label.setText('You clicked button 2')
    
        

app =QApplication([])
window= MainWindow()
window.show()
app.exec()