import os
import cv2
osp = os.path

def get_keypoints(img, net, rerun=False):
    json_string = '{"version": 1.0, "people": [{"face_keypoints": [], "pose_keypoints": ['

    img_h, img_w = img.shape[:2]
    input_blob = cv2.dnn.blobFromImage(img, 1.0 / 255, (368,368), (0, 0, 0), swapRB=False, crop=False)
    net.setInput(input_blob)

    out = net.forward()
    out_h = out.shape[2]
    out_w = out.shape[3]

    for i in range(18):
        prob_map = out[0, i, :, :]
        _, prob, _, point = cv2.minMaxLoc(prob_map)

        x = (img_w*point[0])/out_w + img_w/out_w/2
        y = (img_h*point[1])/out_h + img_h/out_h/2

        if prob > 0.1:
            json_string += str(x)+', '+str(y)+', '+str(prob)+', '
        else:
            json_string += str(0)+', '+str(0)+', '+str(0)+', '

    return json_string[:-2]

if __name__ == '__main__':
    net = cv2.dnn.readNetFromCaffe("openpose/pose_deploy_linevec.prototxt", "openpose/pose_iter_440000.caffemodel")

    img_dir = 'data/test/image/'
    out_dir = 'data/test/pose/'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for img_name in os.listdir(img_dir):
        img = cv2.imread(osp.join(img_dir,img_name))
        json_string = get_keypoints(img, net)
        json_string += '], "hand_right_keypoints": [], "hand_left_keypoints": []}]} '

        with open(out_dir+img_name.split('.')[0]+'_keypoints.json','w') as f:
            f.write(json_string)
