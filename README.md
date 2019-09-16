# [![Version][version-badge]][version-link] ![MIT License][license-badge]


compute similar scores of two strings

`TextSimilarScore`这是个计算两个短文本相似度的算法

# 安装方法
```pip install TextSimilarScore```

```pip install -r resuirements.txt```
# 使用方法
```
import TextSimilarScore.tools.TextSim as ts
test = ts.TextSimilarity('中移在线全链路智能化系统研发项目', '中移在线全国智能路由决策项目')
# 计算连续最长公共子串的距离
print(test.lcs())
# 计算编辑距离
print(test.minimumEditDistance())
# 基于tf-idf计算距离
print(test.splitWordSimlaryty())
# 计算JaccardSim系数
print(test.JaccardSim())
```