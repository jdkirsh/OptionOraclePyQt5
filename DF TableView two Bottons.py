import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import pandas as pd


from database import dataTable

# qtcreator_file  = "<your .ui file>" # Enter file here.
qtcreator_file  = "jkTableViewCheckPutsCallsBotton.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # data = pd.read_csv("../database/SPYtoDF1.csv")
        data = dataTable.dataSelect(callSw=True,putSw=True)
        self.model = TableModel(data)
        self.jktableView.setModel(self.model)

        self.calls_push_button.clicked.connect(self.callsputsBthState)
        self.puts_push_button.clicked.connect(self.callsputsBthState)

    def callsputsBthState(self):
        print ("In callsputsBthState(self)")
        self.callsCheckedSw = False
        self.putsCheckedSw = False
        # data = dataTable.dataSelect(callSw=True,putSw=True)
        if self.calls_push_button.isChecked():
            self.callsCheckedSw = True
        if self.puts_push_button.isChecked():
            self.putsCheckedSw = True
        print ("going to print")
        print ("self.callsChecked=",self.callsCheckedSw)
        print (" self.putsChecked=",self.putsCheckedSw)
        data = dataTable.dataSelect(callSw=self.callsCheckedSw, putSw=self.putsCheckedSw)
        self.model = TableModel(data)
        self.jktableView.setModel(self.model)

    def callsputsBtnHnadler(self):
        print ("In: callsputsBtnHnadler(self)" )
        if self.calls_push_button.isChecked() and not self.puts_push_button.isChecked:
            print ("dataTable.dataSelect(True, False)")
            data = dataTable.dataSelect(True, False)
            self.model = TableModel(data)
            self.jktableView.setModel(self.model)
        elif self.puts_push_button.isChecked() and not self.calls_push_button.isChecked:
            print("dataTable.dataSelect(False, True)")
            dataTable.dataSelect(True, False)
            data = dataTable.dataSelect(False, True)
            self.model = TableModel(data)
            self.jktableView.setModel(self.model)
        else:
            print("dataTable.dataSelect(False, True)")
            data = dataTable.dataSelect(True, True)
            self.model = TableModel(data)
            self.jktableView.setModel(self.model)

    def callsBtnHandler(self):
        if self.calls_push_button.isChecked():
            print ("calls_push_button.isChecked")
            data = dataTable.dataSelect(True, False)
            self.model = TableModel(data)
            self.jktableView.setModel(self.model)
        else:
            # self.putsTable()
            print ("CallsPushButton.clicked")
        # data = pd.read_csv("CalltoDF1.csv")
        # self.model = TableModel(data)
        # self.jktableView.setModel(self.model)

    def putsBtnHandler(self):
        if self.puts_push_button.isChecked():
            print("calls_push_button.isChecked")
            data = dataTable.dataSelect(False, True)
            self.model = TableModel(data)
            self.jktableView.setModel(self.model)
        else:
            # self.putsTable()
            print ("PutsPushButton.clicked")
            # data = pd.read_csv("PuttoDF1.csv")
            # self.model = TableModel(data)
            # self.jktableView.setModel(self.model)

    # def callsBtnHandler(self):
    #     if self.calls_push_button.isChecked():
    #         self.callsTable()
    #     else:
    #         self.putsTable()
    #
    # def callsTable(self):
    #     print("callsTable")
    #     dataTable.dataSelect(True, False)
    #
    # def putsTable(self):
    #     print("putsTable")
    #     dataTable.dataSelect(False, True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())