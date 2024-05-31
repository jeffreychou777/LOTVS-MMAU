_base_ ="../../configs/deformable_detr/deformable-detr_r50_16xb2-50e_coco.py"


model = dict(
      bbox_head = dict(num_classes =7 )
)


data_root = '../../data/MM-AU-Detect'
metainfo = {
    'classes': ('motorcycle','truck','bus','traffic light','person','bicycle','car', ),
    'palette': [
        (220, 20, 60),
    ]
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=data_root + '/labels/train.json',
        data_prefix=dict(img='images/train/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=data_root + '/labels/val.json',
        data_prefix=dict(img='images/val/')))
test_dataloader = val_dataloader


val_evaluator = dict(ann_file=data_root + '/labels/val.json')
test_evaluator = val_evaluator

train_cfg = dict(type='EpochBasedTrainLoop',max_epochs=1, val_interval=1)

work_dir = '../../work_dirs/mmaudet_train/def_detr_mmadudet_train'