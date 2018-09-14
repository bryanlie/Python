import xlrd
from xlutils.copy import copy
import numpy as np


def deal_excel():
    dropped = []

    worksheet = xlrd.open_workbook('gradebook_168.xlsx')
    sheet_names = worksheet.sheet_names()
    sheet = worksheet.sheet_by_name(sheet_names[0])

    for row_ind in range(sheet.nrows):
        row = []
        for col_ind in range(sheet.ncols):
            cell = sheet.cell(row_ind, col_ind)
            row.append(int(cell.value))
        print(row)
        row.sort()
        newrow = row[2:]
        print(newrow, "\n")
        avg = np.average(newrow)
        dropped.append(np.round(avg, 3))
    return dropped


def write_excel(data):
    w = copy(xlrd.open_workbook('gradebook_168.xlsx'))
    sheet = w.get_sheet(0)
    for i in range(len(data)):
        sheet.write(i, 10, data[i])
    w.save('gb1.xls')
    return


if __name__ == '__main__':
    data = deal_excel()
    write_excel(data)