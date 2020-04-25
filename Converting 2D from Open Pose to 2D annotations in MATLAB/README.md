# Convert 2D Data from OpenPose (JSON file) to 2D annotations in MATLAB #

This file gives you information about how to convert 2D Data obtained from OpenPose in the form of JSON file to 2D annotations in MATLAB.
Here we have considered body25 model.
You can use this code as a function or you can run it on individual JSON files.

Here the idea is
1. Load the json file using loadjson function. As the obtained value from it is a structure, we will select 
people from it using S.People. Then convert the cell array obtained for different  people into an ordinary array.
2. Then for each person detected ,we take the values of x,y,c for each joint and store it in the form of matrix.
3. Once we have stored data of one person, we take x and y value from it and store this value in another variable in first and second column
and we increase the initial column value by 2 so that next person data can be stored in next two columns.
