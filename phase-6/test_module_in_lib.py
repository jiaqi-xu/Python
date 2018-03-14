# -*- encoding: utf-8 -*-

obj = __import__('lib.account', fromlist=True)
print(obj)

obj.login()


