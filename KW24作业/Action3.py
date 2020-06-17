"""
Action3:对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem的类型
Step3,数据统计
品牌投诉总数
车型投诉总数
哪个品牌平均车型投诉最多
"""


import pandas as pd
#数据加载
result = pd.read_csv('car_complain.csv')
# print(result)
# # 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
tags = result.columns[7:]
print(tags)
#统计各品牌投诉总数
df= result.groupby(['brand'])['id'].agg(['count'])
print(df)
# #统计各车型投诉总数
df2= result.groupby(['car_model'])['id'].agg(['count'])
print(df2)
# #统计各品牌包含车型数量
df3=result.groupby(['brand','car_model'])['id'].agg(['count'])
print(df3)
# #连接表格并计算各品牌每个车型的平均投诉量
df4=df.merge(df3, left_index=True, right_index=True, how='left')
# print(df4)
df4['average']=df4['count_x']/df4['count_y']
print(df4)
df4.to_csv('temp2.csv')
df4=df4.sort_values('average',ascending=False)
print(df4)