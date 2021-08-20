from flask import Flask, request
from tryongenerator.vtp_bottom.cp_vton_plus.cp_vton_module import VTPModule

import json
import cv2
import os
osp = os.path

cvm = VTPModule()

HOST = '127.0.0.1'
PORT = 8524

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def createPFAFN():
    content = request.data
    data_dict = json.loads(content)
    print(data_dict)
    
    dataroot = data_dict['dataroot']
    cloth_path = data_dict['cloth']
    models_path = data_dict['models']

    cvm.renew_dataset(dataroot, models_path, cloth_path)
    
    cvm.call_gmm()
    dir_names = cvm.call_tom()

    saved_json = json.dumps(dir_names)
    print(dir_names)
    return saved_json

if __name__ == "__main__":
    app.run(debug=True, port=PORT)