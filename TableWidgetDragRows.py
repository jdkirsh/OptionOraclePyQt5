# https://stackoverflow.com/questions/34533878/drag-and-dropping-rows-between-two-separate-qtablewidgets

import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidget, QWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout, QVBoxLayout, \
    QApplication, QComboBox


class TableWidgetDragRows(QTableWidget):    # sub class of QTableWidget
    def __init__(self, *args, **kwargs):
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
        print ("In dropMimeData...")
        return True


    def dropEvent(self, event):
        # The QTableWidget from which selected rows will be moved
        print ("In dropEvent...")
        sender = event.source()

        # Default dropEvent method fires dropMimeData with appropriate parameters (we're interested in the row index).
        super().dropEvent(event)
        # Now we know where to insert selected row(s)
        print ("in  super().dropEvent(event)..."," dropRow = self.last_drop_row", self.last_drop_row)
        dropRow = self.last_drop_row
        print("dropRow=",dropRow)

        selectedRows = sender.getselectedRowsFast()
        # print ("selectedRows=",selectedRows)

        # Allocate space for transfer
        for _ in selectedRows:
            self.insertRow(dropRow)
            print ("In Loop..."," self.insertRow(dropRow)...", " dropRow=",dropRow)

        # if sender == receiver (self), after creating new empty rows selected rows might change their locations
        sel_rows_offsets = [0 if self != sender or srow < dropRow else len(selectedRows) for srow in selectedRows]
        selectedRows = [row + offset for row, offset in zip(selectedRows, sel_rows_offsets)]

        # copy content of selected rows into empty ones
        for i, srow in enumerate(selectedRows):             # iterate every selected Row
            rowColumn = 0
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)
            rowColumn = 1
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)
            rowColumn = 2
            item = sender.item(srow, rowColumn)
            source = QTableWidgetItem(item)
            print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            self.setItem(dropRow + i, rowColumn, source)
            rowColumn = 3
            # item = sender.item(srow, rowColumn)
            # source = QTableWidgetItem(item)
            print("dropping :", item.text(), " srow=", srow, " rowColumn=", rowColumn)
            comboBox = QtWidgets.QComboBox()
            li = ["Put","Call"]
            comboBox.addItems(li)
            self.setCellWidget(dropRow + i, rowColumn, comboBox)


            # for rowColumn in range(self.columnCount()):     # iterate every column
            #     item = sender.item(srow, rowColumn)
            #     # if (sender.item(srow, j) is not None):
            #     if item:
            #         source = QTableWidgetItem(item)
            #         print ("dropping :",item.text(), " srow=",srow," rowColumn=",rowColumn  )
            #
            #         '''
            #         attr = ['one', 'two', 'three', 'four', 'five']
            #         i = 0
            #         for j in attr:
            #             self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(j))
            #             comboBox = QtWidgets.QComboBox()
            #             self.tableWidget.setCellWidget(i, 1, comboBox)
            #             i += 1
            #             '''
            #         comboBox = QtWidgets.QComboBox()
            #         li = ["Item1","Item2"]
            #         comboBox.addItems(li)
            #         # self.setItem(dropRow + i, rowColumn, source)
            #         self.setCellWidget(dropRow + i, rowColumn, comboBox)
            #         self.setItem(dropRow + i, rowColumn, source)

        # delete selected rows
        for srow in reversed(selectedRows):
            sender.removeRow(srow)

        event.accept()


    def getselectedRowsFast(self):
        selectedRows = []
        for item in self.selectedItems():
            if item.row() not in selectedRows:
                selectedRows.append(item.row())
                # print ("item.row=",item.row())
                print("item.row=", item.text())
        selectedRows.sort()
        print ("selectedRows=", selectedRows)
        return selectedRows


class Window(QWidget):
    def __init__(self):
        super().__init__()    # super gives access to the parent object QWidget

        layout = QVBoxLayout()  # Vertical layout
        self.setLayout(layout)
        columnCount = 4         # number of columns in table
        # combobox = QComboBox()
        # combobox.addItem("Combobox item")

       #  self.table_widgets = []  # Create List container for tables
       # for _ in range(2):
        source_tw = TableWidgetDragRows()   # tw is object TableWidgetsDragRows is a class type QTableWidget defined before
        source_tw.setColumnCount(columnCount)         # the tw table has less columns
        source_tw.setHorizontalHeaderLabels(['Colour', 'Model','carYear','Type'])   #  set label for tw table

        source_tw.setAcceptDrops(False)         # source_tw will not accept records moved out

        layout.addWidget(source_tw)

        dest_tw = TableWidgetDragRows()  # tw is object TableWidgetsDragRows is a class type QTableWidget defined before
        dest_tw.setColumnCount(columnCount)  # the tw table has less columns



        dest_tw.setHorizontalHeaderLabels(['Colour', 'Model','carYear','Type'])  # set label for tw table
        layout.addWidget(dest_tw)
        # self.table_widgets.append(tw)   # two tw tables in the table_widgets list container


        # filled_widget = self.table_widgets[0]      #  filled_widget is the first in the table_widgets container
        filled_widget = source_tw
        items = [('Red', 'Toyota','1998','Call'), ('Blue', 'RV','1977','Put'), ('Green', 'Beetle','1976','Call')]
        for i, (colour, model, carYear,type) in enumerate(items):
            c = QTableWidgetItem(colour)
            m = QTableWidgetItem(model)
            y = QTableWidgetItem(carYear)
            t = QTableWidgetItem(type)

            filled_widget.insertRow(filled_widget.rowCount())
            # filled_widget.setCellWidget(i, 0, combobox)
            # filled_widget.setCellWidget(i, 1, combobox)

            filled_widget.setItem(i, 0, c)
            filled_widget.setItem(i, 1, m)
            filled_widget.setItem(i, 2, y)
            filled_widget.setItem(i, 3, t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())