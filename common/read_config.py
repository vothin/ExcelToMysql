# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:18
# @Author  : vothin
# @File    : read_config.py

# ****************************************************************

import pyymal
from base.global_path import mysql_path
from common.record_log import logs

class ReadConfig(object):

    def __init__(self):
        self.conf = self.getConfig()

    # 读取配置文件yaml_path
    def getConfig(self):
        with open(mysql_path, 'r', encoding='utf-8') as f:
            conf_obj = f.read()



