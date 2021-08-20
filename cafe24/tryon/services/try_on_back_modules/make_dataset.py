import os
osp = os.path
from os.path import join as pjoin
import random
import numpy as np
import cv2
from tqdm import tqdm

from tryongenerator.utils.util_module import TryOnUtils
from tryongenerator.PF_AFN.PF_AFN_test.module import PF_AFN

target_models = '/data/moncha-museum/viton/dataset/VITON_traindata/VITON_traindata/train_img'
target_product = '/data/moncha-museum/viton/dataset/VITON_traindata/VITON_traindata/train_color'
target_png = '/data/moncha-museum/viton/dataset/VITON_traindata/VITON_traindata/train_edge'
# target_dir = '/data/moncha-museum/viton/dataset/VITON_traindata/VITON_traindata/train_png2monojpg'

target_dir = '/data/moncha-museum/viton/dataset/result'


files = random.sample(os.listdir(target_product), k=100)
pfafn = PF_AFN()

for product in tqdm(files):
    product_name = product.split('.')[0]

    clothes_path = pjoin(target_product, product)
    edge_path = pjoin(target_png, product_name+'.jpg')

    if not osp.isdir(pjoin(target_dir, product_name)):
        os.makedirs(pjoin(target_dir, product_name))


    for file in files: 
        model_name = file.split('_')[0]+'_0'
        model_path = pjoin(target_models, model_name+'.jpg')

        img = pfafn.gen_image(model_path, clothes_path, edge_path)


        cv2.imwrite(pjoin(target_dir, product_name, model_name+'.jpg'), img)




# tryonutils = TryOnUtils()
# make png dataset
# for file in files:
#     img_name = file.split('.')[0]
#     product_name = img_name.split('_')[0]+'_1'
#     img = cv2.imread(osp.join(target_product, product_name+'.jpg'))
#     cv2.imwrite(pjoin(target_png, product_name+'.png'), img)


#     img = cv2.imread(osp.join(target_png, product_name+'.png'), cv2.IMREAD_UNCHANGED)
#     rgba = cv2.cvtColor(rgb_data, cv2.COLOR_RGB2RGBA)


#     # convert rgb to rgba 
#     # reference https://stackoverflow.com/questions/32290096/python-opencv-add-alpha-channel-to-rgb-image/32290192#32290192
#     # b_channel, g_channel, r_channel = cv2.split(img)
#     # alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
#     # img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
#     new_img = tryonutils.png2monojpg(rgba)

#     cv2.imwrite(pjoin(target_dir, product_name+'.jpg'), new_img)

