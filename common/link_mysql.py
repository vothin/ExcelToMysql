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

        connect = pymysql.Connect(
            host = self.conf['url'],
            port = self.conf['port'],
            user = self.conf['username'],
            passwd = self.conf['password'],
            db = 'wdkl_member',

        )

    # 获得配置文件的数据
    def getConfig(self, sec_name):
        r = ReadConfig()
        readConfig = r.getValue(sec_name)

        return readConfig





if __name__ == '__main__':
    l = LinkMysql('mysql_localhost')
    print(l)


