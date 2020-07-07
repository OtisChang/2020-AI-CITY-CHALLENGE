#  Pyramid Granularity Attentive Model
Implement of paper:AI City Challenge 2019 – City-Scale Video Analytics for Smart Transportation

## Dependencies

- Python >= 3.6
- PyTorch >= 1.0.0
- torchvision
- scipy
- numpy
- scikit_learn
- tqdm
- glob
- pandas
- visdom
- PIL
- h5py




## Data

VERI
AICity track 2


## Weights

weights/
	pretrain weight: VERI.pth(VERI + ImageNet)
	best weight: pyramid.pth(pretrain完再利用AIcity Data train)

## notice

```
1. when you run code please put the label.csv to the file, ex: put label/AICity/train/label.csv to track 2 train data file
2. label.csv index is id, image name , pose, color
3. the txt will save in save/
4. please run 'python -m visdom.server -port 8098' before you train
5. The folder "AIC20_ReID" should have there sub-floder : "image_train"、"image_test"、"image_query" which has images respectively.
6. 請在main.py的第135行設定pretrained weight(VERI.pth)的絕對路徑
7. 請在utils/metrics.py的第8行，設定train_label_num.txt的絕對路徑

```

## Train

You can specify more parameters in opt.py

```
python main.py --mode train --data_path <your dataset dir> --class_num <dataset id number>

EX : python main.py --mode train --data_path "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310_v2/AIC20_ReID"
```

## Evaluate

```
python3 main.py --mode evaluate -data_path <your dataset dir> --weight <weights/pyramid.pth>

EX : python main.py --mode evaluate --data_path "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310_v2/AIC20_ReID" --weight "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310_v2/weights/pyramid_v1.pth"
```

## AIcity result

```
python main.py --mode aicity --data_path <your dataset dir>

EX : python main.py --mode aicity --data_path "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310_v2/AIC20_ReID"

## Citation

```text
@ARTICLE{Chang19AI,
    author = {{Ming-Ching Chang and Jiayi Wei and Zheng-An Zhu and Yan-Ming Chen and Chan-Shuo Hu and Ming-Xiu Jiang and Chen-Kuo Chiang},
    title = "{{AI} {C}ity {C}hallenge 2019 -- {C}ity-Scale Video Analytics for Smart Transportation}",
    year = 2019,
}
```
