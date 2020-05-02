# Estimation of Gait Parameters using 3D Pose Estimation and prediction based on Gait Parameters if a person has a disease or not.

Here I have given an idea about the work done in my Research Project, Hiwi and Thesis.

The Proposed architecture for gait parameter estimation is given as follows:

![alt text](https://github.com/Ankitjaiswal1201/Thesis/blob/master/Images/arch.png)


The proposed approach consists of three main blocks. They are 
1. Data acquisition, 
2. 3D pose-estimation and 
3. Gait parameter extraction. 

In data acquisition block, the data is collected using the Microsoft Kinect device and is stored for further processing using XPCV
software. The stored data is then used to estimate 3D Pose estimation of the person as shown in the 3D pose-estimation block.
Using the 3D pose estimation results, the gait parameters are extracted as shown in the gait parameter extraction block.


### Conversion of Dat raw files to any viewable format like .bmp, .png, .jpg. ###
Here we are converting color image and depth images in the form of .dat files from Kinect to .bmp files and saving it in a folder.

### 3D Pose Estimation ###
Here the 3D Pose estimation is performed by using RGB Images, Depth Images, mat files obtained from 2D Pose estimation using OpenPose. Only 3D Pose estimation values for 25 keypoints are stored in excel file. The values can also be stored in the form of 3D Point Cloud format (PCD).

### Converting 2D Data from OpenPose (JSON file) to 2D annotations in MATLAB. ###
This folder gives information of how to convert 2D Data obtained from OpenPose to 2D annotations in MATLAB.


