# coding: utf-8
# In[1]:

import os
import math
import random
from PIL import Image

import numpy as np
import tensorflow as tf
import cv2
import keras.backend as K
slim = tf.contrib.slim

# In[2]:
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# In[3]:

import sys

sys.path.append('./')

# In[4]:

from SSD.nets import ssd_vgg_300, ssd_common, np_methods
from SSD.preprocessing import ssd_vgg_preprocessing
from SSD.notebooks import visualization




# ## Post-processing pipeline
#
# The SSD outputs need to be post-processed to provide proper detections. Namely, we follow these common steps:
#
# * Select boxes above a classification threshold;
# * Clip boxes to the image shape;
# * Apply the Non-Maximum-Selection algorithm: fuse together boxes whose Jaccard score > threshold;
# * If necessary, resize bounding boxes to original image shape.

# In[7]:

# Main image processing routine.
def process_image(img, select_threshold=0.5, nms_threshold=.45, net_shape=(300, 300)):
    # In[5]:

    # TensorFlow session: grow memory when needed. TF, DO NOT USE ALL MY GPU MEMORY!!!
    gpu_options = tf.GPUOptions(allow_growth=True)
    config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
    isess = tf.InteractiveSession(config=config)
    # ## SSD 300 Model
    #
    # The SSD 300 network takes 300x300 image inputs. In order to feed any image, the latter is resize to this input shape (i.e.`Resize.WARP_RESIZE`). Note that even though it may change the ratio width / height, the SSD model performs well on resized images (and it is the default behaviour in the original Caffe implementation).
    #
    # SSD anchors correspond to the default bounding boxes encoded in the network. The SSD net output provides offset on the coordinates and dimensions of these anchors.

    # In[6]:

    # Input placeholder.
    net_shape = (300, 300)
    data_format = 'NHWC'
    img_input = tf.placeholder(tf.uint8, shape=(None, None, 3))
    # Evaluation pre-processing: resize to SSD net shape.
    image_pre, labels_pre, bboxes_pre, bbox_img = ssd_vgg_preprocessing.preprocess_for_eval(
        img_input, None, None, net_shape, data_format, resize=ssd_vgg_preprocessing.Resize.WARP_RESIZE)
    image_4d = tf.expand_dims(image_pre, 0)

    # Define the SSD model.
    reuse = True if 'ssd_net' in locals() else None
    ssd_net = ssd_vgg_300.SSDNet()
    with slim.arg_scope(ssd_net.arg_scope(data_format=data_format)):
        predictions, localisations, _, _ = ssd_net.net(image_4d, is_training=False, reuse=reuse)

        # Restore SSD model.
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    CKPT_DIR = os.path.join(ROOT_DIR, "checkpoints")
    ckpt_filename = os.path.join(CKPT_DIR, "ssd_300_vgg.ckpt")
    # ckpt_filename = '../checkpoints/VGG_VOC0712_SSD_300x300_ft_iter_120000.ckpt'
    isess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(isess, ckpt_filename)

    # SSD default anchor boxes.
    ssd_anchors = ssd_net.anchors(net_shape)
    # Run SSD network.
    rimg, rpredictions, rlocalisations, rbbox_img = isess.run([image_4d, predictions, localisations, bbox_img],
                                                              feed_dict={img_input: img})
    isess.close()
    K.clear_session()
    tf.reset_default_graph()
    # Get classes and bboxes from the net outputs.
    rclasses, rscores, rbboxes = np_methods.ssd_bboxes_select(
        rpredictions, rlocalisations, ssd_anchors,
        select_threshold=select_threshold, img_shape=net_shape, num_classes=21, decode=True)

    rbboxes = np_methods.bboxes_clip(rbbox_img, rbboxes)
    rclasses, rscores, rbboxes = np_methods.bboxes_sort(rclasses, rscores, rbboxes, top_k=400)
    rclasses, rscores, rbboxes = np_methods.bboxes_nms(rclasses, rscores, rbboxes, nms_threshold=nms_threshold)
    # Resize bboxes to original image shape. Note: useless for Resize.WARP!
    rbboxes = np_methods.bboxes_resize(rbbox_img, rbboxes)

    return rclasses, rscores, rbboxes


# In[21]:
def dome(filename,classes):

# Test on some demo image and visualize output.
#     ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
#     path = os.path.join(ROOT_DIR, "demo")
#     image_names = sorted(os.listdir(path))
    img = mpimg.imread(filename)
    rclasses, rscores, rbboxes = process_image(img)
    str = visualization.bboxes_draw_on_img(img, rclasses, rscores, rbboxes, visualization.colors_plasma,classes)
    #plt.imshow(img) # 显示图片
    #plt.show()
    im = Image.fromarray(img)
    im.save('D:\\result3.jpg')
#dome('I:/yolo_tensorflow/test/person.jpg',[])
    return str