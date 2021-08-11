from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle("Radio button")
        self.resize(1280,720)
        layout = QVBoxLayout()
        male_button =QRadioButton("male")
        male_button.toggled.connect(lambda: self.show_selected(male_button))
        female_button =QRadioButton("female")
        female_button.toggled.connect(lambda: self.show_selected(female_button))
        layout.addWidget(male_button)
        layout.addWidget(female_button)
        

        self.label = QLabel("You select nothing")
        # label = QLabel("You select nothing")
        layout.addWidget(self.label)
        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget) 
    

    def show_selected(self, button):
        print(self.label.setText(button.text()))
        # print(button.text())


app =QApplication([])
window= MainWindow()
window.show()
app.exec()