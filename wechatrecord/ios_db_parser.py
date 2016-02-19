# coding=utf-8
# @Author: 2kpurple
# @Date: 2016-02-04 13:32

"""
微信聊天记录
"""

import sqlite3
import db_parser


class IosDBParser(db_parser):

    def __init__(self, platform, path):
        """
        :param path: 微信聊天记录的文件夹路径
        :param platform: 平台 android or ios
        """

        self.platform = platform
        self.path = path
        # self.db = sqlite
