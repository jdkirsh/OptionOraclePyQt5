from csv import reader
from csv import DictReader
import pandas as pd

INFILE = r'C:\FINANCE\Python\pyCharm\Projects\OptionOraclePyQt5\database\twBottom.csv'

def main():
    print('**** Read csv into a list of lists ****')

    # read csv file as a list of lists
    with open(INFILE, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)

    print('*** Select value in csv Specific Row and Column ***')

    # select the value from csv at row number 3 and column number 2
    row_number = 3
    col_number = 2
    value = list_of_rows[row_number - 1][col_number - 1]

    print('Value in cell at 3rd row and 2nd column : ', value)

    print('*** Use pandas to read rows in a csv file to a list of list without header ***')

    # Create a dataframe from csv
    df = pd.read_csv(INFILE, delimiter=',')
    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]
    # Print list of lists i.e. rows
    print(list_of_rows)

    print('*** Use pandas to read rows in a csv file to a list of list ***')

    # Create a dataframe from csv
    df = pd.read_csv(INFILE, delimiter=',')
    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]
    # Insert Column names as first list in list of lists
    list_of_rows.insert(0, df.columns.to_list())
    # Print list of lists i.e. rows
    print(list_of_rows)

    print('**** Read csv into list of tuples using Python ****')

    # open file in read mode
    with open(INFILE, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Get all rows of csv from csv_reader object as list of tuples
        list_of_tuples = list(map(tuple, csv_reader))
        # display all rows of csv
        print(list_of_tuples)

    print('*** Read csv into list of tuples using pandas in python (without header) ***')

    # Create a dataframe from csv
    df = pd.read_csv(INFILE, delimiter=',')

    # Create a list of tuples for Dataframe rows using list comprehension
    list_of_tuples = [tuple(row) for row in df.values]
    # Print list of tuple
    print(list_of_tuples)

    print('**** Read csv into list of dictionaries using python ****')

def read_twBottomDict():
        # open file in read mode
        with open(INFILE, 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            dict_reader = DictReader(read_obj)
            # get a list of dictionaries from dct_reader
            list_of_dict = list(dict_reader)
        return list_of_dict
            # print list of dict i.e. rows
            # print(list_of_dict)

def main():
    jk = read_twBottomDict()
    myDF = pd.DataFrame(jk)
    print(jk[2]['CheckMark'])
    jk[2]['CheckMark'] = 'N'
    print(jk[2]['CheckMark'])

    print ("pause")

if __name__ == '__main__':
    main()