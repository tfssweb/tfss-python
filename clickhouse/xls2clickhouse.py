import os
import re
import xlrd
from clickhouse_driver import Client
from datetime import datetime
from xlrd import xldate_as_tuple
import time


# 连接clickhouse数据库。
client = Client(host='127.0.0.1', port='9000', user='default', database='default', password='xxxxxxxx')


def find_xls_files(folder_path):
  files = [f for f in os.listdir(folder_path) if re.match(r'[A-Za-z]*.*.xls', f)]
  print(files)
  return files


def xls_to_ck(path):
    # Open the workbook and select the first worksheet
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_index(0)

    # Iterate through each row in worksheet and fetch values into dict
    # Notice range is hardcoded to 1 where the spreadsheet for iZettle starts
    for rownum in range(1, sh.nrows):
        row_values = sh.row_values(rownum)
        print(row_values)

        age = 22

        # 对XLSX日期进行转换以及格式化
        trans = datetime(*xldate_as_tuple(sh.cell(rownum, 0).value, 0))
        print(type(trans))
        # 将datetime转换为date
        DataDate = datetime.date(trans)
        # DataDate = trans.strftime('%Y-%m-%d')
        print(DataDate)
        # 时间戳
        Timestamp = time.mktime(DataDate.timetuple())
        print(Timestamp)



        insert_sql = '''
             INSERT INTO database.table (age, DataDate, `Timestamp`) VALUES
        '''

        insert_data = [[age, DataDate, int(Timestamp)]]


        client.execute(insert_sql, insert_data, types_check=True)


""" MAIN EXECUTION SEGMENT BELOW """

# Find all xls files in dir to be parsed
xls = find_xls_files(".")

# Serialize and print to terminal
for filepath in xls:
    print(filepath)

    start = time.time()
    xls_to_ck(filepath)
    end = time.time()
    print('消耗时间(秒)：', end - start)

