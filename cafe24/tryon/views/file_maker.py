import os
from os.path import join as pjoin
import ftplib


'''
    images refer to list of names of images
'''
def send_image_ftp(images, shop_url, nickname, pwd):
    ftp = ftplib.FTP()
    ftp.retrlines('LIST')
    for image in images:
        file = cv2.imread(image)
        ftp.storbinary(f'STOR/web/{image}', file)

    ftp.quit()

def make_html(images):
    return