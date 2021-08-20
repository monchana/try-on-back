import os
from math import ceil
import cv2
import os.path as osp

def pad(img):
    img_h,img_w = img.shape[:2]
    if img_h*192 != img_w*256:
        if img_h*192 > img_w*256:
            new_img_h = ceil(img_h/4)*4
            new_img_w = new_img_h*3//4

            diff_h = new_img_h-img_h
            diff_w = new_img_w-img_w

            top = diff_h//2
            bottom = diff_h-top
            left = diff_w//2
            right = diff_w-left

            img = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value=[255,255,255])
        else:
            new_img_w = ceil(img_w/3)*3
            new_img_h = new_img_w*4//3

            diff_w = new_img_w-img_w
            diff_h = new_img_h-img_h

            top = diff_h//2
            bottom = diff_h-top
            left = diff_w//2
            right = diff_w-left

            img = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,value=[255,255,255])

    return img


def pad_overall(img_dict):
    """
        input : {'cloth':cloth_dir, 'model':model_dir_list}
        output: {'cloth':resized_cloth, 'model': resized_model_list}
    """
    output_imgs={}
    # img = cv2.imread(osp.join(img_dir,img_name))
    img = cv2.imread(img_dict['cloth'])
    img = pad(img)
    img = cv2.resize(img, (192,256))
    output_imgs['cloth'] = img

    model_imgs = []
    for img_name in img_dict['model']:
        img = cv2.imread(img_name)
        img = pad(img)
        img = cv2.resize(img, (192,256))
        model_imgs.append(img)
    
    output_imgs['model'] = model_imgs

    return output_imgs
