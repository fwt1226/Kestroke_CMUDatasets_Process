# Kestroke_CMUDatasets_Process

Keystroke Dynamics - Benchmark Data Set ：http://www.cs.cmu.edu/~keystroke/

CMUDatasets：
51个用户
每个用户分8次输入，每次输入50遍，一共输入400遍。
固定密码：（.tie5Roanl）

对该数据集的excel文件进行处理：
按行读取excel文件，每400行属于一个对象，分对象生成51个json文件；
将每个对象的json文件按不同特征再分为3个json文件；
3个特征：KeyHoldTime/Up-DownTime/Down-DownTime。
