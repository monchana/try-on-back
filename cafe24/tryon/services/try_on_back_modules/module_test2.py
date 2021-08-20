import os 
# from namegenerator.src import *
import random
# from tryongenerator.PF_AFN.PF_AFN_test.module import PF_AFN
# from tryongenerator.utils.util_module import TryOnUtils
from tryongenerator.vtp_bottom.bottomUtil import BottomUtil

from tqdm import tqdm
from shutil import copyfile, copytree
from os.path import join as pjoin
import cv2

root_dir = '/home/hsna/workspaces/try-on/try_on_back_modules/examples'

bu = BottomUtil(root_dir=root_dir)

img_paths = [pjoin(root_dir, 'image', img) for img in os.listdir(pjoin(root_dir, 'image'))]

bu.save_keypoints(img_paths)
bu.image_parse(img_paths)
bu.body_masking(img_paths)