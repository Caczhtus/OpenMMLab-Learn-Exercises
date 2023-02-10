# coding:utf-8
# 训练集验证集测试集设置并存储在imagesets里面的train.txt,val.txt等
import os
import random
import argparse
 
parser = argparse.ArgumentParser()
# xml文件的地址，根据自己的数据进行修改 xml一般存放在Annotations下
parser.add_argument('--xml_path', default='Annotations', type=str, help='input xml label path')
# 数据集的划分，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default='ImageSets/Main', type=str, help='output txt label path')
opt = parser.parse_args()
 
# 0.81:0.09:0.1为训练集：验证集：测试集
trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path
total_xml = os.listdir(xmlfilepath)    # 记录xmlfilepath下的所有文件，不要有其他格式的文件
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)
 
num = len(total_xml)    # 统计xmlfilepath下的文件数量，注意不要有其他的文件，以免多统计
list_index = range(num)
tv = int(num * trainval_percent)	# 训练验证集的数量
tr = int(tv * train_percent)	# 训练集的数量
trainval = random.sample(list_index, tv)	
train = random.sample(trainval, tr)
 
file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')
 
for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)
 
file_trainval.close()
file_train.close()
file_val.close()
file_test.close()