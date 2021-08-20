import os 
# from namegenerator.src import *
import random
# from tryongenerator.PF_AFN.PF_AFN_test.module import PF_AFN
# from tryongenerator.utils.util_module import TryOnUtils
# from tryongenerator.vtp_bottom.bottomUtil import BottomUtil
from tryongenerator.vtp_bottom.cp_vton_plus.cp_vton_module import VTPModule

from tqdm import tqdm
from shutil import copyfile, copytree
from os.path import join as pjoin
import cv2

target_product = '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data/cloth'
target_model =  '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data/image'

target_pairs = '/home/hsna/workspaces/try-on/try_on_back_modules/examples/train_pairs.txt'
pairs = []
with open(target_pairs, 'r') as openfile:
    pairs = openfile.readlines()

pairs = [pair.replace('\n', '') for pair in pairs ]

files = random.sample(pairs, k=100)

products = []
models = []
for file in files:
    model, product = file.split(' ')
    products.append(product)
    models.append(model)

cvm = VTPModule()
dataroot = '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data'
for product in tqdm(products):
    product_name = product.split('.')[0]
    product_path = pjoin(target_product, product)
    
    models_path = [pjoin(target_model, model) for model in models]

    # cvm.make_dataset(models_path, product_path)
    cvm.renew_dataset(dataroot ,models, product)

    cvm.call_gmm()
    cvm.call_tom()

    copytree(pjoin('/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom', 'result'), pjoin('/home/hsna/workspaces/try-on/try_on_back_modules/examples/bottom', product_name))

