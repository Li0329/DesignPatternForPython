# -*- coding: utf-8 -*-
# @Time : 2023/3/30 16:14
# @Author : Morpheus
# @File : 单例模式的应用.py
# @Software: PyCharm
# @desc:以维护一个服务器状态检查列表为例

class HealthCheck:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck.__instance:
            HealthCheck.__instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck.__instance

    def __init__(self):
        self._servers = []

    def add_servers(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def change_servers(self):
        self._servers.pop()
        self._servers.append("Server 5")

    @property
    def servers(self):
        return self._servers


if __name__ == "__main__":
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.add_servers()
    for item in hc1.servers:
        print(item)

    print("----分割线----")

    hc2.change_servers()
    for item in hc2.servers:
        print(item)