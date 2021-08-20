from shutil import copyfile
import os
from os.path import join as pjoin


target_dir = '/home/hsna/workspaces/try-on/try_on_back_modules/examples/bottom'


target_product = '/data/moncha-museum/viton/dataset/pants_training_data/clothes'
target_models = '/data/moncha-museum/viton/dataset/pants_training_data/people'

dest = '/data/moncha-museum/viton/dataset/pants_result'

products = os.listdir(target_dir)
models = os.listdir(os.path.join(target_dir, products[0]))

for file in products:
    file = file+'.jpg'
    copyfile(pjoin(target_product, file), pjoin(dest, 'products', file))


for file in models:
    copyfile(pjoin(target_models, file), pjoin(dest, 'models', file))

