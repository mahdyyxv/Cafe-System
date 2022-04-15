# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerSKapxZ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import PySide2.QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(495, 538)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 491, 511))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(410, 260, 31, 20))
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 110, 61, 21))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 181, 51, 21))
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 380, 41, 21))
        self.comboBox_5 = QComboBox(self.tab)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(30, 282, 151, 41))
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(300, 227, 93, 51))
        self.comboBox_4 = QComboBox(self.tab)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(30, 140, 151, 41))
        self.lcdNumber_2 = QLCDNumber(self.tab)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(20, 370, 201, 51))
        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(400, 240, 51, 22))
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 150, 61, 21))
        self.pushButton_8 = QPushButton(self.tab)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 30, 93, 28))
        self.pushButton_9 = QPushButton(self.tab)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(410, 290, 31, 41))
        font = QFont()
        font.setPointSize(36)
        self.pushButton_9.setFont(font)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 220, 61, 21))
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 260, 55, 16))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(380, 430, 93, 31))
        self.comboBox_3 = QComboBox(self.tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(30, 210, 151, 41))
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(40, 430, 93, 28))
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(200, 291, 61, 21))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 20, 113, 51))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 210, 381, 81))
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 60, 421, 101))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_15.setFont(font1)
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 370, 281, 71))
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(180, 310, 93, 28))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SYS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"HOT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"COLD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0633\u0639\u0631", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Nothing", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Lemon", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Orange", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Mango", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0647", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Nothing", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Tea", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Coffe", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Nescafe", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0634\u0631\u0648\u0628", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"New Bill", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0634\u0631\u0648\u0628", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fresh", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Nothing", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Pepsi", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Cola", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Amestel", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0634\u0631\u0648\u0628", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u0637\u0631\u0627\u0628\u064a\u0632\u0647", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Bill", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password Please", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Don't Share The Password With Anyone ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TODAYS TOTAL WILL SHOWN HERE", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Private", None))
    # retranslateUi




if __name__ == "__main__":
    import sys
    app = PySide2.QtWidgets.QApplication(sys.argv)
    MainWindow = PySide2.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
