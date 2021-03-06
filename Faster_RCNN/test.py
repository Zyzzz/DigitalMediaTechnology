#!/usr/bin/env python

# --------------------------------------------------------
# Tensorflow Faster R-CNN
# Licensed under The MIT License [see LICENSE for details]
# Written by Xinlei Chen, based on code from Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from Faster_RCNN.lib.config import config as cfg
from Faster_RCNN.lib.utils.nms_wrapper import nms
from Faster_RCNN.lib.utils.test import im_detect
#from nets.resnet_v1 import resnetv1
from Faster_RCNN.lib.nets.vgg16 import vgg16

CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('vgg16.ckpt',), 'res101': ('res101_faster_rcnn_iter_110000.ckpt',)}
DATASETS = {'pascal_voc': ('voc_2007_trainval',), 'pascal_voc_0712': ('voc_2007_trainval+voc_2012_trainval',)}


def vis_detections(class_name, dets,classes,ax,thresh=0.5):
    """Draw detected bounding boxes."""
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return ''
    if class_name not in classes:
        return ''
    str1=''
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]
        if score<0.6:
            continue
        str1+=str(class_name)+':'+str(score)+' '
        ax.add_patch(
            plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1], fill=False,
                          edgecolor='red', linewidth=3.5)
        )
        ax.text(bbox[0], bbox[1] - 2,
                '{:s} {:.3f}'.format(class_name, score),
                bbox=dict(facecolor='blue', alpha=0.5),
                fontsize=14, color='white')
    plt.axis('off')
    plt.tight_layout()
    plt.draw()
    return str1

def demo(sess, net, image_name,classes):
    """Detect object classes in an image using pre-computed object proposals."""

    # Load the demo image
    im_file = image_name
    im = cv2.imread(im_file)

    # Detect all object classes and regress object bounds
    scores, boxes = im_detect(sess, net, im)
    # Visualize detections for each class
    CONF_THRESH = 0.1
    NMS_THRESH = 0.1
    fig, ax = plt.subplots(figsize=(12, 12))
    im = im[:, :, (2, 1, 0)]
    ax.imshow(im, aspect='equal')
    str=''
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1  # because we skipped background
        cls_boxes = boxes[:, 4 * cls_ind:4 * (cls_ind + 1)]
        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        dets = dets[keep, :]
        str+=vis_detections(cls, dets, classes,ax,thresh=CONF_THRESH)
    return str

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16 res101]',
                        choices=NETS.keys(), default='vgg16')
    parser.add_argument('--dataset', dest='dataset', help='Trained dataset [pascal_voc pascal_voc_0712]',
                        choices=DATASETS.keys(), default='pascal_voc')
    args = parser.parse_args()

    return args


def dectect(filename,claesses):
    args = parse_args()

    # model path
    demonet = args.demo_net
    dataset = args.dataset
    tfmodel = r'C:\Projects\Pycharm\DigitalMediaTechnology\Faster_RCNN\default\voc_2007_trainval\default\vgg16_faster_rcnn_iter_40000.ckpt'


    if not os.path.isfile(tfmodel + ".meta"):
        print(tfmodel)
        raise IOError(('{:s} not found.\nDid you download the proper networks from '
                       'our server and place them properly?').format(tfmodel + '.meta'))

    # set config
    tfconfig = tf.ConfigProto(allow_soft_placement=True)
    tfconfig.gpu_options.allow_growth = True

    # init session
    sess = tf.Session(config=tfconfig)
    # load network
    if demonet == 'vgg16':
        net = vgg16(batch_size=1)
    # elif demonet == 'res101':
        # net = resnetv1(batch_size=1, num_layers=101)
    else:
        raise NotImplementedError
    net.create_architecture(sess, "TEST", 21,
                            tag='default', anchor_scales=[8, 16, 32])
    saver = tf.train.Saver()
    saver.restore(sess, tfmodel)

    print('Loaded network {:s}'.format(tfmodel))

    #im_names = ['000456.jpg', '000457.jpg', '000542.jpg', '001150.jpg',
      #          '001763.jpg', '004545.jpg']


    str = demo(sess, net, filename,claesses)
    plt.savefig(r'D:\result4.jpg', format='jpg', transparent=True, pad_inches=0,dpi=300, bbox_inches='tight')
    #plt.show()
    return str

#print(dectect(r'I:\yolo_tensorflow\test\person.jpg',["person",'dog']))
