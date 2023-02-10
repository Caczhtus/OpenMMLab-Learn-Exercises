## 任务描述

本次任务主要基于抽烟目标数据集训练目标检测模型，主要采用的 `YOLOV3` 进行训练

## 实验环境

GTX 3090 + 24 核 CPU

batchsize：16（可以设到 48）

## 数据集

https://aistudio.baidu.com/aistudio/datasetdetail/94796

### 数据集操作的脚本

1. 划分数据集
2. 获取类别列表

## 验证结果

|                   Model                   |  mAP   | mAP_50 |
| :---------------------------------------: | :----: | :----: |
| yolov3_mobilenetv2_mstrain-416_30e_bloods | 0.8768 | 0.8770 |

## 相关文件

配置文件：[yolov3_mobilenetv2_mstrain-416_30e_bloods.py](./config/yolov3_mobilenetv2_mstrain-416_30e_bloods.py)

日志文件：[20230210_175449.log](./work_dirs/yolov3/yolov3_mobilenetv2_mstrain-416_30e_bloods/20230210_175449.log)

权重文件：[latest.pth](./work_dirs/yolov3/yolov3_mobilenetv2_mstrain-416_30e_bloods/latest.pth)

## 遇到的问题

1. VOC的数据集整理问题：
   1. 根目录要为 VOC2007 或 VOC2012

   2. classes 要记得赋值

   3. 要有 `ImageSets` 的文件，注意目录结构：

      1. ```
         ├─Annotations                                                                                     ├─ImageSets                                                                                       │  └─Main
         └─JPEGImags
         ```

2. 非 COCO 数据集评价指标没有 `bbox`，要直接改成 `mAP`：https://github.com/open-mmlab/mmdetection/issues/2705