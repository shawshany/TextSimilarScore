#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-12 14:04
# @Author   : 病虎
# @E-mail   : victor.xsyang@gmail.com
# @File     : TextSimilarTest.py
# @User     : ora
# @Software: PyCharm
#Reference:**********************************************
import TextSimilarScore.tools.TextSim as ts
import importlib
importlib.reload(ts)
test = ts.TextSimilarity('中移在线全链路智能化系统研发项目', '中移在线全国智能路由决策项目')

print(test.lcs())