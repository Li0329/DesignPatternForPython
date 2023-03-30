# -*- coding: utf-8 -*-
# @Time : 2023/3/30 14:42
# @Author : Morpheus
# @File : normal.py
# @Software: PyCharm
# @desc: 一般实现

class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)
