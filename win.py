from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit.setGeometry(QtCore.QRect(143, 336, 621, 201))
        self.textedit.setObjectName("Textedit")
        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(250, 20, 113, 22))
        self.combobox.setObjectName("combobox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textedit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textedit_2.setGeometry(QtCore.QRect(145, 91, 621, 211))
        self.textedit_2.setObjectName("Textedit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 20, 80, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 20, 80, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lr4"))
        self.pushButton.setText(_translate("MainWindow", "Запуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Открыть файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Parsemail"))
        self.pushButton_4.setText(_translate("MainWindow", "Parsip"))
