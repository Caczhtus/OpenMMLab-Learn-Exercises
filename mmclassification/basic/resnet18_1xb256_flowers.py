_base_ = [
    # '../_base_/datasets/pipelines/auto_aug.py',
    '../_base_/models/resnet18.py', '../_base_/datasets/imagenet_bs64_autoaug.py',
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]

# model
model = dict(
    head=dict(
        num_classes=5,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, ),
    )
)

# datasets
data = dict(
    samples_per_gpu=256,
    workers_per_gpu=4,
    train=dict(
        data_prefix='data/',
        ann_file='data/dataset-flowers/train.txt',
        classes='data/dataset-flowers/classes.txt'),
    val=dict(
        data_prefix='data/',
        ann_file='data/dataset-flowers/val.txt',
        classes='data/dataset-flowers/classes.txt'),
    test=dict(
        data_prefix='data/',
        ann_file='data/dataset-flowers/val.txt',
        classes='data/dataset-flowers/classes.txt')
)

evaluation = dict(interval=1, metric='accuracy', metric_options={'topk': (1, )})


# schedules
lr_config = dict(policy='step', step=[30, 60, 90])
runner = dict(type='EpochBasedRunner', max_epochs=100) # config epoch
checkpoint_config = dict(interval=10, max_keep_ckpts=3)


# runtimes
load_from = 'checkpoints/resnet18_8xb32_in1k_20210831-fbbb1da6.pth'  # fineturn
workflow = [('train', 1)]
work_dir = 'work_dirs/resnet/resnet18/resnet18_1xb256_flower_fineturn/'
gpu_ids = range(0, 1)



