# coding=utf-8
# __author__="Devlee"
"""
处理登录验证事务
"""

import os
import json
import time
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functools import wraps
from core import db_handler
from core import logger
from conf import settings

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            print('请先登录！')

    return wrapper

def acc_auth(account,password):
    """
    用户验证
    """
    data = db_handler.db_handler(account)
    if data is not None:
        # print(data)
        if data['password'] == password:
            exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
            if time.time() > exp_time_stamp:
                print("账户 %s 已过期，请重新申请新卡！" %account)
            else:
                print("登录成功！")
                return data
        else:
            print("用户名或密码错误，请重试！")
    else:
        print("用户名不存在，请重试！")

def acc_login(user_data,log_obj):
    """登录过程"""
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("用户名：").strip()
        password = int(input("密码：").strip())
        data = acc_auth(account,password)
        if data:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            log_obj.info("账户: %s登陆成功"%user_data['account_id'])
            return data
        retry_count += 1
    else:
        log_obj.error("尝试次数过多，请稍后再试！")
        exit()

# if __name__ == '__main__':
#     log_obj = logger.logger('login')
#     user_data = {'is_authenticated': False}
#     acc_login(user_data, log_obj)




