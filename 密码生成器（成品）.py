# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-19
# @FileName: 密码生成器（成品）.py
# import random
#
# """根据PEP-8规范调整代码格式"""
# #  定义可选字符集
# LOWERCASES = 'abcdefghijklmnopqrstuvwxyz'
# UPPERCASES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# DIGITS = '0123456789'
# SYMBOLS = '!@#$%&*_-=+'
# SPECIALS = r'~`@#$%^&*()-_=+[{]}\|;:\'",.<>/?'
#
#
# def generate_pwd(length=12, complexity=3):
#     """
#                 生成随机密码。
#                 :param    length:    密码长度，默认为12。
#                 :param    complexity:    密码复杂度，即包含多少种可选字符集，默认为3。
#                                                         例如，复杂度为1则只包含小写字母；复杂度为2则包含小写字母和大写字母。
#                 :return:    返回生成的随机密码。
#                 """
#     charset = ""
#     #  根据复杂度参数拼接可选字符集
#     if complexity >= 1:
#         charset += LOWERCASES
#     if complexity >= 2:
#         charset += UPPERCASES + DIGITS
#     if complexity >= 3:
#         charset += SYMBOLS
#     if complexity >= 4:
#         charset += SPECIALS
#     #  处理复杂度为0的情况
#     if not charset:
#         return ""
#
#     #  打乱字符集顺序
#     charset = list(charset)
#     random.shuffle(charset)
#
#     #  从随机顺序的字符集中选出字符拼接成密码
#     pwd = ''.join(random.choice(charset) for _ in range(length))
#     return pwd
#
#
# #  生成一个长度为20，复杂度为5的密码
# password = generate_pwd(length=20, complexity=5)
# print(password)
# # """
# # 用过的密码：$X2##~U+:4[azX!#MJiL
# # """
"""=================================================================================================================="""
import random
import string


def generate_password():
    """
    生成密码的函数
    """
    password = ''

    # 生成8-16位的密码
    length = random.randint(8, 16)

    # 生成包含字母和数字混合的密码
    while not any(x in password for x in string.ascii_letters) or not any(x in password for x in string.digits):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # 判断是否包含连续的字母或数字，若包含重新生成
    while any(x + y + z in password for x, y, z in
              zip(string.ascii_letters, string.ascii_letters[1:], string.ascii_letters[2:])) \
            or any(x + y + z in password for x, y, z in zip(string.digits, string.digits[1:], string.digits[2:])):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    return password


# 生成密码示例
password = generate_password()
print(password)
"""
广东人社统一认证系统：EN5CWw4CH7dh3F
"""
