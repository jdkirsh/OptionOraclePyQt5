import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem, QWidget, QHBoxLayout, QApplication, \
    QVBoxLayout
from database import TwTopTwBottom

class TableWidgetDragRows(QTableWidget):
# class TableWidgetDragRows(QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setDragDropOverwriteMode(False)
        # self.setSelectionMode(QAbstractItemView.SingleSelection)

        self.last_drop_row = None

    # Override this method to get the correct row index for insertion
    def dropMimeData(self, row, col, mimeData, action):
        self.last_drop_row = row
        return True


    def dropEvent(self, event):
        # The QTableWidget from which selected rows will be moved
        sender = event.source()

        # Default dropEvent method fires dropMimeData with appropriate parameters (we're interested in the row index).
        super().dropEvent(event)
        # Now we know where to insert selected row(s)
        dropRow = self.last_drop_row

        selectedRows = sender.getselectedRowsFast()

        # Allocate space for transfer
        for _ in selectedRows:
            self.insertRow(dropRow)

        # if sender == receiver (self), after creating new empty rows selected rows might change their locations
        sel_rows_offsets = [0 if self != sender or srow < dropRow else len(selectedRows) for srow in selectedRows]
        selectedRows = [row + offset for row, offset in zip(selectedRows, sel_rows_offsets)]

        # copy content of selected rows into empty ones
        for i, srow in enumerate(selectedRows):
            for j in range(self.columnCount()):
                item = sender.item(srow, j)
                if item:
                    source = QTableWidgetItem(item)
                    self.setItem(dropRow + i, j, source)

        # delete selected rows
        for srow in reversed(selectedRows):
            sender.removeRow(srow)

        event.accept()


    def getselectedRowsFast(self):
        selectedRows = []
        for item in self.selectedItems():
            if item.row() not in selectedRows:
                selectedRows.append(item.row())
        selectedRows.sort()
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

        twBottom = TableWidgetDragRows()

        # get twBottom columnCount

        twBottom.setColumnCount(2)

        # get twBottom HorizontalHeaderLables
        
        twBottom.setHorizontalHeaderLabels(['Colour', 'Model'])


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