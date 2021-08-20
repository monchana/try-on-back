from flask import Flask, request
from namegenerator.src import *

import json
import cv2
import os
osp = os.path

ng = NameGenerator()

HOST = '127.0.0.1'
PORT = 8522

app = Flask(__name__)

@app.route('/',  methods=['POST'])
def createPFAFN():
    content = request.data
    img_path = json.loads(content)

    result = ng.generate(img_path)
    
    saved_json = json.dumps(result)
    print(result)
    return saved_json

if __name__ == "__main__":
    app.run(debug=True, port=PORT)