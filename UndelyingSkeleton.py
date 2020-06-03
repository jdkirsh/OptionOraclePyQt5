import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from database import underlyingDB


# qtcreator_file  = "<your .ui file>" # Enter file here.
qtcreator_file  = "UnderlyingV01.ui" # Enter file here.
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
        self.underlyingDot = underlyingDB.dictToDot(self.underlyingDF)
        print ("DF pause")
        # self.QuotePriceLe.setText(underlyingDot.)
# df.set_index('ID').T.to_dict('list')
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())