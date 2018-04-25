# coding=utf-8
# __author__ = "Devlee"

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage', # support mysql in the future
    'name': 'accounts',
    'path': "%s\db" %BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transaction.log', # 交易日志
    'login': 'login.log' # 登录日志
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}


