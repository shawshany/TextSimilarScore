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
test = ts.TextSimilarity('中移在线全链路智能化系统研发项', '中移在线全国智能路由决策项目')
# 计算连续最长公共子串的距离
print(test.lcs())
# 计算编辑距离
print(test.minimumEditDistance())
# 基于tf-idf计算距离
print(test.splitWordSimlaryty())
# 计算JaccardSim系数
print(test.JaccardSim())