import cv2
import os
from time import time

from utils import *


def FeatMatch(opts):
    desc_dict = {}

    img_names = sorted(os.listdir(opts['data_dir']))
    img_paths = [os.path.join(opts['data_dir'], x) for x in img_names if \
                 x.split('.')[-1] in opts['ext']]

    data = []
    t1 = time()
    for i, img_path in enumerate(img_paths):
        img = cv2.imread(img_path)
        img_name = img_names[i].split('.')[0]
        img = img[:, :, ::-1]

        feat = cv2.SIFT_create()
        kp, desc = feat.detectAndCompute(img, None)
        data.append((img_name, kp, desc))
        # print(img_name)
        desc_dict[img_name] = [kp, desc]

        t2 = time()
        if (i % opts['print_every']) == 0:
            print('FEATURES DONE: {0}/{1} [time={2:.2f}s]'.format(i + 1, len(img_paths), t2 - t1))
        t1 = time()

    num_done = 0
    num_matches = ((len(img_paths) - 1) * (len(img_paths))) / 2

    match_dict = {}
    t1 = time()
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            img_name1, kp1, desc1 = data[i]
            img_name2, kp2, desc2 = data[j]

            matcher = getattr(cv2, opts['matcher'])(crossCheck=opts['cross_check'])
            matches = matcher.match(desc1, desc2)

            matches = sorted(matches, key=lambda x: x.distance)
            match_dict[img_name1 + '_' + img_name2] = matches
            num_done += 1
            t2 = time()

            if (num_done % opts['print_every']) == 0:
                print(
                    'MATCHES DONE: {0}/{1} [time={2:.2f}s]'.format(num_done, num_matches, t2 - t1))

            t1 = time()

    return desc_dict, match_dict


if __name__ == '__main__':
    curr_dir = os.getcwd()
    data_root = os.path.join(curr_dir, 'data')
    image_root_dirs = os.listdir(data_root)
    image_dir = []
    for img_rt_dir in image_root_dirs:
        pth = os.path.join(data_root, img_rt_dir, 'images')
        image_dir.append(pth)
    for i, dt in enumerate(image_dir):
        # defaults for demo purposes
        opts = {"data_dir": dt, 'ext': ['jpg', 'png'],
                'features': 'SIFT', 'matcher': 'BFMatcher', 'cross_check': True, 'print_every': 1,
                'save_results': False}
        FeatMatch(opts)
