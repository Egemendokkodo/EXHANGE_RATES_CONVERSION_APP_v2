from PyQt5 import QtCore, QtGui, QtWidgets
#pip install pyqt5 ve pyqt5-tools
from datetime import datetime
#pip install datetime
import requests
#pip install requests
import json
import webbrowser



class Ui_MainWindow(object):
    def bbcac(self):
        webbrowser.open("https://www.bbc.com/news/business/economy")
    def cnbcac(self):
        webbrowser.open("https://www.cnbc.com/economy/")
    def nytimesac(self):
        webbrowser.open("https://www.nytimes.com/section/business/economy")





    def api(self):
        self.api_url = "https://v6.exchangerate-api.com/v6/9883f350adc2bfedfb32f568/latest/"
        self.base = self.base_combobox.currentText()
        self.to = self.to_combobox.currentText()
        self.amount = int(self.amount_money_lineedit.text())
        self.result = requests.get(self.api_url + self.base)
        self.result = json.loads(self.result.text)

        for i in range(1,3):
                self.sonuclabel1.setText(
                        "1 {0} = {1} {2}".format(self.base, self.result['conversion_rates'][self.to], self.to))
                self.sonuclabel2.setText(
                        "{0} {1} ={2} {3}".format(self.amount, self.base,
                                                self.amount * self.result['conversion_rates'][self.to],
                                                self.to))

        self.frame_9.setStyleSheet("#frame_9{\n"
                                   "background-color: white;\n"
                                   "border-radius:20px;\n"
                                   "border:1px solid gray;}")






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 607)
        MainWindow.setStyleSheet("\n"
"#MainWindow{\n"
"background-color:#e0eee0;\n"
"\n"
"border:2px solid blue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.convertbtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.convertbtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/exchange-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.convertbtn.setIcon(icon)
        self.convertbtn.setObjectName("convertbtn")
        self.horizontalLayout_2.addWidget(self.convertbtn)
        self.newsbtn = QtWidgets.QPushButton(self.frame_8)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/news-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newsbtn.setIcon(icon1)
        self.newsbtn.setObjectName("newsbtn")
        self.horizontalLayout_2.addWidget(self.newsbtn)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.datetimelabel = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.datetimelabel.setFont(font)
        self.datetimelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datetimelabel.setObjectName("datetimelabel")
        self.verticalLayout_3.addWidget(self.datetimelabel, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.page1)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_13 = QtWidgets.QFrame(self.frame_7)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.base_combobox = QtWidgets.QComboBox(self.frame_11)
        self.base_combobox.setMinimumSize(QtCore.QSize(200, 0))
        self.base_combobox.setObjectName("base_combobox")
        self.base_combobox.addItem("")
        self.base_combobox.setItemText(0, "")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")
        self.base_combobox.addItem("")
        self.horizontalLayout_5.addWidget(self.base_combobox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.to_combobox = QtWidgets.QComboBox(self.frame_10)
        self.to_combobox.setMinimumSize(QtCore.QSize(200, 0))
        self.to_combobox.setObjectName("to_combobox")
        self.to_combobox.addItem("")
        self.to_combobox.setItemText(0, "")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")
        self.to_combobox.addItem("")
        self.horizontalLayout_6.addWidget(self.to_combobox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_7)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.amount_money_lineedit = QtWidgets.QLineEdit(self.frame_12)
        self.amount_money_lineedit.setMinimumSize(QtCore.QSize(140, 35))
        self.amount_money_lineedit.setStyleSheet("border:2px solid blue;\n"
"border-radius:15px;")
        self.amount_money_lineedit.setObjectName("amount_money_lineedit")
        self.verticalLayout_8.addWidget(self.amount_money_lineedit, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.convertbtn_2 = QtWidgets.QPushButton(self.frame_12)
        self.convertbtn_2.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.convertbtn_2.setFont(font)
        self.convertbtn_2.setStyleSheet("\n"
"#convertbtn_2{\n"
"border:2px solid blue;\n"
"border-radius:10px;\n"
"}\n"
"#convertbtn_2:hover{\n"
"    background-color:#cae1ff;\n"
"}")
        self.convertbtn_2.setObjectName("convertbtn_2")
        self.verticalLayout_8.addWidget(self.convertbtn_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_9 = QtWidgets.QFrame(self.frame_12)
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.sonuclabel1 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sonuclabel1.setFont(font)
        self.sonuclabel1.setText("")
        self.sonuclabel1.setObjectName("sonuclabel1")
        self.verticalLayout_9.addWidget(self.sonuclabel1, 0, QtCore.Qt.AlignHCenter)
        self.sonuclabel2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sonuclabel2.setFont(font)
        self.sonuclabel2.setText("")
        self.sonuclabel2.setObjectName("sonuclabel2")
        self.verticalLayout_9.addWidget(self.sonuclabel2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.verticalLayout_6.addWidget(self.frame_12, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_3 = QtWidgets.QFrame(self.page2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.bbcbtn = QtWidgets.QPushButton(self.frame_3)
        self.bbcbtn.setMinimumSize(QtCore.QSize(100, 80))
        self.bbcbtn.setStyleSheet("#bbcbtn {\n"
"    box-shadow: 3px 4px 0px 0px #899599;\n"
"    background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);\n"
"    background-color:#ededed;\n"
"    border-radius:15px;\n"
"    border:1px solid #d6bcd6;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#3a8a9e;\n"
"    font-family:Arial;\n"
"    font-size:17px;\n"
"    padding:7px 25px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #e1e2ed;\n"
"}\n"
"#bbcbtn:hover {\n"
"    background:linear-gradient(to bottom, #bab1ba 5%, #ededed 100%);\n"
"    background-color:#bab1ba;\n"
"}\n"
"#bbcbtn:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/bbc-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bbcbtn.setIcon(icon2)
        self.bbcbtn.setIconSize(QtCore.QSize(50, 50))
        self.bbcbtn.setObjectName("bbcbtn")
        self.verticalLayout_11.addWidget(self.bbcbtn, 0, QtCore.Qt.AlignHCenter)
        self.cnbcbtn = QtWidgets.QPushButton(self.frame_3)
        self.cnbcbtn.setMinimumSize(QtCore.QSize(100, 80))
        self.cnbcbtn.setStyleSheet("#cnbcbtn {\n"
"    box-shadow: 3px 4px 0px 0px #899599;\n"
"    background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);\n"
"    background-color:#ededed;\n"
"    border-radius:15px;\n"
"    border:1px solid #d6bcd6;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#3a8a9e;\n"
"    font-family:Arial;\n"
"    font-size:17px;\n"
"    padding:7px 25px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #e1e2ed;\n"
"}\n"
"#cnbcbtn:hover {\n"
"    background:linear-gradient(to bottom, #bab1ba 5%, #ededed 100%);\n"
"    background-color:#bab1ba;\n"
"}\n"
"#cnbcbtn:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/cnbc-logo-black-transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cnbcbtn.setIcon(icon3)
        self.cnbcbtn.setIconSize(QtCore.QSize(50, 50))
        self.cnbcbtn.setObjectName("cnbcbtn")
        self.verticalLayout_11.addWidget(self.cnbcbtn, 0, QtCore.Qt.AlignHCenter)
        self.nytimesbtn = QtWidgets.QPushButton(self.frame_3)
        self.nytimesbtn.setMinimumSize(QtCore.QSize(100, 80))
        self.nytimesbtn.setStyleSheet("#nytimesbtn {\n"
"    box-shadow: 3px 4px 0px 0px #899599;\n"
"    background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);\n"
"    background-color:#ededed;\n"
"    border-radius:15px;\n"
"    border:1px solid #d6bcd6;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#3a8a9e;\n"
"    font-family:Arial;\n"
"    font-size:17px;\n"
"    padding:7px 25px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px 1px 0px #e1e2ed;\n"
"}\n"
"#nytimesbtn:hover {\n"
"    background:linear-gradient(to bottom, #bab1ba 5%, #ededed 100%);\n"
"    background-color:#bab1ba;\n"
"}\n"
"#nytimesbtn:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/article-ny-times-bold-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nytimesbtn.setIcon(icon4)
        self.nytimesbtn.setIconSize(QtCore.QSize(50, 50))
        self.nytimesbtn.setObjectName("nytimesbtn")
        self.verticalLayout_11.addWidget(self.nytimesbtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.convertbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page1))
        self.newsbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page2))
        self.convertbtn_2.clicked.connect(self.api)
        self.bbcbtn.clicked.connect(self.bbcac)
        self.cnbcbtn.clicked.connect(self.cnbcac)
        self.nytimesbtn.clicked.connect(self.nytimesac)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hasan&Hamit\'s Currency Converter"))
        self.label.setText(_translate("MainWindow", "H&H\'S CURRENCY CONVERTER"))
        self.convertbtn.setText(_translate("MainWindow", "CONVERTOR"))
        self.newsbtn.setText(_translate("MainWindow", "NEWS"))
        self.datetimelabel.setText(_translate("MainWindow", f"{datetime.strftime(datetime.now(),'%d %B %Y')}"))
        self.label_2.setText(_translate("MainWindow", "FROM"))
        self.base_combobox.setItemText(1, _translate("MainWindow", "TRY"))
        self.base_combobox.setItemText(2, _translate("MainWindow", "USD"))
        self.base_combobox.setItemText(3, _translate("MainWindow", "GBP"))
        self.base_combobox.setItemText(4, _translate("MainWindow", "EUR"))
        self.label_3.setText(_translate("MainWindow", "TO"))
        self.to_combobox.setItemText(1, _translate("MainWindow", "TRY"))
        self.to_combobox.setItemText(2, _translate("MainWindow", "USD"))
        self.to_combobox.setItemText(3, _translate("MainWindow", "GBP"))
        self.to_combobox.setItemText(4, _translate("MainWindow", "EUR"))
        self.label_4.setText(_translate("MainWindow", "AMOUNT\n"
""))
        self.amount_money_lineedit.setPlaceholderText(_translate("MainWindow", "enter the amount"))
        self.convertbtn_2.setText(_translate("MainWindow", "CONVERT"))
        self.bbcbtn.setText(_translate("MainWindow", "BBC ECONOMY"))
        self.cnbcbtn.setText(_translate("MainWindow", "CNBC ECONOMY"))
        self.nytimesbtn.setText(_translate("MainWindow", "NY TIMES"))
import qrcimages


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
