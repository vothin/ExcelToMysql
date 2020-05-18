# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:40
# @Author  : vothin
# @File    : dml_mysql.py

# ****************************************************************

import time
from common.record_log import logs
from base.base import Base

class DML_Mysql(Base):

    # 查询数据
    def insertData(self, name, value):
        sql = 'insert into care_carolie_item ' \
              '(create_time, name, carolie, unit_qty, unit) ' \
              'values(%s, "%s", 90, %s, "克")'

        now_time = int(time.time())

        self.cursor.execute(sql % (now_time, name, value))
        self.connect.commit()


    # 修改数据
    def deleteData(self):
        sql = 'delete from care_carolie_item ' \
              'where bool_consume is null'

        self.cursor.execute(sql)
        self.connect.commit()
        logs.info('成功删除%s数据' % self.cursor.rowcount)


    # 查询语句
    def selectData(self):
        sql = 'select * from care_carolie_item'

        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            print(i)
        logs.info('成功查询%s数据' % self.cursor.rowcount)


if __name__ == '__main__':
    l = DML_Mysql('mysql_39')
    l.selectData()



