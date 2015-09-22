# -*- coding: utf-8 -*-
import pydata
import attr

class Test(pydata.CPyData):
	_data_name_ = "test"

	id = attr.IntAttr(label="ID")
	a = attr.FloatAttr(label="属性1")
	name = attr.StringAttr(label="名字")



obj = Test.get(1)

print obj.id,obj.a, obj.name

