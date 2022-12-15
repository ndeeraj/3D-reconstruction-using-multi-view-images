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

[should be nothing right?]

Data setup
----------
We used data from https://github.com/openMVG/SfM_quality_evaluation.
The script expects the data to be in [project root]/data/[fountain-P11], [project root]/data/[castle-P19] etc. 
Make sure that there are no other sub folders in the data directory.

In this repository, we have just submitted fountain-P11 dataset for demo purposes. the sfm script


