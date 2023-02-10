## 任务描述

本次任务主要基于 `balloon` 数据集训练实力分割模型，主要采用 `HeKaiming` 的 `Mask R-CNN` 进行训练，并最后完成对视频进行逐帧测试的任务

**问题详情**见：[detail](https://github.com/open-mmlab/OpenMMLabCamp/blob/main/AI%20%E5%AE%9E%E6%88%98%E8%90%A5%E5%9F%BA%E7%A1%80%E7%8F%AD/%E4%BD%9C%E4%B8%9A%E4%BA%8C_mmdetection.md)

## 实验环境

GTX 3090 + 24 核 CPU

## 数据集

https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip

## 测试视频

[test_video.mp4](https://github.com/Caczhtus/OpenMMLabCamp/blob/main/AI%20%E5%AE%9E%E6%88%98%E8%90%A5%E5%9F%BA%E7%A1%80%E7%8F%AD/%E4%BD%9C%E4%B8%9A%E4%BA%8C%E8%B5%84%E6%96%99/test_video.mp4)

## 验证结果

|                  Model                   | bbox_mAP | bbox_mAP_50 | bbox_mAP_75 | segm_mAP | segm_mAP_50 | segm_mAP_75 |
| :--------------------------------------: | :------: | :---------: | :---------: | :------: | :---------: | :---------: |
| mask_rcnn_r50_fpn_fp16_1x16b-50e_balloon |  0.6215  |   0.8146    |   0.7643    |  0.7223  |   0.7972    |   0.7914    |

## 相关文件

配置文件：[mask_rcnn_r50_fpn_fp16_1x16b-50e_balloon](./config/mask_rcnn_r50_fpn_fp16_1x16b-50e_balloon.py)

结果视频：[result_video.mp4](./result/result_video.mp4)

权重文件：[链接：https://pan.baidu.com/s/1L2KGhIPRMk6MNCsv7Db_LQ?pwd=r97c 
提取码：r97c](链接：https://pan.baidu.com/s/1L2KGhIPRMk6MNCsv7Db_LQ?pwd=r97c 
提取码：r97c)