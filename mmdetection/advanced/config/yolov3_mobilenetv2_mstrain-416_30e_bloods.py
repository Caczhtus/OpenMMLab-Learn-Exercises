_base_ = ['./_base_/yolov3_mobilenetv2_mstrain-416_300e_coco.py']

model = dict(bbox_head=dict(num_classes=1))

dataset_type = 'VOCDataset'
classes=('smoke',)
data= dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    train = dict(
        dataset= dict(
            type='VOCDataset',
            classes = classes,
            ann_file='/openbayes/input/VOC2007/ImageSets/Main/train.txt',
            img_prefix='/openbayes/input/VOC2007/'
        ) 
    ),
    val=dict(
        type='VOCDataset',
        classes = classes,
        ann_file='/openbayes/input/VOC2007/ImageSets/Main/val.txt',
        img_prefix='/openbayes/input/VOC2007/'
    ),
    test=dict(
        type='VOCDataset',
        classes = classes,
        ann_file='/openbayes/input/VOC2007/ImageSets/Main/test.txt',
        img_prefix='/openbayes/input/VOC2007/'
    )
)

runner = dict(type='EpochBasedRunner', max_epochs=30)
work_dir = 'work_dirs/yolov3/yolov3_mobilenetv2_mstrain-416_30e_bloods/'
checkpoint_config = dict(interval=2, max_keep_ckpts=2)
load_from = 'config/_base_/yolov3_mobilenetv2_mstrain-416_300e_coco_20210718_010823-f68a07b3.pth'
evaluation = dict(interval=1, metric=['mAP'])  #https://github.com/open-mmlab/mmdetection/issues/2705


