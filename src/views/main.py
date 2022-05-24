from PyQt5 import QtCore, QtGui, QtWidgets
        
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(500, 700)
                MainWindow.setMaximumSize(QtCore.QSize(500, 700))
                MainWindow.setStyleSheet("background-color: #000000;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.one = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
                self.one.setGeometry(QtCore.QRect(30, 500, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.one.setFont(font)
                self.one.setStyleSheet("QPushButton#one{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#one:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.one.setObjectName("one")
                self.six = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
                self.six.setGeometry(QtCore.QRect(270, 410, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.six.setFont(font)
                self.six.setStyleSheet("QPushButton#six{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#six:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.six.setObjectName("six")
                self.div = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
                self.div.setGeometry(QtCore.QRect(150, 230, 93, 71))
                self.div.setStyleSheet("QPushButton#div{\n"
"    image: url(:/data/res/divide.png);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#div:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.div.setText("")
                self.div.setObjectName("div")
                self.five = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
                self.five.setGeometry(QtCore.QRect(150, 410, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.five.setFont(font)
                self.five.setStyleSheet("QPushButton#five{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#five:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.five.setObjectName("five")
                self.clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
                self.clear.setGeometry(QtCore.QRect(30, 230, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.clear.setFont(font)
                self.clear.setStatusTip("")
                self.clear.setStyleSheet("QPushButton#clear{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#clear:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.clear.setObjectName("clear")
                self.two = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
                self.two.setGeometry(QtCore.QRect(150, 500, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.two.setFont(font)
                self.two.setStyleSheet("QPushButton#two{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#two:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.two.setObjectName("two")
                self.four = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
                self.four.setGeometry(QtCore.QRect(30, 410, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.four.setFont(font)
                self.four.setStyleSheet("QPushButton#four{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#four:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.four.setObjectName("four")
                self.three = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
                self.three.setGeometry(QtCore.QRect(270, 500, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.three.setFont(font)
                self.three.setStyleSheet("QPushButton#three{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#three:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.three.setObjectName("three")
                self.zero = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
                self.zero.setGeometry(QtCore.QRect(150, 590, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.zero.setFont(font)
                self.zero.setStyleSheet("QPushButton#zero{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#zero:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.zero.setObjectName("zero")
                self.equals = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.ans())
                self.equals.setGeometry(QtCore.QRect(385, 490, 101, 181))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.equals.setFont(font)
                self.equals.setStyleSheet("QPushButton#equals {\n"
"    background-color: #8E05C2;\n"
"    color: #000000;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#equals:pressed {\n"
"    color: #8E05C2;\n"
"    background-color: #000000;\n"
"}")
                self.equals.setObjectName("equals")
                self.mod = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
                self.mod.setGeometry(QtCore.QRect(30, 590, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.mod.setFont(font)
                self.mod.setStyleSheet("QPushButton#mod{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#mod:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.mod.setObjectName("mod")
                self.deci = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
                self.deci.setGeometry(QtCore.QRect(270, 590, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.deci.setFont(font)
                self.deci.setStyleSheet("QPushButton#deci{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#deci:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.deci.setObjectName("deci")
                self.mul = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
                self.mul.setGeometry(QtCore.QRect(270, 230, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.mul.setFont(font)
                self.mul.setStyleSheet("QPushButton#mul{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#mul:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.mul.setObjectName("mul")
                self.delete_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
                self.delete_2.setGeometry(QtCore.QRect(390, 230, 93, 71))
                self.delete_2.setStyleSheet("QPushButton#delete_2{\n"
"    image: url(:/data/res/backspace-arrow.png);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#delete_2:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.delete_2.setText("")
                self.delete_2.setObjectName("delete_2")
                self.add = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
                self.add.setGeometry(QtCore.QRect(390, 410, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.add.setFont(font)
                self.add.setStyleSheet("QPushButton#add{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#add:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.add.setObjectName("add")
                self.seven = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
                self.seven.setGeometry(QtCore.QRect(30, 320, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.seven.setFont(font)
                self.seven.setStyleSheet("QPushButton#seven{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#seven:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.seven.setObjectName("seven")
                self.nine = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
                self.nine.setGeometry(QtCore.QRect(270, 320, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.nine.setFont(font)
                self.nine.setStyleSheet("QPushButton#nine{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#nine:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.nine.setObjectName("nine")
                self.sub = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
                self.sub.setGeometry(QtCore.QRect(390, 320, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.sub.setFont(font)
                self.sub.setStyleSheet("QPushButton#sub{\n"
"    color: #8E05C2;    \n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#sub:pressed{\n"
"    background-color: #EEEEEE;    \n"
"}")
                self.sub.setObjectName("sub")
                self.eight = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
                self.eight.setGeometry(QtCore.QRect(150, 320, 93, 71))
                font = QtGui.QFont()
                font.setPointSize(40)
                self.eight.setFont(font)
                self.eight.setStyleSheet("QPushButton#eight{\n"
"    color: #8E05C2;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#eight:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.eight.setObjectName("eight")
                self.screen = QtWidgets.QLineEdit(self.centralwidget)
                self.screen.setGeometry(QtCore.QRect(20, 90, 470, 121))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.screen.setFont(font)
                self.screen.setStyleSheet("QLineEdit#screen{\n"
"    border: 5px solid #8E05C2;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    color: #8E05C2;\n"
"}")
                self.screen.setText("")
                self.screen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.screen.setObjectName("screen")
                self.info = QtWidgets.QPushButton(self.centralwidget)
                self.info.setGeometry(QtCore.QRect(430, 20, 50, 50))
                self.info.setStyleSheet("QPushButton#info{\n"
"    image: url(:/data/res/information.png);\n"
"}\n"
"QPushButton#info:pressed{\n"
"    background-color: #EEEEEE;\n"
"}")
                self.info.setText("")
                self.info.setObjectName("info")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def ans(self):
                try:
                        data = self.screen.text()
                        answer = eval(data)
                        self.screen.setText(str(answer))
                except:
                        self.screen.setText("ERROR")

        def remove_it(self):
                self.screen.setText(self.screen.text()[:-1])

        def dot_it(self):
                screen1 = self.screen.text()

                if screen1[-1] == ".":
                        pass
                else:
                        self.screen.setText(f'{screen1}.')

        def press_it(self, pressed):
                if pressed == 'C':
                        self.screen.setText("0")
                else:
                        if self.screen.text() == "0":
                                self.screen.setText("")
                        self.screen.setText(f"{self.screen.text()}{pressed}")

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Kalculator"))
                self.one.setText(_translate("MainWindow", "1"))
                self.one.setShortcut(_translate("MainWindow", "1"))
                self.six.setText(_translate("MainWindow", "6"))
                self.six.setShortcut(_translate("MainWindow", "6"))
                self.div.setShortcut(_translate("MainWindow", "/"))
                self.five.setText(_translate("MainWindow", "5"))
                self.five.setShortcut(_translate("MainWindow", "5"))
                self.clear.setText(_translate("MainWindow", "C"))
                self.clear.setShortcut(_translate("MainWindow", "Del"))
                self.two.setText(_translate("MainWindow", "2"))
                self.two.setShortcut(_translate("MainWindow", "2"))
                self.four.setText(_translate("MainWindow", "4"))
                self.four.setShortcut(_translate("MainWindow", "4"))
                self.three.setText(_translate("MainWindow", "3"))
                self.three.setShortcut(_translate("MainWindow", "3"))
                self.zero.setText(_translate("MainWindow", "0"))
                self.zero.setShortcut(_translate("MainWindow", "0"))
                self.equals.setText(_translate("MainWindow", "="))
                self.equals.setShortcut(_translate("MainWindow", "Enter"))
                self.mod.setText(_translate("MainWindow", "%"))
                self.deci.setText(_translate("MainWindow", "."))
                self.deci.setShortcut(_translate("MainWindow", "."))
                self.mul.setText(_translate("MainWindow", "X"))
                self.mul.setShortcut(_translate("MainWindow", "*"))
                self.delete_2.setShortcut(_translate("MainWindow", "Backspace"))
                self.add.setText(_translate("MainWindow", "+"))
                self.add.setShortcut(_translate("MainWindow", "+"))
                self.seven.setText(_translate("MainWindow", "7"))
                self.seven.setShortcut(_translate("MainWindow", "7"))
                self.nine.setText(_translate("MainWindow", "9"))
                self.nine.setShortcut(_translate("MainWindow", "9"))
                self.sub.setText(_translate("MainWindow", "-"))
                self.sub.setShortcut(_translate("MainWindow", "-"))
                self.eight.setText(_translate("MainWindow", "8"))
                self.eight.setShortcut(_translate("MainWindow", "8"))
                self.info.setShortcut(_translate("MainWindow", "Ctrl+I"))
                

                

import data


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
