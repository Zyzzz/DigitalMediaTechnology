# tf-faster-rcnn
Tensorflow Faster R-CNN for Windows by using Python 3.5 

This is the branch to compile Faster R-CNN on Windows. It is heavily inspired by the great work done [here](https://github.com/smallcorgi/Faster-RCNN_TF) and [here](https://github.com/rbgirshick/py-faster-rcnn). I have not implemented anything new but I fixed the implementations for Windows and Python 3.5.

### PLEASE BE AWARE: I do not have time or intention to fix all the issues for this branch as I do not use it commercially. I created this branch just for fun. If you want to make any commitment, it is more than welcome. Tensorflow has already released an object detection api. Please refer to it. https://github.com/tensorflow/models/tree/master/research/object_detection


# How To Use This Branch
1- Install tensorflow, preferably GPU version. Follow [instructions]( https://www.tensorflow.org/install/install_windows). If you do not install GPU version, you need to comment out all the GPU calls inside code and replace them with relavent CPU ones.

2- Install python packages (cython, python-opencv, easydict)

3- Checkout this branch

4- Go to  ./data/coco/PythonAPI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run `python setup.py build_ext --inplace`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run `python setup.py build_ext install`

5- Follow this instruction to download PyCoco database. [Link]( https://github.com/rbgirshick/py-faster-rcnn#beyond-the-demo-installation-for-training-and-testing-models)

I will be glad if you can contribute with a batch script to automatically download and fetch. The final structure has to look like

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"data/VOCDevkit2007/annotations_cache"
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"data/VOCDevkit2007/VOC2007"
  
 6- Download pre-trained VGG16 from [here](http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz) and place it as "data\imagenet_weights\vgg16.ckpt"
 
 For rest of the models, please check [here](https://github.com/tensorflow/models/tree/master/research/slim#pre-trained-models)
 
  7- Run train.py
  
  Notify me if there is any issue found. Please note that, I have compiled cython modules with sm61 architecture (GTX 1060, 1070 etc.). Compile support for other architectures will be added. 
 

安装cython, python-opencv, easydict，pycoco
预训练模型：
链接：https://pan.baidu.com/s/1zUZRZyitKrxlFgQ73ZW-nw 
提取码：ws12 

放入Faster_RCNN\data\imagenet_weights
模型地址：
链接：https://pan.baidu.com/s/1OXug3kxk4dK8hwZvaeluKw 
提取码：bqsx 

将default文件夹中的四个模型文件存入Faster_RCNN\default\voc_2007_trainval\default\（没有就创建）
修改模型地址在test.py的模型绝对路径在122行
运行test.py