from win import Ui_MainWindow
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor , QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMessageBox
import sys
resault = re.compile(r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.('
                            r'?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
mind = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")"
                          r"@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
combo_1 = re.compile(r"жизнь")
combo_2 = re.compile(r"as")
combo_3 = re.compile(r"kuku")


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.combobox.addItem('жизнь', 1)
        self.ui.combobox.addItem('as', 2)
        self.ui.combobox.addItem('kuku', 3)
        self.ui.pushButton_2.clicked.connect(self.openpng)
        self.ui.pushButton.clicked.connect(self.parscombo)
        self.ui.pushButton_3.clicked.connect(self.parsemail)
        self.ui.pushButton_4.clicked.connect(self.parsip)

    def parscombo(self):
        if self.ui.combobox.currentData() == 1:
            cursor = self.ui.textedit.textCursor()
            for m in combo_1.finditer(self.ui.textedit.toPlainText()):
                nn = m.start()
                nm = len(m.group())
                self.ui.textedit_2.append('На позиции ' + str(nn) + ' был обнаружен ' + str(m.group()))
                start = nn
                length = nm
                cursor.clearSelection()
                cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
                cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, start + length)
                cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, length)
                cursor.selectedText()
                m = QTextCharFormat()
                n = QBrush(QColor(255, 255, 0))
                m.setBackground(n)
                cursor.setCharFormat(m)
                self.ui.textedit.setTextCursor(cursor)
            cursor.clearSelection()
            m = QTextCharFormat()
            n = QBrush(QColor(0, 0, 0))
            m.setBackground(n)
            cursor.setCharFormat(m)
        elif self.ui.combobox.currentData() == 2:
            cursor = self.ui.textedit.textCursor()
            for m in combo_2.finditer(self.ui.textedit.toPlainText()):
                nn = m.start()
                nm = len(m.group())
                self.ui.textedit_2.append('На позиции ' + str(nn) + ' был обнаружен ' + str(m.group()))
                start = nn
                length = nm
                cursor.clearSelection()
                cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
                cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, start + length)
                cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, length)
                cursor.selectedText()
                m = QTextCharFormat()
                n = QBrush(QColor(255, 150, 0))
                m.setBackground(n)
                cursor.setCharFormat(m)
                self.ui.textedit.setTextCursor(cursor)
            cursor.clearSelection()
            m = QTextCharFormat()
            n = QBrush(QColor(0, 0, 0))
            m.setBackground(n)
            cursor.setCharFormat(m)
        elif self.ui.combobox.currentData() == 3:
            cursor = self.ui.textedit.textCursor()
            for m in combo_3.finditer(self.ui.textedit.toPlainText()):
                nn = m.start()
                nm = len(m.group())
                self.ui.textedit_2.append('На позиции ' + str(nn) + ' был обнаружен ' + str(m.group()))
                start = nn
                length = nm
                cursor.clearSelection()
                cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
                cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, start + length)
                cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, length)
                cursor.selectedText()
                m = QTextCharFormat()
                n = QBrush(QColor(100, 255, 0))
                m.setBackground(n)
                cursor.setCharFormat(m)
                self.ui.textedit.setTextCursor(cursor)
            cursor.clearSelection()
            m = QTextCharFormat()
            n = QBrush(QColor(0, 0, 0))
            m.setBackground(n)
            cursor.setCharFormat(m)

    def openpng(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "All files (*.*)")
        if path:
            f = open(path, 'r+')
            try:
                text = f.read()
                # errorFormat = '<span style="color:red;">{}</span>'
                # print(text)
                # self.ui.textedit.setText(errorFormat.format(text))
                self.ui.textedit.setText(text)
                self.ui.textedit.update()

            finally:
                f.close()

    def parsip(self):
        cursor = self.ui.textedit.textCursor()
        for m in resault.finditer(self.ui.textedit.toPlainText()):
            nn = m.start()
            nm = len(m.group())
            self.ui.textedit_2.append('На позиции ' + str(nn) + ' был обнаружен ' + str(m.group()))
            start = nn
            length = nm
            cursor.clearSelection()
            cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
            cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, start + length)
            cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, length)
            cursor.selectedText()
            m = QTextCharFormat()
            n = QBrush(QColor(255, 255, 0))
            m.setBackground(n)
            cursor.setCharFormat(m)
            self.ui.textedit.setTextCursor(cursor)
        cursor.clearSelection()
        m = QTextCharFormat()
        n = QBrush(QColor(0, 0, 0))
        m.setBackground(n)
        cursor.setCharFormat(m)

    def parsemail(self):
        cursor = self.ui.textedit.textCursor()
        for m in mind.finditer(self.ui.textedit.toPlainText()):
            nn = m.start()
            nm = len(m.group())
            self.ui.textedit_2.append('На позиции ' + str(nn) + ' был обнаружен ' + str(m.group()))
            start = nn
            length = nm
            cursor.clearSelection()
            cursor.movePosition(QTextCursor.Start, QTextCursor.MoveAnchor)
            cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor, start + length)
            cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, length)
            cursor.selectedText()
            m = QTextCharFormat()
            n = QBrush(QColor(255, 255, 0))
            m.setBackground(n)
            cursor.setCharFormat(m)
            self.ui.textedit.setTextCursor(cursor)
        cursor.clearSelection()
        m = QTextCharFormat()
        n = QBrush(QColor(0, 0, 0))
        m.setBackground(n)
        cursor.setCharFormat(m)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
