# coding=utf-8
# __author__="Devlee"

"""主逻辑模块，负责交互界面"""
import time

from core import auth
from core.auth import login_required
from core import accounts
from core import logger
from core import transaction

trans_logger = logger.logger('transaction')
login_logger = logger.logger('login')

login_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def account_info(account_data):
    """账户信息"""
    for key in account_data.keys():
        print(key,account_data[key],sep='\t\t')

@login_required
def repay(account_data):
    """还款"""
    account_data = account_data['account_data']
    account_data = accounts.load_data(account_data['id'])   # 保证读取到最新的数据
    print("您的余额：%s"%account_data['balance'])
    repay_amount = float(input("请输入要还款的金额：").strip())
    if repay_amount > 0:
        new_data= transaction.make_transaction(trans_logger,account_data,repay_amount,'repay')
        if new_data:
            print("您的余额：%s"%new_data['balance'])
        else:
            print('交易失败！')

def withdraw(account_data):
    """取款"""
    account_data = account_data['account_data']
    account_data = accounts.load_data(account_data['id'])
    print("您的余额：%s" % account_data['balance'])
    withdraw_amount = float(input("请输入取款金额：").strip())
    if withdraw_amount < account_data['balance'] and withdraw_amount > 0:
        new_data = transaction.make_transaction(trans_logger,account_data,withdraw_amount,'withdraw')
        if new_data:
            print("您的余额：%s"%new_data['balance'])
        else:
            print('交易失败！')

def transfer(acc_data):
    """转账"""
    pass
def pay_check(acc_data):
    """账单"""
    pass
def logout(acc_data):
    """注销"""
    pass

def interactive(acc_data):
    """交互界面"""
    menu = u'''
        ------- My Bank ---------
        \033[32;1m1.  账户信息
        2.  还款(功能已实现)
        3.  取款(功能已实现)
        4.  转账
        5.  账单
        6.  退出
        \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    acc_data = auth.acc_login(login_data,login_logger)
    if login_data['is_authenticated']:
        login_data['account_data'] = acc_data
        interactive(login_data)
