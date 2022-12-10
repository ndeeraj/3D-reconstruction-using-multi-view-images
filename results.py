import sys
import os
from open3d import io, visualization


def main(dataset):
    curr_dir = os.getcwd()
    res_root = os.path.join(curr_dir, 'results')

    pth = os.path.join(res_root, dataset, 'point-clouds')

    point_f_names = sorted(os.listdir(pth))
    cld_pts = []
    point_f_paths = [os.path.join(pth, x) for x in point_f_names if \
                     x.split('.')[-1] in ['ply']]

    for pts_file in point_f_paths:
        cloud = io.read_point_cloud(pts_file)
        cld_pts.append(cloud)

    visualization.draw_geometries(cld_pts)  # Visualize the point cloud


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("The script expects a single argument specifying the dataset of the point "
                        "cloud to visualize.\nIt expects the ply files to bt in results\\["
                        "arg]\\point-clouds folder")
    main(sys.argv[1])
