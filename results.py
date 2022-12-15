import sys
import os
from open3d import io, visualization

"""
This script uses open3d to visualize a point cloud.
It accepts feature method that created the result "SIFT|CNN", the dataset directory 
(one of the top level directories inside the data folder)

expects the point cloud files to be in [project-root]/results/[CNN|SIFT]/[Dataset]
"""
def main(feat_method, dataset):
    curr_dir = os.getcwd()
    res_root = os.path.join(curr_dir, 'results')

    pth = os.path.join(res_root, feat_method, dataset, 'point-clouds')

    point_f_names = sorted(os.listdir(pth))

    point_f_paths = [os.path.join(pth, x) for x in point_f_names if \
                     x.split('.')[-1] in ['ply']]
    point_f_paths = point_f_paths[-1]
    cloud = io.read_point_cloud(point_f_paths)
    visualization.draw_geometries([cloud])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("The script expects a single argument specifying the dataset of the point "
                        "cloud to visualize.\nIt expects the ply files to be in results\\[arg1]\\["
                        "arg2]\\point-clouds folder")
    main(sys.argv[1], sys.argv[2])
