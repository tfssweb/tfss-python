#!/usr/bin/env python
# coding=utf-8
import xlrd, json, os, re, sys
from collections import OrderedDict
import datetime


def find_xls_files(folder_path):
    files = [f for f in os.listdir(folder_path) if re.match(r'[A-Za-z]*.*.xls', f)]
    print(files)
    return files


def xls_to_json(path):
    # Open the workbook and select the first worksheet
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_index(0)

    # List to hold dictionaries
    transaction_list = []

    # Iterate through each row in worksheet and fetch values into dict
    # Notice range is hardcoded to 1 where the spreadsheet for iZettle starts
    for rownum in range(1, sh.nrows):
        transaction = OrderedDict()
        row_values = sh.row_values(rownum)
        print(row_values)

        # Skip digital fees
        # if "Digital Fee" in row_values[4]: continue
        # if "iZettle Fee" in row_values[4]: continue

        transaction['DataDate'] = row_values[0].replace('/', '-')
        transaction['ProvinceName'] = row_values[1]
        transaction['CityName'] = row_values[2]
        transaction['CountyName'] = row_values[3]
        transaction['Clng'] = row_values[4]
        transaction['Clat'] = row_values[5]
        transaction['PointName'] = row_values[6]
        transaction['SO2Value'] = row_values[7]
        transaction['COValue'] = row_values[8]
        transaction['NO2Value'] = row_values[9]
        transaction['O31HValue'] = row_values[10]
        transaction['O38HValue'] = row_values[11]
        transaction['PM10Value'] = row_values[12]
        transaction['PM25Value'] = row_values[13]
        transaction['NOValue'] = row_values[14]

        # print(transaction)
        transaction_list.append(transaction)

    parsed_xls = json.dumps(transaction_list, ensure_ascii=False)

    return parsed_xls


""" MAIN EXECUTION SEGMENT BELOW """

# Find all xls files in dir to be parsed
xls = find_xls_files(".")

# Serialize and print to terminal
for filepath in xls:
    print(len(sys.argv))
    print(sys.argv[0])
    if (len(sys.argv) == 2):
        # If a second argument is given to the script, it dumps the output in a file by that name
        with open(sys.argv[1], 'w') as f:
            f.write(xls_to_json(filepath))
    else:
        # Writes output to terminal
        # print(xls_to_json(filepath))
        print(filepath)
        json_file_name = filepath.replace('.xls', '.json')

        with open(json_file_name, 'w', encoding="UTF-8") as f:
            f.write(xls_to_json(filepath))
