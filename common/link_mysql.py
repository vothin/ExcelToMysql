# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:40
# @Author  : vothin
# @File    : link_mysql.py

# ****************************************************************

import pymysql
from common.record_log import logs
from common.read_config import ReadConfig
from base.base import Base

class LinkMysql(Base):

    # 查询数据
    def insertData(self, name, value):
        sql = 'insert into care_carolie_item ' \
              '(name, carolie, unit_qty, unit) ' \
              'values(%s, 90, %s, "克")'

        self.cursor.execute(sql % (name, value))
        self.connect.commit()
        logs.info("成功插入数据")

        self.cursor.close()
        self.connect.close()
        logs.info('关闭数据库')


    # 修改数据
    def deleteData(self):
        sql = 'delete from care_carolie_item ' \
              'where bool_consume is null'

        self.cursor.execute(sql)
        self.connect.commit()
        logs.info('成功删除数据')

        self.cursor.close()
        self.connect.close()
        logs.info('关闭数据库')



if __name__ == '__main__':
    l = LinkMysql('mysql_localhost')
    # l.insertData('1', 2)
    l.deleteData()



