# _*_ coding: utf-8 _*_
from __future__ import division  #  整数除法（非地板除）必须在文件的开头
import types
import json
from collections   import  Iterable
import os
import  sys, shelve

from operator import add, sub
from random import randint, choice


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
    #上下文管理修饰 contextlib 模块 | from contextlib import contextmanager  |  @contextmanager
    # sys.exc_info() 获取异常信息的途径

#函数

    #函数返回值  None ,  Object  ,  Tuple
    #参数组：func(*tuple_grp_nonkw_args 元组参数, **dict_grp_kw_args 字典参数)
    #完整公式：func(positional_args, keyword_args,*tuple_grp_nonkw_args, **dict_grp_kw_args)
    #匿名函数：lambda为减少代码行 lambda [arg1[, arg2, ... argN]]: expression 在调用时绕过函数的栈分配
    #非关键字可变参数（元组）必须在位置和默认参数之后
    #全局变量想作用于函数内，需加 global
    #生成器 函数内 yield语句，暂停中间返回   next()下一步执行， 迭代属性
    #加强版生成器  next(), send(), close() 双向通讯  ： PEP 的255 和342 中


#模块

    #语法：import  module,  from  module  import  names  as  别名   PEP 221  
    #规范：标准库，第三方库，自定义库  PEP 8  python 风格

#类
    #__init__()类似于类构造器，初始化调用一个实例
    #__dict__属性包含一个字典,dir(),  类函数 派生类->基类 '深度优先搜索'
    #__new__() 在_init_()之前，构造一个实例，主要用于不可变类str、int 、tuple 自定义这些类的实例化过程途径
    #类属性与实例属性的名字空间不同 ,  Class._dict_() instance._dict_()
    #类属性为类似静态属性，new（）实例进类属性_dict_属性字典内
    #实例属性调用初始化类属性，如果被_init_或赋值，则生成新的实例属性
    #当del 当前实例属性后，又调用初始化类属性
    #类函数必须声明 self, 除非强制声明函数类型
    #类静态方法与类方式  staticmethod(foo)、 classmethod(foo)


class  classBYinstance():
    
    CL_attrBy=10
    
    def __init__(self):
        
        self.CL_attrBy=20

    def  MethodA(baby=10):
        
        return  baby

    def  MethodB(self,baby=10):

        return baby

    MethodA=staticmethod(MethodA) 


class Singleton(object):
      def __new__(cls): #cls 类本身
          # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
          if not hasattr(cls, 'instance'):
             cls.instance = super(Singleton, cls).__new__(cls)
             
          return cls.instance
 


if __name__ == '__main__':
    
    obj1 = Singleton()
    obj2 = Singleton()
 
    print obj1 is obj2

    objCL1=classBYinstance()

    objCL1.CL_attrBy=30

    classBYinstance.CL_attrBy=50

    del  objCL1.CL_attrBy

    #******************************************

    print '类函数A' , objCL1.MethodA(20)

    print '类实例函数B' , objCL1.MethodB(20)

    print '类属性：' , classBYinstance.CL_attrBy
    print '实例属性：' , objCL1.CL_attrBy

    

    














     




