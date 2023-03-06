from pyecharts.charts import Map
from pyecharts import options as opts
#将数据处理成列表
locate = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','陕西','甘肃','青海','宁夏','新疆']

GDP_1978 = [108.84,82.65,183.06,87.99,58.04,229.20,81.98,174.80,272.81,249.24,123.72,114.10,66.37,87.00,225.45,162.92,151.00,146.99,185.85,75.85,16.40,67.32,184.61,46.62,69.05,81.07,64.73,15.54,13.00,39.07]

GDP_2017 = [28014.94,18549.19,34016.32,15528.42,16096.21,23409.24,14944.53,15902.68,30632.99,85869.76,51768.26,27018,32182.09,20006.31,72634.15,44552.83,35478.09,33902.96,89705.23,18523.26,4462.54,19424.73,36980.22,13540.83,16376.34,21898.81,7459.9,2624.83,3443.56,10881.96]
list1 = [[locate[i],GDP_1978[i]] for i in range(len(locate))]
list2 = [[locate[i],GDP_2017[i]] for i in range(len(locate))]

map_1 = Map()

map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="全国各省GDP"),
    visualmap_opts=opts.VisualMapOpts(max_=100000)  #最大数据范围
    )
map_1.add("2017年各省GDP", list2, maptype="china")
map_1.add("1978年各省GDP", list1, maptype="china")
map_1.render('../templates/map1.html')

a=1
b=1.2
print(a+b)
print(sum(i for i in range(1,101)))
list0=[]
for i in[[1, 2], [3, 4], [5, 6]]:
    for j in i:
        list0.append(j)
print(list0)


#funA 作为装饰器函数
def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"

@funA
def funB():
    print("学习 Python")


# a = input().split(',')
# b = input().split(',')
# c = [int(i) for i in a]
# d = [int(j) for j in b]
# c.extend(d)
# c.sort(reverse=True)
# print((',').join(str(x) for x in c))

# a = input()
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(len(b))

# str_1 = str(input())
# dict_1 = {}
# #循环遍历列表或字符串，如果字符在字典中则值加1，如果不在则创建（key,value)
# for i in str_1:
#     dict_1[i] = dict_1.get(i, 0) + 1
# #打印出出现次数最多的字符
# print(dict_1)
# temp = max(dict_1.values())
# for k, v in dict_1.items():
#     if v == temp:
#         print(v)


str_1 = str(input())
dict_1 = {}
#循环遍历列表或字符串，如果字符在字典中则值加1，如果不在则创建（key,value)
for i in str_1:
    dict_1[i] = dict_1.get(i, 0) + 1
#打印出出现次数最多的字符
print(dict_1)
list=[]
for k, v in dict_1.items():
    if v <=1:
        list.append(k)
print(('').join(str(x) for x in list))
