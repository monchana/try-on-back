import cv2
import os
import json
from .pose import get_keypoints
from .pad_resize import pad
from os.path import join as pjoin
from math import ceil
import requests
import numpy as np
from .html import line, grid, zigzag

osp=os.path
# save all temp images
class TryOnUtils():

    def __init__(self, root_dir=None):
        self.root = ''
    
    def pad_overall(self, img_paths, dest_dir):
        """
            input : img_dir dir of saved images
        """
        # save to preprocess?
        # img = cv2.imread(osp.join(img_dir,img_name))
        for img_name in img_paths:
            img = cv2.imread(img_name)
            img = pad(img)
            img = cv2.resize(img, (192,256))
            base_img_name = osp.base(img_name)
            cv2.imwrite(osp.join(dest_dir, base_img_name))

    def png2monojpg(self, img):
        h, w, c = img.shape

        if c < 4:
            return None  #FAIL, 알파채널 없음

        _, _, _, mask = cv2.split(img)
        new_img = np.zeros((h, w, 1), np.uint8) #새 이미지는 원채널
        new_img[mask > 125] = 255

        return new_img
    
    # product image
    def detect_bg(self, img_path, no_bg_dir, mask_dir):
        '''
            input: img_dir: path to img
            output: img binary file
        '''
        no_bg_save_dir = no_bg_dir

        img_name = img_path.split('/')[-1].split('.')[0]

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(img_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'LRCm7A4eEBsHHrYUz9cqSL9D'},
        )
        if response.status_code == requests.codes.ok:
            with open(pjoin(no_bg_save_dir, img_name+'.png'), 'wb') as out:
                out.write(response.content)

        else:
            print("Error:", response.status_code, response.text)
            return None

        img = cv2.imread(pjoin(no_bg_save_dir, img_name+'.png'), cv2.IMREAD_UNCHANGED)
        new_img = png2monojpg(img)

        cv2.imwrite(pjoin(mask_dir, img_name+'.jpg'), new_img)
    
    
    def make_html(img_urls):
        '''
            input: img_urls: list of paths to imgs
            output: html dict
        '''
    
        htmls = {}
        htmls['single_line']= line(img_urls)
        htmls['grid'] = grid(img_urls)
        htmls['zigzag'] = zigzag(img_urls)

        return htmls
        
