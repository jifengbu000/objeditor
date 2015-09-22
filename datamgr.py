# -*- coding: utf-8 -*-


dataDict = {}

DATA_LIB_DIR = "data"

def load(name):
	global dataDict
	if dataDict.has_key(name):
		return dataDict[name]
	mod = __import__("%s.%s"%(DATA_LIB_DIR,name))
	dataDict[name] = mod.data



def get(name):
	return dataDict.get(name)

