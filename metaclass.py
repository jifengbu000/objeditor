# -*- coding: utf-8 -*-
import attr

class MetaClass(type):

	FORBIDEN_FIELD_NAMES = ["_data_dict_","_data_name_","_attr_dict_"]

	def __new__(cls, name, bases, attrs):
		attr_fields = {}
		for attr_name, attr_value in attrs.items():
			if not isinstance(attr_value, attr.BaseAttr):
				continue
			if attr_name in cls.FORBIDEN_FIELD_NAMES:
				raise Exception("%s cannot be a attr name"%attr_name)
			attr_fields[attr_name] = attr_value
			attr_value.name = attr_name
			del attrs[attr_name]

		attrs['_attr_dict_'] = attr_fields

		return super(MetaClass, cls).__new__(cls, name, bases, attrs)

