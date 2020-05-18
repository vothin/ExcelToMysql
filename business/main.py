# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 15:08
# @Author  : vothin
# @File    : main.py

# ****************************************************************

from common.read_excel import ReadExcel
from common.dml_mysql import DML_Mysql
from common.record_log import logs

class Main(DML_Mysql):

    def main(self):

        self.deleteData()

        data = ReadExcel('Sheet1').data

        count = 0
        for i in range(len(data)):
            self.insertData(data[i][0], data[i][1])
            count += 1
            # print(data[i][0], data[i][1])

        logs.info('成功插入%s条数据', count)
        self.cursor.close()
        self.connect.close()
        logs.info('关闭数据库')


if __name__ == '__main__':
    m = Main('mysql_localhost')
    m.main()
