#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 2kpurple
# @Date: 2016-02-03 17:44
# @Last Modified by:  2kpurple

from setuptools import setup, find_packages


setup(
    name='WeChatRecord',
    version='0.1',
    packages=find_packages(),
    author='2kpurple',
    description='WeChat Chat History Export Tool',
    entry_point={
        'console_scripts': [
            'wechatrecord = wechatrecord:start'
        ]
    }
)
