# coding=utf-8
# __author__="Devlee"

"""读写用户信息"""

import os
import json
import time

# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import db_handler
from conf import settings

def load_data(acc_name):
    """读取用户信息"""
    return db_handler.db_handler(acc_name)

def dump_data(account_data):
    """写入用户信息"""
    acc_file = os.path.join(settings.DATABASE['path'],'accounts',str(account_data['id']))
    acc_file += '.json'
    with open(acc_file,'w') as f:
        json.dump(account_data,f)
    return True

if __name__ == '__main__':
    data = {
        "id": 'wmm',
        "password": 666666,
        "credit": 15000,
        "balance": 15000,
        "enroll_date": "2018-04-21",
        "expire_date": "2050-01-01",
        "pay_day": 9,
        "status": 0
    }

    if dump_data(data):
        print('写入成功！')
    else:
        print('写入失败！')
