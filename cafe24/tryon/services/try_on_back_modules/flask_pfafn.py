from flask import Flask, request
from tryongenerator.PF_AFN.PF_AFN_test.module import PF_AFN
import json
import cv2
import os
osp = os.path

pfafn = PF_AFN()

HOST = '127.0.0.1'
PORT = 8523

app = Flask(__name__)


@app.route('/', methods=['POST'])
def createPFAFN():
    content = request.data
    data_dict = json.loads(content)
    print(data_dict)
    cloth_path = data_dict['cloth']
    edge_path = data_dict['edge']
    models_path = data_dict['models']

    dest_dir = data_dict['dest']
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    saved_dest = []
    for model in models_path:
        model_name = os.path.basename(model)
        img = pfafn.gen_image(model, cloth_path, edge_path)
        cv2.imwrite(osp.join(dest_dir, model_name), img)
        saved_dest.append(osp.join(dest_dir, model_name))

    saved_json = json.dumps(saved_dest)

    return saved_json


if __name__ == "__main__":
    app.run(debug=True, port=PORT)
