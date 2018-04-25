# coding=utf-8
# __author__="Devlee"

import json

acc_data = {
    'id': 12345,
    'password': 666666,
    'credit': 15000, # 可用额度
    'balance': 15000, # 可用余额
    'enroll_date': '2018-04-21',
    'expire_date': '2050-01-01',
    'pay_day': 9, # 还款日
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_data))