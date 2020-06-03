import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from database import underlyingDB

# qtcreator_file  = "<your .ui file>" # Enter file here.
qtcreator_file  = "OptionsOracleV01.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.RefreshPb.clicked.connect(self.refresh_underlying)

    def refresh_underlying(self):
        print ("Refreshing")
        self.underlyingDF = underlyingDB.loadUnderlying()

        print (self.underlyingDF['Symbol'][0])

        self.SymbolLe.setText(self.underlyingDF['Symbol'][0])
        self.LastUpdateLe.setText(self.underlyingDF['RecDate'][0])
        self.LastPriceLe.setText(self.underlyingDF['LastPrice'][0])
        self.ImpPctLe.setText(self.underlyingDF['ImpPct'][0])
        self.HisPctLe.setText(self.underlyingDF['HisPct'][0])
        self.DividendPctLe.setText(self.underlyingDF['DividendPct'][0])
        self.BidLe.setText(self.underlyingDF['Bid'][0])
        self.AskLe.setText(self.underlyingDF['Ask'][0])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())