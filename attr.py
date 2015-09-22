# -*- coding: utf-8 -*-

class BaseAttr(object):
	def __init__(self, **kwargs):
		self.name = None
		self.label = kwargs.get("label","")

	def __get__(self, instance, owner):
		instance._data.get(self.name)

	def __set__(self, instance, value):
		pass



class IntAttr(BaseAttr):
	pass


class FloatAttr(BaseAttr):
	pass

class StringAttr(BaseAttr):
	pass
