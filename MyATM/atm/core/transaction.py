# coding=utf-8
# __author__ = "Devlee"

"""交易模块"""

# import os
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from core import logger
from core import accounts

def make_transaction(log_obj,account_data,amount,tran_type,**others):
    """负责交易逻辑及日志输出"""
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount -interest
            if new_balance < 0:
                print('您的额度已不足！')
                return account_data  # 直接返回，不写入
        account_data['balance'] = new_balance
        accounts.dump_data(account_data)
        log_obj.info("账户:%s     项目:%s       金额%s    利息%s        "%(account_data['id'], tran_type, amount, interest))
        return account_data
    else:
        print("不支持的交易类型！")

# if __name__ == '__main__':
#     lg = logger.logger('transaction')
#     data = {
#         "id": 'wmm',
#         "password": 666666,
#         "credit": 15000,
#         "balance": 15000,
#         "enroll_date": "2018-04-21",
#         "expire_date": "2050-01-01",
#         "pay_day": 9,
#         "status": 0
#     }
#     make_transaction(lg,data,1000,'repay')
