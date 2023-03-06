# list = [1,2,3,4,5]  # list是可迭代对象
# lterator = iter(list)  # 通过iter()方法取得list的迭代器
# print(next(lterator))  # 1
# print(next(lterator))  # 2
# # print(next(lterator))  # 3
# # print(next(lterator))  # 4
# # print(next(lterator))  # 5
# # print(next(lterator))
# # 生成器函数
# # return: 函数执行的终止
# # yield: 表示函数执行的暂停
# def func02():
#     a = 1
#     yield a
#     b = "hello"
#     yield b
#     c = [1, 2]
#     yield c
# gen2 = func02()
# print("gen2:", gen2)
# # <generator object func02 at 0x7f94da357a98>
# print(gen2.__next__())  # 1
# print(gen2.__next__())  # hello
# for item in gen2:
#     print("for:", item)  # [1, 2]
# gen2.__next__()  # 报错


# import time
#
# from datetime import datetime
#
#
# # 编写一个装饰器，用来装饰test函数
# # 装饰器具有以下功能：
# # 1、test调用时，可以打印是第几次调用
# # 2、test如果多次调用传入的参数相同，则第二次不需要耗时，直接返回结果，即实现简单缓存功能
# # 3、test调用时，可以打印耗时时间
#
#
#
# def test(word):
#     time.sleep(2)
#     return word.upper()
#
#
# if __name__ == '__main__':
#     print(test("hero"))
#     print(test("hero"))
#     print(test("her"))

# import time
# from datetime import datetime
# 编写一个装饰器，用来装饰test函数
# 装饰器具有以下功能：
# 1、test调用时，可以打印是第几次调用
# 2、test如果多次调用传入的参数相同，则第二次不需要耗时，直接返回结果，即实现简单缓存功能
# 3、test调用时，可以打印耗时时间
# count = 0
# cache = {}
# def decorate(fn):
#     def inner(*args, **kwargs):
#         start = time.time()
#         global count
#         global cache
#         # global data
#         if (args, str(kwargs)) in cache.keys():
#             return cache[(args, str(kwargs))]
#             data = fn(*args, **kwargs)
#             cache[(args, str(kwargs))] = data # 这里由于**kwargs是字典，而python字典的Key要是字符串类型,所以就str(kwargs)
#             end = time.time()
#             print("第%d次被调用" % (count))
#             print("耗时时间: ", end - start)
#         return data
#     return inner
#
# @decorate
# def test(word):
#     time.sleep(2)
#     return word.upper()
#
#
# if __name__ == '__main__':
#     print(test("hero"))
#     print(test("hero"))
#     print(test("her"))




# import time
# from datetime import datetime
# count = 0
# a = {}
# def decorate(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         global count
#         count += 1
#         global a
#         if (args, str(kwargs)) in a.keys():
#             return a[(args, str(kwargs))]
#         data = func(*args, **kwargs)
#         a[(args, str(kwargs))] = data
#         end = time.time()
#         print("第%d次被调用" % (count))
#         print("耗时时间: ", end - start)
#         return func
#     return inner
#
# @decorate
# def test(word):
#     time.sleep(2)
#     return word.upper()
#
#
# if __name__ == '__main__':
#     print(test("hero"))
#     print(test("hero"))
#     print(test("her"))





import time
from datetime import datetime
count = 0
a = {}
def decorate(func):
    def inner(*args, **kwargs):
        start = time.time()
        global count
        global a
        count += 1
        if (args, str(kwargs)) in a.keys():
            print("第%d次被调用1" % (count))
            print("dayin")
            return a[(args, str(kwargs))]
        data = func(*args, **kwargs)
        a[(args, str(kwargs))] = data
        end = time.time()
        print("输出")
        print("第%d次被调用2" % (count))
        print("耗时时间: ", end - start)
        return data
    return inner


@decorate
def test(word):
    time.sleep(2)
    return word.upper()


if __name__ == '__main__':
    print(test("hero"))
    print(test("hero"))
    print(test("her"))