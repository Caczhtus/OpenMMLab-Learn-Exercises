# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd
 
sets = ['train', 'val', 'test']
classes = ["chilun","luomao","luogan","chachidao","sizhui","gangguan","changxidao","duanxidao"]   # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)
 
def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h
 
def convert_annotation(image_id):
    in_file = open('/media/rjs/文档/xiaolunwen/yolov5-master/VOC/VOC2007/Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('/media/rjs/文档/xiaolunwen/yolov5-master/my_yolo_dataset/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)	# 解析xml文档
    root = tree.getroot()  # 获取根节点
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
wd = getcwd()   # 返回当前进程的工作目录。
for image_set in sets:  # 第一轮image_set为train，第二轮val,第三轮test
    if not os.path.exists('/media/rjs/文档/xiaolunwen/yolov5-master/my_yolo_dataset/labels/'):
        os.makedirs('/media/rjs/文档/xiaolunwen/yolov5-master/my_yolo_dataset/labels/')
    image_ids = open('/media/rjs/文档/xiaolunwen/yolov5-master/VOC/VOC2007/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()   # txt里面的所有图片
    list_file = open('/media/rjs/文档/xiaolunwen/yolov5-master/my_yolo_dataset/%s.txt' % (image_set), 'w')    # 转换过后的列表txt文件位置
    for image_id in image_ids:  # 迭代读取图片的名称，文件名不包括后缀
        list_file.write(abs_path + '/media/rjs/文档/xiaolunwen/yolov5-master/VOC/VOC2007/JPEGImages/%s.jpg\n' % (image_id))   # 在txt文件里面写入图片信息
        convert_annotation(image_id)    # xml转换成标注txt文件
    list_file.close()
 