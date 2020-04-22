import xlrd
import json
import os
import jsonlines

# 按行读取excel文件，每400行生成一个json文件

#创建一个文件夹存放json文件
def createDirectoryStructure():
	directory = 'CMUDataRow'
	if not os.path.exists(directory):
		os.makedirs(directory)

def processText(eachsubject,newfile):
    book = xlrd.open_workbook('datarow.xls') # 读取表格
    sheet1 = book.sheets()[0] # 读取sheet1

	# subject1读取1-400行生成json文件，subject2读取401-800行生成json文件，以此类推
    for i in range(400*(eachsubject-1)+1,400*eachsubject+1):
        rowdata = sheet1.row_values(i) # 读取表中第i行

        with open(newfile, 'a') as f:
            json.dump(rowdata, f)
            f.write('\n')

def dataCleanup():
	createDirectoryStructure()
	# 生成51个json文件存入文件夹
	for eachsubject in range(1,52):
		newfile = ['CMUDataRow/subject{0}.json'.format(eachsubject)]
		processText(eachsubject,newfile[0])
		print()

if __name__ == '__main__':
	dataCleanup()