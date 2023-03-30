# -*- coding: utf-8 -*-
# @Time : 2023/3/30 15:20
# @Author : Morpheus
# @File : meta.py
# @Software: PyCharm
# @desc: 基于元类实现的单例设计模式

class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
