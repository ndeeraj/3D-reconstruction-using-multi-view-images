# 3D reconstruction using multi-view images

In this project we implement a traditional SfM pipeline using https://github.com/muneebaadil/how-to-sfm as a reference. 
we also extend the pipeline to use features extracted from D2-Net https://github.com/mihaidusmanu/d2-net

Setup for SfM pipeline
---------------

- OpenCV python
- Numpy
- MeshLab / open3D - optional, only if you want to visualize the point cloud

Setup for D2-Net
----------

- We have changed the files in D2-Net according to our use case and solved the deprecation errors, so no additional setup for D2-Net is required.
- For our pipeline to work we need d2-net files which contain the features extracted for each image to be in the data directory, for instance, `[project root]/data/fountain-P11/images/`
- If you do not find them, for each image you can generate the file by 

Data setup
----------
We used data from https://github.com/openMVG/SfM_quality_evaluation.
The script expects the data to be in [project root]/data/[fountain-P11], [project root]/data/[castle-P19] etc. 
Make sure that there are no other sub folders in the data directory.

In this repository, we have just submitted fountain-P11 dataset for demo purposes. the sfm script

Running SfM using SIFT features
-------------------------------

- run `python sfm.py -h` for help on the options.
- To run the demo on "fountain-P11", execute `python sfm.py --demo --features SIFT`
- To run for the entire dataset, execute `python sfm.py --no-demo --features SIFT`
- The point cloud `.ply` file will be generated in [project-root]/results/SIFT/[dataset name]/point-clouds

Visualizing point clouds
------------------------

- If you installed open3D, you can use the results script as  `python results.py [SIFT|CNN] [dataset name]` like `python results.py SIFT fountain-P11`. The script expects the `.ply` files to be in [project-root]/results/SIFT/fountain-P11
- You can also load up the highest numbered `.ply` file in MeshLab to visualize.
- In either method, you would need to zoom and rotate the points to see the reconstructions clearly.
- The results we obtained for few dataset are in `results\cloud_point_visualization`


