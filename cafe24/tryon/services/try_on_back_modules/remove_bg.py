import json
import os
import requests
from namegenerator.src import *
# from NameGenerator import *

def detect_bg(img_cloth):
    '''
        input: img_cloth: path to img
        output: img binary file
    '''
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(f'/home/hsna/workspaces/try-on/try_on_back_modules/{img_cloth}', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'LRCm7A4eEBsHHrYUz9cqSL9D'},
    )
    if response.status_code == requests.codes.ok:
        return respose.content

        # with open('no-bg.jpg', 'wb') as out:
        #     out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
        return None


def make_html(img_urls):
    '''
        input: img_urls: list of paths to imgs
        output: html dict
    '''
    
    htmls = {}
    htmls['line']= """"""
    
    return


    
    