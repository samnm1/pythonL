# _*_ coding: utf-8 _*_
from __future__ import division  #  整数除法（非地板除）必须在文件的开头
import types
import json
from collections   import  Iterable
import os
import  sys, shelve


#基础类型
    #所有的Python 对象都拥有三个特性：身份，类型和值。

    #print cmp(1, -5) 比较两个数值 大于是1  等于 0   小于 -1     
    #print repr(obj)  用于解释器阅读的字符串性
    #print str(obj)   用于友好性阅读

    #可变类型 列表， 字典
    #不可变类型 数字、字符串、元组

    #访问模型  Python 类型*******************
    #直接访问 数字
    #顺序访问 字符串、列表、元组
    #映射访问 字典 **************************
    # Decimal   十进位浮点型  适合货币单位
    # 元组(,), 列表[,], 字典{key:value,key:value}

    # 数据类相关模块   decimal、array高效数学数组、math/cmath复数包含
    # 三引号  所见即所得的string处理
    # 浅拷贝是对象类型一样，内容是引用（list,dict,copy）, 深拷贝需要使用  import copy.deepcopy函数
    # 字典 哈希 {key:value,key:value}  dict()
    # print  json.dumps(fdict,ensure_ascii=False,encoding='utf-8') 打印字典中文
    # 字典比较大小cmp(), 解释器顺序  字典长度->键 -> 值
    # hash() 判断是否能成为字典的键key
    # *性能* ：直接迭代序列要比索引迭代快
    # 列表解析表达式->动态创建一个列表list对象  语法： [expr for iter_var in iterable if cond_expr]
    # 生成器表达式->生成器是特定的函数, 允许你返回一个值  语法： (expr for iter_var in iterable if cond_expr)
    # *性能* ：生成器性能优于列表解析表达式

#文件与输入输出
    # 使用open 操作文件，使用file对象判断文件
    # import os 文件系统
    # *性能*：尽可能用迭代器遍历文件
    # 序列化对象  import  pickle.dump(obj,file[,protocol])  load(file)
    # dbm模块，允许提供一个持久字典dbm来存储名称和值，类似java.util.map 
    # dbm常用的dbm模块， dbm.dumb可移植，简单的dbm库， dbm.gnu  GNU dbm库
    # shelve提供对象序列化及存储转化， 步骤：shelve -> anydbm ->cpickle
    # assert断言，测试表达式 

#异常
    #语法：try-except-else-finally:
    #内建所有错误Exception , 所有错误 BaseException
    #except 参数，except (Exception1, Exception2, ..., ExceptionN)[, reason]:
    #上下文管理 with context_expression [as target(s)]:
    #


class Sample:
    def __enter__(self):
        return self
    def __exit__(self,type,value,trace):
        print 'type:',type
        print 'value:',value
        print 'trace:',trace
    def do_something(self):
        bar=1/1
        return bar+10
with Sample() as sample:
    sample.do_something()




try:
    float('12323%abc')
except :
    import sys
    print  sys.exc_info()

print '继续...........'

