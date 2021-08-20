import os
import cv2
import numpy as np

def contour(img):
    return cv2.Canny(img, 60, 120)

def calc_box(img):
    bnd = np.argwhere(img != 0.)
    (ymin, xmin), (ymax, xmax) = bnd.min(0), bnd.max(0)
    return (xmin, ymin, xmax - xmin, ymax - ymin)

def grabcut(img):
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    canny = contour(img)
    rect = calc_box(canny)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    ret = np.where((mask == 2) | (mask == 0), 0, 255).astype('uint8')
    return ret

def make_jpg(mask):
    return cv2.merge((mask, mask, mask))


# mask cloths
def mask_overall(img_dir):
    """
        input : dir to cloth
        output : masked cloth
    """
    img = cv2.imread(img_dir)
    mask = grabcut(img)
    mask_jpg = make_jpg(mask)
    return mask_jpg
