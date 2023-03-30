# -*- coding: utf-8 -*-
# @Time : 2023/3/30 15:10
# @Author : Morpheus
# @File : monostate.py
# @Software: PyCharm
# @desc: 单态模式 所有该类的对象共享同一种状态

"""
实现的关键在于__dict__方法，Python使用dict方法存放一个类所有对象的状态
"""

class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


class Bord_new(object):
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Bord_new, cls).__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj

    def __init__(self):
        self.name = None


if __name__ == "__main__":
    b = Borg()
    b1 = Borg()
    print(b.__dict__)
    print(b1.__dict__)

    b.x = 100
    print(b.__dict__)
    print(b1.__dict__)

    bn = Bord_new()
    bn2 = Bord_new()
    print(bn.__dict__)
    print(bn2.__dict__)
    bn2.name = "licheng"
    print(bn.__dict__)
    print(bn2.__dict__)

