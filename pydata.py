# -*- coding: utf-8 -*-
import metaclass
import datamgr

class CPyData(object):

	__metaclass__ = metaclass
	_data_name_ = None
	_data_dict_ = {}
	_attr_dict_ = {}

	def __init__(self):
		self._data = {}

	@classmethod
	def get(cls,id):
		return cls._data_dict_.get(id)

	@classmethod
	def load(cls):
		for key, data in datamgr.get(cls._data_name_).iteritems():
			obj = cls()
			obj._data = data
			cls._data_dict_[key] = obj
