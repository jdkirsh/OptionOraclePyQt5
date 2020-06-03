# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UnderlyingV01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 40, 160, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.QuotePriceLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.QuotePriceLbl.setObjectName("QuotePriceLbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.QuotePriceLbl)
        self.QuotePriceLe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.QuotePriceLe.setObjectName("QuotePriceLe")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.QuotePriceLe)
        self.AskLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.AskLbl.setObjectName("AskLbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.AskLbl)
        self.AskLe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.AskLe.setObjectName("AskLe")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AskLe)
        self.BidLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.BidLbl.setObjectName("BidLbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BidLbl)
        self.BidLe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.BidLe.setObjectName("BidLe")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BidLe)
        self.DivPctLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.DivPctLbl.setObjectName("DivPctLbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.DivPctLbl)
        self.DivPct = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.DivPct.setObjectName("DivPct")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.DivPct)
        self.VolumeLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.VolumeLbl.setObjectName("VolumeLbl")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.VolumeLbl)
        self.VolumeLe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.VolumeLe.setObjectName("VolumeLe")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.VolumeLe)
        self.CapLbl = QtWidgets.QLabel(self.formLayoutWidget)
        self.CapLbl.setObjectName("CapLbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.CapLbl)
        self.CapLe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.CapLe.setObjectName("CapLe")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.CapLe)
        self.RefreshPb = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshPb.setGeometry(QtCore.QRect(100, 210, 75, 23))
        self.RefreshPb.setObjectName("RefreshPb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QuotePriceLbl.setText(_translate("MainWindow", "Quote Price"))
        self.AskLbl.setText(_translate("MainWindow", "Ask"))
        self.BidLbl.setText(_translate("MainWindow", "Bid"))
        self.DivPctLbl.setText(_translate("MainWindow", "Div %"))
        self.VolumeLbl.setText(_translate("MainWindow", "Volume"))
        self.CapLbl.setText(_translate("MainWindow", "Cap"))
        self.RefreshPb.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
