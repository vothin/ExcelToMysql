# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 10:47
# @Author  : vothin
# @File    : read_excel.py

# ****************************************************************

import xlrd
from common.record_log import logs
from base.global_path import excel_path

class ReadExcel():

    def __init__(self, sheet):
        self.data = self.getExcel(sheet)


    # 读取数据文件xlsx
    def getExcel(self, sheet):

        # 打开xlsx文件
        data = xlrd.open_workbook(excel_path)

        # 获取sheet页
        sheet = data.sheet_by_name(sheet)

        # 循环sheet页的内容
        sheet_list = []
        for i in range(sheet.nrows):
            sheet_list.append(sheet.row_values(i))

        return sheet_list


    # 获取配置文件的值
    def getValue(self, index):
        try:
            self.data[index]
        except Exception as e:
            logs.error(e)



if __name__ == '__main__':
    r = ReadExcel('Sheet1')
    print(r.data)