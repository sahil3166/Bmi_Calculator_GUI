from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTableView, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 744)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("caculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 225, 210, 255), stop:1 rgba(255, 255, 255, 255))")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 30, 401, 581))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border:10px solid rgb(255, 102, 0);border-style: inset;")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_inches = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_inches.setGeometry(QtCore.QRect(270, 80, 111, 41))
        self.lineEdit_inches.setStyleSheet(
            "font: 9pt \"Arial\";border:0;background-color:qlineargradient 0;border:1px solid black\n"
            "")
        self.lineEdit_inches.setObjectName("lineEdit_inches")
        self.lineEdit_feet = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_feet.setGeometry(QtCore.QRect(150, 80, 111, 41))
        self.lineEdit_feet.setWhatsThis("<html><head/><body><p><br/></p></body></html>")
        self.lineEdit_feet.setStyleSheet(
            "font: 9pt \"Arial\";border:1px solid black;background-color:qlineargradient 0")
        self.lineEdit_feet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_feet.setObjectName("lineEdit_feet")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.lineEdit_kgs = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_kgs.setGeometry(QtCore.QRect(150, 160, 113, 41))
        self.lineEdit_kgs.setStyleSheet(
            "font: 9pt \"Arial\";border:0;background-color:qlineargradient 0;border:1px solid black")
        self.lineEdit_kgs.setObjectName("lineEdit_kgs")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 101, 41))
        self.label_2.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label_2.setObjectName("label_2")
        self.pbutton_bmi = QtWidgets.QPushButton(self.frame)
        self.pbutton_bmi.setGeometry(QtCore.QRect(90, 270, 221, 51))
        self.pbutton_bmi.setStyleSheet("font: 9pt \"Arial\";border:0;border: 2px solid black")
        self.pbutton_bmi.setFlat(False)
        self.pbutton_bmi.setObjectName("pbutton_bmi")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 120, 70, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(270, 120, 70, 21))
        self.label_4.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 200, 70, 21))
        self.label_5.setStyleSheet("font: 8pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(150, 410, 101, 31))
        self.label_6.setStyleSheet("font: 10pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.label_ans = QtWidgets.QLabel(self.frame)
        self.label_ans.setGeometry(QtCore.QRect(160, 450, 91, 41))
        self.label_ans.setStyleSheet("font: 11pt \"Arial Rounded MT Bold\";border:0;background-color:qlineargradient 0")
        self.label_ans.setText("")
        self.label_ans.setObjectName("label_ans")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(261, 340, 91, 41))
        self.pushButton.setStyleSheet("font: 9pt \"Arial\";border:0;border:1px solid black;border-style: ridge")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_inches.raise_()
        self.lineEdit_feet.raise_()
        self.label.raise_()
        self.lineEdit_kgs.raise_()
        self.label_2.raise_()
        self.pbutton_bmi.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_ans.raise_()
        self.pushButton.raise_()
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 40, 321, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 8pt \"Arial\";background-color:qlineargradient 0")
        self.label_7.setObjectName("label_7")
        self.frame.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_feet, self.lineEdit_inches)
        MainWindow.setTabOrder(self.lineEdit_inches, self.lineEdit_kgs)
        MainWindow.setTabOrder(self.lineEdit_kgs, self.pbutton_bmi)
        MainWindow.setTabOrder(self.pbutton_bmi, self.pushButton)

        # t1 = self.lineEdit_kgs.text()

        # print("11")
        self.pbutton_bmi.clicked.connect(self.bmi_calculation)
        # print("ch2")

        self.pushButton.clicked.connect(self.clear_data)

    def popup_message(self, error_id):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setIcon(QMessageBox.Warning)

        if error_id == 1:
            msg.setText("Please Enter Correct Data!!")
        x_1 = msg.exec_()

    def bmi_calculation(self):

        try:

            h1 = float(self.lineEdit_feet.text())
            h2 = float(self.lineEdit_inches.text())
            h3 = h1 * 12
            h4 = h3 + h2
            h5 = h4 * 0.0254
            # print(h5)

            w = float(self.lineEdit_kgs.text())

            bmi = w / (h5) ** 2
            # print(bmi)

            """
            if(bmi>0):

                if bmi < 18.5:
                    print("Underweight",bmi)

                elif bmi >= 18.5 and bmi < 25:
                    print("Normal",bmi)

                elif bmi >= 25 and bmi < 30:
                    print("Overweight",bmi)

                else:
                    print("Obesity",bmi)

            else:
                print("enter valid details")
            """

            self.label_ans.setText(str(round(bmi, 2)))
            # print("check1")
        except:
            # print("lemon")
            self.popup_message(error_id=1)

    def clear_data(self):

        self.lineEdit_feet.clear()
        self.lineEdit_inches.clear()
        self.lineEdit_kgs.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMI Calculator"))
        self.lineEdit_inches.setToolTip(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" font-size:8pt;\">Enter inches</span></p></body></html>"))
        self.lineEdit_feet.setToolTip(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:8pt;\">Enter height</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Height</span></p></body></html>"))
        self.lineEdit_kgs.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:8pt;\">Enter weight</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Weight</span></p></body></html>"))
        self.pbutton_bmi.setText(_translate("MainWindow", "Calculate BMI"))
        self.label_3.setText(_translate("MainWindow", "(Feet)"))
        self.label_4.setText(_translate("MainWindow", "(Inches)"))
        self.label_5.setText(_translate("MainWindow", "(Kgs)"))
        self.label_6.setText(_translate("MainWindow", "Your BMI:"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-family:\'Verdana,Arial,sans-serif\'; font-size:9pt; font-weight:600; color:#000000;\">BMI Categories:</span></p><p><span style=\" font-family:\'Verdana,Arial,sans-serif\'; font-size:9pt; color:#000000;\">Underweight = &lt;18.5 </span></p><p><span style=\" font-family:\'Verdana,Arial,sans-serif\'; font-size:9pt; color:#000000;\">Normal weight = 18.5–24.9 </span></p><p><span style=\" font-family:\'Verdana,Arial,sans-serif\'; font-size:9pt; color:#000000;\">Overweight = 25–29.9 </span></p><p><span style=\" font-family:\'Verdana,Arial,sans-serif\'; font-size:9pt; color:#000000;\">Obesity = BMI of 30 or greater</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
