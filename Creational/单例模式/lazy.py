# -*- coding: utf-8 -*-
# @Time : 2023/3/30 14:47
# @Author : Morpheus
# @File : lazy.py
# @Software: PyCharm
# @desc: 懒汉式加载 只有在有需要的时候才创建实例


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("正在初始化...")
        else:
            print("已构建实例", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


if __name__ == "__main__":
    a = Singleton()

    # 在这一步调用的时候才创建了实例，我们可以很容易地看出这一步的内存地址和下面对象的内存地址相同
    print(Singleton.getInstance())
    b = Singleton()

