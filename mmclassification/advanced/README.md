# 实验说明

使用 resnet18 对花数据集进行训练100轮，使用step对学习率进行调整，分别在30、60、90轮的地方进行梯度衰减，然而效果并不显著，精度并没有达到很高的程度，其他同学每轮都进行衰减可以到达90以上的 top-1 精度

- `20230205_232234.log`：训练+验证的日志文件
- `epoch_100.pth`：训练 100 轮的权重
- `resnet18_1xb256_flowers.py`：配置文件