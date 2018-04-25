# coding=utf-8
# __author__="Devlee"

"""
处理所有日志相关事务
"""

import logging
from conf import settings

def logger(log_type):
    """"返回logger对象"""

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    # 创建控制台日志并设为debug级别
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # 创建文件日志并设置级别
    log_file = "%s/log/%s" %(settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)

    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


