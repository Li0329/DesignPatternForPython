# -*- coding: utf-8 -*-
# @Time : 2023/3/31 11:52
# @Author : Morpheus
# @File : Simple_Factory.py
# @Software: PyCharm
# @desc: 简单工厂模式的实现



"""
允许接口创建对象，但是不会暴露对象的创建逻辑
"""

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Cat(Animal):
    def do_say(self):
        print("meow")


class Dog(Animal):
    def do_say(self):
        print("woof")

# 定义一个森林工厂
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
