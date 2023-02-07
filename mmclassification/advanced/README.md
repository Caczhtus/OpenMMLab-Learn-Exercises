# 实验说明

使用 vision transformer base patch 16 对血细胞数据集数据集进行训练 30 轮，使用 cos 对学习率进行调整



## 数据集介绍

该数据集包含12,500个血细胞增强图像，并带有伴随的细胞类型标签。每种4种不同的细胞类型大约有3,000张图像，这些图像分为4个不同的文件夹（根据细胞类型）。细胞类型是嗜酸性粒细胞，淋巴细胞，单核细胞和嗜中性粒细胞。文件夹`dataset-master`包含410个带有子类型签和边界框（JPEG + XML）的血细胞图像，而文件夹`dataset2-master`的TRAIN文件中每个种类细胞包含大约2500个增强图像。 我们主要使用`dataset2-master`对细胞进行分类

## 数据集链接

[数据集链接](https://aistudio.baidu.com/aistudio/datasetdetail/106627/0)



## 相关文件

- 权重文件：[下载链接](https://www.aliyundrive.com/s/3Vqk3n8gwJK)         密码：`94zq`

- 日志文件：`20230207_122335.log`
- 精度文件：`20230207_122335.log.json`
- 配置文件：`vit-base-p16_pt-1xb256_bloods-224.py`

