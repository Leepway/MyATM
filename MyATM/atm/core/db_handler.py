# coding=utf-8
# __author__="Devlee"

"""
为不同数据存储方式提供统一访问接口
"""

import json
import os

from conf import settings

def file_db_handle(conn_params, acc_name):
    """
    文件存储访问具体实现
    """
    acc_file = os.path.join(conn_params['path'], conn_params['name'], str(acc_name)+'.json')
    # print(acc_file)
    if os.path.isfile(acc_file):
        with open(acc_file, 'r') as f:
            account_data = json.load(f)
            return account_data
    else:
        return None


def db_handler(acc_name):
    """
    为不同数据存储方式提供统一访问接口
    """

    conn_params = settings.DATABASE     # 数据库连接参数
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params, acc_name)
    else:
        # 其他存储方式
        pass


