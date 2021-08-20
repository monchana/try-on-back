import os
from os.path import join as pjoin
import requests
import json
import random

clothes_path = 'dataset/test_clothes/003434_1.jpg'
edge_path = 'dataset/test_edge/003434_1.jpg'
img_path = 'dataset/test_img/000066_0.jpg'

root_dir = '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/PF_AFN/PF_AFN_test'

# send_dict = {'cloth': pjoin(root_dir, clothes_path), 'edge': pjoin(root_dir, edge_path), 
#     'models': [pjoin(root_dir, img_path)], 'dest':root_dir}


# target_product = '/home/hsna/workspaces/try-on/try_on_back_modules/examples/bottom/13210273li_12_f'
# target_model =  '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data/image'
# target_pairs = '/home/hsna/workspaces/try-on/try_on_back_modules/examples/train_pairs.txt'

dataroot = '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data'

target_cloth = '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data/cloth/13210273li_12_f.jpg'
target_model =  '/home/hsna/workspaces/try-on/try_on_back_modules/tryongenerator/vtp_bottom/data/image/GM0019123123228_0_ORGINL_20200110170201548_1265e.jpg'



send_dict = {'cloth': pjoin(target_cloth), 
    'models': [pjoin(target_model)], 'dataroot':dataroot}

json_data = json.dumps(send_dict)

response = requests.post(
            "http://127.0.0.1:8524",
            data=json_data,
        )

data = json.loads(response.content)
print(data)