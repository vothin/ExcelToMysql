# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 15:22
# @Author  : vothin
# @File    : global_path.py

# ****************************************************************

import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)

excel_path = os.path.join(BIR, r'data\食物表.xlsx')
mysql_path = os.path.join(BIR, r'config\mysql_url.yaml')
log_path = os.path.join(BIR, r'log\log.log')
