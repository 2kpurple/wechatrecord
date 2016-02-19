# coding=utf-8
# @Author: 2kpurple
# @Date: 2016-2-18 17:47

"""
数据库解析器基类
"""


class DBParser:

    def __init__(self, path, mode):
        """
        :param path: 聊天记录所在目录
        :param mode: 解析模式 1为解析朋友列表 2为解析记录列表
        """
        self.path = path
        self.mode = mode

    def parse(self):
        """
        解析微信数据库
        :return: 微信对象
        """
        pass

    def parseUser(self):
        

    def _parse_friends_list(self):
        """
        解析朋友列表
        :return: 返回朋友列表
        """
        pass

    def _parse_history_list(self):
        """
        解析历史记录列表
        :return: 返回历史记录列表
        """
        pass
