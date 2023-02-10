import glob
import xml.etree.ElementTree as ET
#import xml.dom.minidom
import tqdm
 
# 类名和数量
classes_numbers = {}
 
#xml路径
path = r''
for xml_file in tqdm.tqdm(glob.glob(path + '\*.xml')):
    # 返回解析树
    tree = ET.parse(xml_file)
    # 获取根节点
    root = tree.getroot()
    # 对所有目标进行解析
    for member in root.findall('object'):
        #获取object标签内的name，找不到的话打开xml文件，看看是name还是clasname...
        objectname = member.find('name').text
        classes_numbers[objectname] = classes_numbers.get(objectname,0)+1
print("done")
print(classes_numbers)