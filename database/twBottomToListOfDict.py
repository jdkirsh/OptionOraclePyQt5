import csv

INFILE = r'C:\FINANCE\Python\pyCharm\Projects\OptionOraclePyQt5\database\twBottom.csv'

# with open(INFILE) as f:
#     a = [{k: int(v) for k, v in row.items()}
#         for row in csv.DictReader(f, skipinitialspace=True)]
#
# print (a)


# from csv import reader
#
# # read csv file as a list of lists
# #####################################
# with open(INFILE, 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Pass reader object to list() to get a list of lists
#     list_of_rows = list(csv_reader)
#
# print(list_of_rows)
#
# # Select specific value in csv by specific row and column number
# ################################################################
# row_number = 4
# col_number = 3
# value = list_of_rows[row_number - 1][col_number - 1]
#
# print('Value in cell at 3rd row and 2nd column : ', value)



# Read csv into list of dictionaries using python
######################################################
# from csv import DictReader
#
# # open file in read mode
# with open(INFILE, 'r') as read_obj:
#     # pass the file object to DictReader() to get the DictReader object
#     dict_reader = DictReader(read_obj)
#     # get a list of dictionaries from dct_reader
#     list_of_dict = list(dict_reader)
#     # print list of dict i.e. rows
#     print(list_of_dict)

from csv import DictReader

print('**** Read csv into list of dictionaries using python ****')
# open file in read mode
def readtwBottom():
    with open(INFILE, 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        # print list of dict i.e. rows
        print(list_of_dict)
    return list_of_dict
        # print list of dict i.e. rows


# def main():
#     myDict = readtwBottom
#
#
#
# if __name__ == '__main__':
#     main()