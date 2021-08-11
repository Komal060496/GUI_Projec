from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("checkboxes")
        self.resize(1280,720)
        layout = QVBoxLayout()


        check1 = QCheckBox("Pick up groceries ")
        check1.toggled.connect(lambda: self.something_checked(check1))
        check2 = QCheckBox("Hello everyone ")
        check2.toggled.connect(lambda: self.something_checked(check2))
         
        self.label =QLabel("you have not selected anything") 
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.checked_stuff =[]

        layout.addWidget(self.label)
        layout.addWidget(check1)
        layout.addWidget(check2)
        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget) 
    def something_checked(self,check):

        if check.isChecked() == False:
            self.checked_stuff = list(filter(lambda stuff: (stuff != check.text()),self.checked_stuff))
        else:
            self.checked_stuff.append(check.text())
        task_string =""
        for task in self.checked_stuff:
            task_string += (task+"\n") 

        self.label.setText(task_string)       
        print(self.checked_stuff)        
        # print(check.isChecked())
        # self.checked_stuff.append(check.text())


app =QApplication([])
window= MainWindow()
window.show()
app.exec()