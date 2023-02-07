_base_ = [
    '../_base_/models/vit-base-p32.py',
    '../_base_/datasets/imagenet_bs64_pil_resize_autoaug.py',
    '../_base_/schedules/imagenet_bs4096_AdamW.py',
    '../_base_/default_runtime.py'
]

# model: vit
model = dict(
    head=dict(hidden_dim=3072,
        num_classes=4
    ),
    train_cfg=dict(
        augments=dict(type='BatchMixup', alpha=0.2, num_classes=4,
                      prob=1.))
)

# dataset
dataset_type='CustomDataset'
data = dict(
    samples_per_gpu=256,
    workers_per_gpu=4,
    train=dict(
        type=dataset_type,
        data_prefix='data/dataset-bloods/train',
        ann_file=None),
    val=dict(
        type=dataset_type,
        data_prefix='data/dataset-bloods/val',
        ann_file=None),
    test=dict(
        type=dataset_type,
        data_prefix='data/dataset-bloods/test',
        ann_file=None)
)

evaluation = dict(interval=1, metric='accuracy', metric_options={'topk': (1, )})

# schedule
optimizer_config = dict(grad_clip=dict(max_norm=1.0))
runner = dict(type='EpochBasedRunner', max_epochs=30)

# runtimes
load_from = 'checkpoints/vit-base-p16_3rdparty_pt-64xb64_in1k-224_20210928-02284250.pth'  # fineturn
workflow = [('train', 1)]
work_dir = 'work_dirs/vit/vit-base-p16/vit-base-p16_pt-1xb256_bloods-224/'
gpu_ids = range(0, 1)