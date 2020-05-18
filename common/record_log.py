# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 16:23
# @Author  : vothin
# @File    : record_log.py

# ****************************************************************

import logging
import colorlog
from base.global_path import log_path

def record_logging(logging_path=None):

    color_logs = {
        "DEBUG"    : 'cyan',
        "INFO"     : 'green',
        "WARNING"  : 'yellow',
        'ERROR'    : 'red',
        'CRITICAL' : 'red',
    }

    if logging_path != None:
        logging_path = logging_path
    else:
        logging_path = log_path

    # 实例loggers
    logger = logging.getLogger(__name__)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # 设置日志级别

        # 日志储存在指定文件中
        fh = logging.FileHandler(logging_path, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 日志打印在屏幕
        sh = colorlog.StreamHandler()   # 控制台日志输出颜色
        sh.setLevel(logging.DEBUG)

        for_mt = colorlog.ColoredFormatter('%(log_color)s %(asctime)s %(filename)s[line:%(lineno)d)] %(levelname)s: %(message)s',
                                           log_colors=color_logs)

        fh.setFormatter(for_mt)
        sh.setFormatter(for_mt)

        # 给logger对象添加handler
        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger

logs = record_logging()

if __name__ == '__main__':
    logs.info('中文')
