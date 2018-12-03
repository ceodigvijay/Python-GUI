from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import math # for square root

class Button(): # to handle button events
    def __init__(self, text, result): # takes parameter of button text and result (QLineEdit)
        self.b=QPushButton(text) # Created an button attribute which is used at line 53 and 55
        self.text=text
        self.result=result
        self.b.clicked.connect(lambda: self.handleInput()) # lambda is must
    def handleInput(self):
        if self.text=="=":
            try:
                self.result.setText(str(eval(self.result.text())))
            except SyntaxError:
                self.result.setText("Invalid Syntax Press AC")
            except ZeroDivisionError:
                self.result.setText("Zero Division Error Press AC")
            except:
                self.result.setText("Some Error Occured, Press AC")
        elif self.text=="AC":
            self.result.setText("")
        elif self.text=="C":
            self.result.setText(self.result.text()[:-1]) # remove last char
        elif self.text=="root":
            self.result.setText(str(math.sqrt(float(self.result.text()))))
            # convert the result (QLineEdit) contents to int or float and apply sqrt method the again convert it to string
        else:
            self.result.setText(self.result.text()+self.text)

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.mainApp()

    def mainApp(self):
        grid=QGridLayout()
        result=QLineEdit()

        buttons=["AC", "C", "root", "/",
                 "7", "8", "9", "+",
                 "4", "5", "6", "-",
                 "1", "2", "3", "*",
                 "0", ".", "="]
        row,column=(1,0) # because at row 0 there is QLineEdit (result named var)
        grid.addWidget(result,0,0,1,4)
        for button in buttons:
            ButtonObject = Button(button,result)
            if column>3: # if column n0.>3 then break the line /// means increment row and column set to 0
                column=0
                row+=1

            if button=="=":
                grid.addWidget(ButtonObject.b, row, column, 1, 2) # "=" Button is of width 2
            else:
                grid.addWidget(ButtonObject.b, row, column, 1, 1)
                column+=1
        self.setLayout(grid)
        self.setWindowTitle("Calculator")

        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Application()
    sys.exit(app.exec_())
