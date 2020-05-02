# Estimation of Gait Parameters using 3D Pose Estimation and prediction based on Gait Parameters if a person has a disease or not.

Here I have given an idea about the work done in my Research Project, Hiwi and Thesis.

## Publication
Research paper published [https://dl.acm.org/doi/10.1145/3375923.3375943](https://dl.acm.org/doi/10.1145/3375923.3375943)

The Proposed architecture for gait parameter estimation is given as follows:

![alt text](https://github.com/Ankitjaiswal1201/Thesis/blob/master/Images/arch.png)


## Project Details
The proposed approach consists of three main blocks. They are 
1. Data acquisition, 
2. 3D pose-estimation and 
3. Gait parameter extraction. 

In data acquisition block, the data is collected using the Microsoft Kinect device and is stored for further processing using XPCV
software []. The stored data is then used to estimate 3D Pose estimation of the person as shown in the 3D pose-estimation block.
Using the 3D pose estimation results, the gait parameters are extracted as shown in the gait parameter extraction block.


### Conversion of Dat raw files to any viewable format like .bmp, .png, .jpg. ###
As the obtained data from XPCV software is raw data, here we are converting color image and depth images in the form of .dat files from kinect to .bmp files and saving it in a folder.

### 3D Pose Estimation ###
The 3D pose estimation is an important aspect ofthe gait parameter estimation. The estimation of 3D pose involves two stages.
The first stage involves 2D pose estimation and the second stage involves mapping of 2D pose estimation results with depth image to generate a 3D point cloud.

2D Pose Estimation
The RGB data acquired from the Kinect is used to estimate the 2D pose. For the estimation of 2D pose, one of the most popular 2D
pose estimation method OpenPose [] is used.
The output of OpenPose looks like as shown in figure below.
![alt text](https://github.com/Ankitjaiswal1201/Thesis/blob/master/Images/pose_face_hands.gif)

OpenPose gives two files. One is Color image with 2D skeleton on it and other JSON file with locations of all key-joints of
detected human skeleton.

### Converting 2D Data from OpenPose (JSON file) to 2D annotations in MATLAB. ###
This folder gives information of how to convert 2D Data (JSON file) obtained from OpenPose to 2D annotations in MATLAB.




