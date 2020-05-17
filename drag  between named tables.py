import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem, QWidget, QHBoxLayout, QApplication, \
    QVBoxLayout
from database import TwTopTwBottom

# from TableWidgetDragRows

class TableWidgetDragRows(QTableWidget):    # sub class of QTableWidget
    def __init__(self, *args, **kwargs):
        # self.twBottomFrame = TwTopTwBottom.gettwBottom()
        # print("self.twBottomFame=", self.twBottomFrame)

        super().__init__(*args, **kwargs)   # accept arguments

        self.cellClicked.connect(self.cell_was_clicked)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows) # full row drag mode
        # self.OverwriteMode(False)
        # self.setSelectionMode(QAbstractItemView.SingleSelection)


        self.last_drop_row = None

    def cell_was_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.itemAt(row, column)
        self.ID = item.text()

    # Override this method to get the correct row index for insertion
    def dropMimeData(self, row, col, mimeData, action):
        self.last_drop_row = row
        # print ("In dropMimeData...")
        return True


    def dropEvent(self, event):
        # The QTableWidget from which selected rows will be moved
        # print ("In dropEvent...")
        twBottomFrame = TwTopTwBottom.gettwBottom()
        # print ("self.twBottomFrame=",self.twBottomFrame)

        sender = event.source()

        # Default dropEvent method fires dropMimeData with appropriate parameters (we're interested in the row index).
        super().dropEvent(event)
        # Now we know where to insert selected row(s)
        # print ("in  super().dropEvent(event)..."," dropRow = self.last_drop_row", self.last_drop_row)
        dropRow = self.last_drop_row
        # print("dropRow=",dropRow)

        selectedRows = sender.getselectedRowsFast()
        # print ("selectedRows=",selectedRows)

        # Allocate space for transfer
        for r in selectedRows:
            self.insertRow(dropRow)
            # print ("In Loop..."," self.insertRow(dropRow)...", " dropRow=",dropRow)

        # if sender == receiver (self), after creating new empty rows selected rows might change their locations
        sel_rows_offsets = [0 if self != sender or srow < dropRow else len(selectedRows) for srow in selectedRows]
        selectedRows = [row + offset for row, offset in zip(selectedRows, sel_rows_offsets)]

        # copy content of selected rows into empty ones
        var1 = enumerate(selectedRows)
        for i, srow in enumerate(selectedRows): # iterate every selected Row
            # print ("for i, srow in enumerate(selectedRows)=", " i=",i, " srow=", srow, " enumerate(selectedRows)=",var1)
            rowColumn = 1
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            # print("dropping :", item.text(), " srow=", srow," dropRow=",dropRow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)
            # dfRow = dropRow + i
            dfRow = dropRow
            dfColumn = 'Type'
            # twBottomFrame.iat[dfRow, dfColumn] = item.text()
            # twBottomFrame = twBottomFrame.reset_index(drop=True)
            twBottomFrame.ix[dfRow, dfColumn] = item.text()
            # twBottomFrame.ix[1, dfColumn] = item.text()
            # twBottomFrame.ix[2, dfColumn] = item.text()
            # twBottomFrame.ix[3, dfColumn] = item.text()
            # twBottomFrame.at[dfRow, dfColumn] = item.text()
            # twBottomFrame.loc[dfRow, twBottomFrame.columns.get_loc(dfColumn)] = item.text()
            # twBottomFrame.loc[twBottomFrame.index[dfRow], dfColumn] = item.text()
            print ("UPDATING=", "dfRow=",dfRow, " dfColumn=",dfColumn," item.text=",item.text() )
            print ("new df=",twBottomFrame )


            rowColumn = 2
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            # print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)

            rowColumn = 3
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            # print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)

            rowColumn = 4
            # item = sender.item(srow, rowColumn)
            # source = QTableWidgetItem(item)
            # print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            comboBox = QtWidgets.QComboBox()
            li = ["Put","Call"]
            comboBox.addItems(li)
            self.setCellWidget(dropRow + i, rowColumn, comboBox)


        # delete selected rows
        for srow in reversed(selectedRows):
            sender.removeRow(srow)

        event.accept()


    def getselectedRowsFast(self):
        selectedRows = []
        for item in self.selectedItems():
            if item.row() not in selectedRows:
                selectedRows.append(item.row())
                # print("In getselectedRowsFast: item.row=", item.text())
        selectedRows.sort()
        # print ("In getselectedRowsFast: selectedRows=", selectedRows)
        return selectedRows

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.table_widgets = []
        # for _ in range(2):
        twTop = TableWidgetDragRows()

        twTop.data = TwTopTwBottom.gettwTop()
        # print ("twTop.data=", twTop.data)
        # get twTop columnCount
        twTop.setColumnCount(twTop.data.shape[1])

        # get twTop HorizontalHeadrLables
        # twTop.setHorizontalHeaderLabels(['Colour', 'Model'])
        twTop.setHorizontalHeaderLabels(list(twTop.data.columns))
        twTop.setAcceptDrops(False)             # twTop is not accepting drops

        twBottom = TableWidgetDragRows()
        twBottom.strategy = TwTopTwBottom.gettwBottom()
        # print (twBottom.data)
        # get twBottom columnCount
        twBottom.setColumnCount(twBottom.strategy.shape[1])

        # get twBottom HorizontalHeaderLables
        twBottom.setHorizontalHeaderLabels(list(twBottom.strategy.columns))
        # table = waitForObject(":Address Book - MyAddresses.adr.File_QTableWidget")

        # columnCount = twBottom.columnCount
        # rowCount = twBottom.rowCount
        # print ("JK columnCount=", columnCount," JK rowCount=",rowCount)
        # for row in range(rowCount):
        # for row in rowCount:
        # #     for col in range(columnCount):
        #       for col in columnCount:
        #         item = twBottom.item(row, col)
        #         itemText = item.text()
        #         print ("JK Looping: ", "row=",row, " col=",col, "itemText=", itemText)
                # test.log(str(itemText))
                # test.verify(itemText != "")



        # self.table_widgets.append(twTop)
        layout.addWidget(twTop)
        layout.addWidget(twBottom)

        # top_widget = self.table_widgets[0]
        # top_widget = twTop
        # rowcount = len(twTop.data.index)
        # print ("rowcount=", rowcount)
        # twTop.rowcount = twTop.data.shape(0)
        for index, row in twTop.data.iterrows():
            Ty = QTableWidgetItem(str(row['Type']))
            St = QTableWidgetItem(str(row['Strike']))
            Sy = QTableWidgetItem(str(row['Symbol']))
            Op = QTableWidgetItem(str(row['Open_Int']))
            Vo = QTableWidgetItem(str(row['Volume']))
            La = QTableWidgetItem(str(row['Last']))
            Ex = QTableWidgetItem(str(row['Exp']))

            twTop.insertRow(index)
            twTop.setItem(index, 1, Ty)
            twTop.setItem(index, 2, St)
            twTop.setItem(index, 3, Sy)
            twTop.setItem(index, 4, Op)
            twTop.setItem(index, 5, Vo)
            twTop.setItem(index, 6, La)
            twTop.setItem(index, 7, Ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())