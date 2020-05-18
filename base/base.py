# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 15:41
# @Author  : vothin
# @File    : base.py

# ****************************************************************


import pymysql
from common.read_config import ReadConfig
from common.record_log import logs

class Base():

    def __init__(self, sec_name):
        r = ReadConfig()
        self.conf = r.getValue(sec_name)

        self.connect = pymysql.Connect(
            host = self.conf['url'],
            port = self.conf['port'],
            user = str(self.conf['username']),
            passwd = str(self.conf['password']),
            db = self.conf['db'],
            charset = 'utf8'
        )

        self.cursor = self.connect.cursor()
        logs.info('成功连接数据库')


