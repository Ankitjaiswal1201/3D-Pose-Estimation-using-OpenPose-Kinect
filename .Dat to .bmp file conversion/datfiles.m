% Here we are converting color image and depth images in the form of .dat files from Kinect to .bmp files and saving it in a folder.



% clear variables;
% close all;
% clc;
% imtool close all;  % Close all figure windows created by imtool.
% workspace;
% 
% %% Read Data
% 
% 
% Dat_color ='D:\Ankit_Jaiswal\Data\Open_pose_data\Alex\RG2_color\';
% Dat_depth ='D:\Ankit_Jaiswal\Data\Open_pose_data\Alex\RG2_Depth\';

function datfiles(color_img,depth_img)

filePattern = fullfile(color_img, '*.dat'); % This gives file name of color image
file = dir(filePattern); % This gives the directory of the color image file 

filePattern2 = fullfile(depth_img, '*.dat'); % This gives file name of depth image
file2 = dir(filePattern2); % This gives the directory of the depth image file 


for k = 1:length(file)

        colourDatBase = file(k).name; % file name of particular color image
        colourDat = fullfile(color_img, colourDatBase);
        
        currentImage=ReadRawData(colourDat); % ReadRawdata is function to read raw dat files
        baseFileName = sprintf('%s.bmp', colourDatBase );
        fullFileName = fullfile(color_img, baseFileName);
        imwrite(currentImage,fullFileName); % Write back the image in .bmp file
        
       
end


for m = 1:length(file2)

        depthDatBase = file2(m).name;
        depthDat = fullfile(depth_img, depthDatBase);
        
        currentImage2=ReadRawData(depthDat);
        currentImage3 = ind2gray(im2uint8(mat2gray(currentImage2)),parula(256));
        baseFileName2 = sprintf('%s.bmp', depthDatBase );
        fullFileName2 = fullfile(depth_img, baseFileName2);
        imwrite(currentImage3,fullFileName2);
        

end
