import xlrd
import json
from difflib import SequenceMatcher as sm
import os
import jsonlines
import numpy

def createDirectoryStructure():
	directory = 'CMUData'
	if not os.path.exists(directory):
		os.makedirs(directory)

		directory = 'CMUData/Hold'
		if not os.path.exists(directory):
			os.makedirs(directory)
		directory = 'CMUData/UD'
		if not os.path.exists(directory):
			os.makedirs(directory)
		directory = 'CMUData/DD'
		if not os.path.exists(directory):
			os.makedirs(directory)

def processHold(eachsubject,directory,newfile):
	filename = 'CMUDataCol/Hold/subject{0}.json'.format(eachsubject)

	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f] # 遍历读取每一次输入的不同按键数据
		kht = [list(lst) for lst in zip(*data)] # 同样的按键在不同输入的数据集合（行列转换）

		outliers = []

		for coldata in kht: # 同样的按键在不同行的数据列表
			a = numpy.array(coldata)
			q1 = numpy.percentile(a, 25)
			q3 = numpy.percentile(a, 75)
			iqr = q3 - q1

			outliers.extend([index for index, item in enumerate(coldata) if item > q3 + (1.5*iqr) or item < q1 - (1.5*iqr)])
		
		for i,HoldTime in enumerate(data):
			if not i in outliers:
				with open(newfile, 'a') as f:		
					json.dump(HoldTime, f)
					f.write('\n') 

def processUD(eachsubject,directory,newfile):
	filename = 'CMUDataCol/UD/subject{0}.json'.format(eachsubject)

	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f] # 遍历读取每一次输入的不同按键数据
		udt = [list(lst) for lst in zip(*data)] # 同样的按键在不同输入的数据集合（行列转换）

		outliers = []

		for coldata in udt: # 同样的按键在不同行的数据列表
			a = numpy.array(coldata)
			q1 = numpy.percentile(a, 25)
			q3 = numpy.percentile(a, 75)
			iqr = q3 - q1

			outliers.extend([index for index, item in enumerate(coldata) if item > q3 + (1.5*iqr) or item < q1 - (1.5*iqr)])
		
		for i,UDTime in enumerate(data):
			if not i in outliers:
				with open(newfile, 'a') as f:		
					json.dump(UDTime, f)
					f.write('\n') 

def processDD(eachsubject,directory,newfile):
	filename = 'CMUDataCol/DD/subject{0}.json'.format(eachsubject)

	with open(filename, 'r') as f:
		data = [json.loads(line) for line in f] # 遍历读取每一次输入的不同按键数据
		ddt = [list(lst) for lst in zip(*data)] # 同样的按键在不同输入的数据集合（行列转换）

		outliers = []

		for coldata in ddt: # 取出同样的按键在每一行的数据列表
			a = numpy.array(coldata)
			q1 = numpy.percentile(a, 25)
			q3 = numpy.percentile(a, 75)
			iqr = q3 - q1

            # 得到异常值所在行数
			outliers.extend([index for index, item in enumerate(coldata) if item > q3 + (1.5*iqr) or item < q1 - (1.5*iqr)])
		
		for i,DDTime in enumerate(data): # 读取第i行的i值及其数据
			if not i in outliers: # 如果第i行不存在异常值，则存入新文件
				with open(newfile, 'a') as f:		
					json.dump(DDTime, f)
					f.write('\n') 

def deleteoutlier():
	createDirectoryStructure()
	for eachsubject in range(1,52):
		directory = ['CMUData']
		newfile = ['CMUData/Hold/subject{0}.json'.format(eachsubject), 'CMUData/UD/subject{0}.json'.format(eachsubject), 'CMUData/DD/subject{0}.json'.format(eachsubject)]
		processHold(eachsubject,directory, newfile[0])
		processUD(eachsubject,directory, newfile[1])
		processDD(eachsubject,directory, newfile[2])
		print()

if __name__ == '__main__':
	deleteoutlier()