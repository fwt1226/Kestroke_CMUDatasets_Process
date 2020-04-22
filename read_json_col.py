import xlrd
import json
from difflib import SequenceMatcher as sm
import os
import jsonlines

def createDirectoryStructure():
	directory = 'CMUDataCol'
	if not os.path.exists(directory):
		os.makedirs(directory)

		directory = 'CMUDataCol/Hold'
		if not os.path.exists(directory):
			os.makedirs(directory)
		directory = 'CMUDataCol/UD'
		if not os.path.exists(directory):
			os.makedirs(directory)
		directory = 'CMUDataCol/DD'
		if not os.path.exists(directory):
			os.makedirs(directory)

def processHold(eachsubject,directory,newfile):
	filename = 'CMUDataRow/subject{0}.json'.format(eachsubject)
	with open(filename, 'r') as f:
		for jsonstr in f.readlines():
			data = json.loads(jsonstr)
			HoldTime = (data[0],data[3],data[6],data[9],data[12],data[15],data[18],data[21],data[24],data[27])
			with open(newfile, 'a') as f:		
				json.dump(HoldTime, f)
				f.write('\n') 

def processUD(eachsubject,directory,newfile):
	filename = 'CMUDataRow/subject{0}.json'.format(eachsubject)
	with open(filename, 'r') as f:
		for jsonstr in f.readlines():
			data = json.loads(jsonstr)
			HoldTime = (data[2],data[5],data[8],data[11],data[14],data[17],data[20],data[23],data[26],data[29])
			with open(newfile, 'a') as f:		
				json.dump(HoldTime, f)
				f.write('\n') 

def processDD(eachsubject,directory,newfile):
	filename = 'CMUDataRow/subject{0}.json'.format(eachsubject)
	with open(filename, 'r') as f:
		for jsonstr in f.readlines():
			data = json.loads(jsonstr)
			HoldTime = (data[1],data[4],data[7],data[10],data[13],data[16],data[19],data[22],data[25],data[28])
			with open(newfile, 'a') as f:		
				json.dump(HoldTime, f)
				f.write('\n') 

def dataCleanup():
	createDirectoryStructure()
	for eachsubject in range(1,52):
		directory = ['CMUDataRow']
		newfile = ['CMUDataCol/Hold/subject{0}.json'.format(eachsubject), 'CMUDataCol/UD/subject{0}.json'.format(eachsubject), 'CMUDataCol/DD/subject{0}.json'.format(eachsubject)]
		processHold(eachsubject,directory, newfile[0])
		processUD(eachsubject,directory, newfile[1])
		processDD(eachsubject,directory, newfile[2])
		print()

if __name__ == '__main__':
	dataCleanup()