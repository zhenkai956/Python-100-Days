# 07 笔记 和 练习

# 演示1：
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

print(s1,s1) 
# 看来同一个print()函数中的字符串，默认同行显示

# 字符串运算函数：
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*')) 
# ******************hello, world!*******************

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' ')) 
#                                      hello, world!

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

# 这个应该是“左置顶，右填充”
print(str1.ljust(50, '+')) 
# hello, world!+++++++++++++++++++++++++++++++++++++


# 列表

# 下面的代码演示了如何定义列表、如何遍历列表以及列表的下标运算。


list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 【区别】字符串的乘法合成的是一个字符串

# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)




list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)


# 列表生成式语法
import sys
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数 
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间 112
print(f)
for val in f:
    print(val)


# 集合

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2} # {1, 2, 3}
print(set1) # {1, 2, 3}
print('Length =', len(set1)) # Length = 3
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# {1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3}

# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
# {3, 5, 6, 9, 10, 12, 15, ... 85, 87, 90, 93, 95, 96, 99}

#(续)添加删除元素
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
# {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}
print(set3.pop()) # 【疑问】这把第一个元素分离出来了
# 1
print(set3) # {2, 3}

# 字典

# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4} 
# {'a': '1', 'b': '2', 'c': '3'} 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 通过键可以获取字典中对应的值
print(scores['骆昊']) # 95
print(scores['狄仁杰']) # 82

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
# 骆昊: 95
# 白元芳: 78
# 狄仁杰: 82

# 更新字典中的元素
scores['白元芳'] = 65
scores['诸葛王朗'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
# {'骆昊': 95, '白元芳': 65, '狄仁杰': 82, \
# '诸葛王朗': 71, '冷面': 67, '方启鹤': 85}

if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# None

# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60)) # 60

# 删除字典中的元素
print(scores.popitem()) # ('方启鹤', 85)
print(scores.popitem()) # ('冷面', 67)
print(scores.pop('骆昊', 100)) # 95
print(scores.pop('二百五', 250)) # 250，这个是默认值，否则是报错的
# 清空字典
scores.clear()
print(scores) #{}


