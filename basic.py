# _*_ coding: utf-8 _*_
from __future__ import division  #  整数除法（非地板除）必须在文件的开头
import types
import  json


#类型
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

    # 数据类相关模块   decimal、array高效数学数组、math/cmath复数包含
    # 三引号  所见即所得的string处理
    # 浅拷贝是对象类型一样，内容是引用（list,dict,copy）, 深拷贝需要使用  import copy.deepcopy函数
    # 字典 哈希 {key:value,key:value}  dict()
    # 序列化对象  import  pickle.dump(obj,file[,protocol])  load(file)
    # print  json.dumps(fdict,ensure_ascii=False,encoding='utf-8') 打印字典中文
    # 字典比较大小cmp(), 解释器顺序  字典长度->键 -> 值
    # hash() 判断是否能成为字典的键key
    # *性能* ：直接迭代序列要比索引迭代快
    # 列表解析，动态创建一个列表  语法： [expr for iter_var in iterable if cond_expr]
    

print  range(8)
print  [(x**2)  for  x  in range(8)  if (x**2)!=4 and  x!=4]

