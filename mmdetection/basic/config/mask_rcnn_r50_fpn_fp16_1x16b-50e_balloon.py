_base_ = ['./_base_/mask_rcnn_r50_fpn_fp16_1x_coco.py']

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)
    )
)

classes=('balloon',)  # 重要
dataset_type='CocoDataset'
dataset_root='/openbayes/input/input0/balloon/'
data= dict(
    samples_per_gpu=16,
    workers_per_gpu=4,
    train = dict(
        type=dataset_type,
        classes = classes,
        ann_file = '/openbayes/input/output0/balloon/train_via_region_data.json',
        img_prefix=dataset_root + 'train/'
    ),
    val=dict(
        type=dataset_type,
        classes = classes,
        ann_file = '/openbayes/input/output0/balloon/val_via_region_data.json',
        img_prefix=dataset_root + 'val/'
    ),
    test=dict(
        type=dataset_type,
        classes = classes,
        ann_file = '/openbayes/input/output0/balloon/val_via_region_data.json',
        img_prefix=dataset_root + 'val/',
    )
)

runner = dict(type='EpochBasedRunner', max_epochs=50)
work_dir = 'work_dirs/mask_rcnn/mask_rcnn_r50_fpn_fp16_1x16b-50e_balloon/'
checkpoint_config = dict(interval=2, max_keep_ckpts=2)
log_config = dict(interval=25, hooks=[dict(type='TextLoggerHook')])
lr_config = dict(policy='step', step=[8, 16, 32, 48])
load_from = 'config/_base_/mask_rcnn_r50_fpn_fp16_1x_coco_20200205-59faf7e4.pth'

