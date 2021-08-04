from os.path import join as pjoin
from random import choice
import os
import ftplib

'''
    images refer to list of names of images
'''
def send_image_ftp(images, shop_url, nickname, pwd):
    ftp = ftplib.FTP()
    ftp.retrlines('LIST')
    file_path = '/data/try-on-image-dir/products/'
    for image in images:
        file = open(pjoin(file_path, choice(os.listdir(file_path))), "rb")
        ftp.storbinary(f'STOR/web/{image}', file)

    ftp.quit()

def make_html(images):
    return (
        "<h1> Single line </ h1>",
        "<h2> Grid </ h2>",
        "<h3> ZigZag </ h3>",
        )