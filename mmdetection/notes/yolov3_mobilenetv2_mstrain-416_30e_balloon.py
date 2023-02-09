_base_ = ['yolov3_mobilenetv2_mstrain-416_300e_coco.py']

model = dict(bbox_head=dict(num_classes=1))

classes=('balloon',)  # 重要
data= dict(
    samples_per_gpu=8,
    workers_per_gpu=4,
    train = dict(
        dataset= dict(
            type='CocoDataset',
            classes = classes,
            ann_file = '/openbayes/input/output0/balloon/train_via_region_data.json',
            img_prefix='/openbayes/input/input0/balloon/train/'
        ) 
    ),
    val=dict(
        type='CocoDataset',
        classes = classes,
        ann_file = '/openbayes/input/output0/balloon/val_via_region_data.json',
        img_prefix='/openbayes/input/input0/balloon/val/'
    ),
    test=dict(
        type='CocoDataset',
        classes = classes,
        ann_file = '/openbayes/input/output0/balloon/val_via_region_data.json',
        img_prefix='/openbayes/input/input0/balloon/val/',
    )
)

runner = dict(type='EpochBasedRunner', max_epochs=30)
work_dir = 'work_dirs/yolov3/yolov3_mobilenetv2_mstrain-416_30e_balloon/'
checkpoint_config = dict(interval=2, max_keep_ckpts=2)
load_from = 'yolov3_mobilenetv2_mstrain-416_300e_coco_20210718_010823-f68a07b3.pth'


