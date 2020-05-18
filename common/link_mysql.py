# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:40
# @Author  : vothin
# @File    : link_mysql.py

# ****************************************************************

import pymysql
from common.record_log import logs
from common.read_config import ReadConfig

class LinkMysql():

    def __init__(self, sec_name):
        self.conf = self.getConfig(sec_name)

        self.connect = pymysql.Connect(
            host = self.conf['url'],
            port = self.conf['port'],
            user = str(self.conf['username']),
            passwd = str(self.conf['password']),
            db = self.conf['db'],
            charset = 'utf8'
        )

        self.cursor = self.connect.cursor()
        logs.info('链接数据库成功')

    # 获得配置文件的数据
    def getConfig(self, sec_name):
        r = ReadConfig()
        readConfig = r.getValue(sec_name)

        return readConfig


    # 查询数据
    def insertData(self, name, value):
        sql = 'insert into care_carolie_item ' \
              '(name, carolie, unit_qty, unit)' \
              ' values(%s, 90, %s, "克")'

        self.cursor.execute(sql % (name, value))
        self.connect.commit()
        logs.info("成功插入数据")
        self.cursor.close()
        self.connect.close()


    # 修改数据
    def deleteData(self):
        sql = 'delete from care_carolie_item' \
              'where bool_consume is Null'

        self.cursor.execute(sql)
        self.connect.commit()
        logs.info('成功删除数据')
        self.cursor.close()
        self.connect.close()



if __name__ == '__main__':
    l = LinkMysql('mysql_localhost')
    l.insertData('1', 2)



