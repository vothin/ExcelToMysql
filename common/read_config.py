# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:18
# @Author  : vothin
# @File    : read_config.py

# ****************************************************************

import yaml
from base.global_path import mysql_path
from common.record_log import logs

class ReadConfig(object):

    def __init__(self):
        self.conf = self.getConfig()

    # 读取配置文件yaml_path
    def getConfig(self):
        # 读取配置文件
        with open(mysql_path, 'r', encoding='utf-8') as f:
            conf_obj = f.read()

        # 转化成字典格式
        conf_dict = yaml.load(conf_obj, Loader=yaml.FullLoader)
        return conf_dict


    # 获取配置文件的值
    def getValue(self, sec_name):
        try:
            return self.conf[sec_name]
        except Exception as e:
            logs.error(e)

if __name__ == '__main__':
    r = ReadConfig()
    r_dict = r.getValue("mysql_localhost")


