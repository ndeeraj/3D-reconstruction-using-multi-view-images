import cv2
import os
from time import time
from skimage.feature import match_descriptors
from utils import *


def FeatMatch(opts):
    desc_dict = {}

    img_names = sorted([x for x in os.listdir(opts['data_dir']) if \
                        x.split('.')[-1] in opts['ext']])
    img_paths = [os.path.join(opts['data_dir'], x) for x in img_names if \
                 x.split('.')[-1] in opts['ext']]

    data = []
    t1 = time()
    for i, img_path in enumerate(img_paths):
        feat_path = img_path

        features = np.load(feat_path)
        keypoints = features["keypoints"][:,[0,1]]
        kp = []
        # need to convert keypoints from d2-net to cv2 keypoints
        for d1 in range(keypoints.shape[0]):
            knt = cv2.KeyPoint(keypoints[d1,0],keypoints[d1,1],size= 16)
            kp.append(knt)

        desc = features["descriptors"]
        img_name = img_names[i].split('.')[0]

        data.append((img_name, kp, desc))
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

            matches_tmp = match_descriptors(desc1, desc2, cross_check=True)
            matches = []
            # need to created cv2 match objects for matches from d2-net
            for match in matches_tmp:
                # sum of squared distance is computed as rge distance measure since
                # cv2 match object need them.
                comp_dist = desc1[match[0], :].copy()
                comp_dist = comp_dist - desc2[match[1], :]
                comp_dist = np.square(comp_dist)
                comp_dist = np.sum(comp_dist)
                distance = np.sqrt(comp_dist)
                match_obj = cv2.DMatch(match[0], match[1], distance)
                matches.append(match_obj)

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
        # defaults for demo
        opts = {"data_dir": dt, 'ext': ['d2-net'],
                'features': 'CNN', 'matcher': 'BFMatcher', 'cross_check': True, 'print_every': 1,
                'save_results': False}
        FeatMatch(opts)

