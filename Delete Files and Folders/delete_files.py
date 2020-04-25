% The following code is used to delete various type of different files from different folder generated during 
% 3D Pose estimation.

import os
import shutil

# Path of Dat files
path2 = "F:/Daten1/"
print(path2)
print(len([name for name in os.listdir(path2)])) # if os.path.isfile(os.path.join(path2, name))]))

i = 1
for i in range(len([name for name in os.listdir(path2)])):

    Color_img ='F:/Daten1/Proband{0}\GAITWCOG\CB7_color'.format(i+23)
    try:
        os.makedirs(Color_img)
    except FileExistsError:
        # directory already exists
        pass
    pathh1 = os.listdir(Color_img)

    depth_img ='F:/Daten1/Proband{0}\GAITWCOG\CB7_Depth'.format(i+23)
    try:
        os.makedirs(depth_img)
    except FileExistsError:
        # directory already exists
        pass
    pathh2 = os.listdir(depth_img)

    json = 'F:/Daten1/Proband{0}\GAITWCOG\CB7_color\json'.format(i+23)
    try:
        os.makedirs(json)
    except FileExistsError:
        # directory already exists
        pass
    pathh3 = os.listdir(json)

    Openpose = 'F:/Daten1/Proband{0}\GAITWCOG/CB7_color/2dOutput/*.png'.format(i+23)

    twoDOutput = 'F:/Daten1/Proband{0}\GAITWCOG/CB7_color/2dOutput/'.format(i+23)
    try:
        os.makedirs(twoDOutput)
    except FileExistsError:
        # directory already exists
        pass
    pathh4 = os.listdir(twoDOutput)

    selected_color ='F:/Daten1/Proband{0}\GAITWCOG\CB7_color\selected'.format(i+23)
    try:
        os.makedirs(selected_color)
    except FileExistsError:
        # directory already exists
        pass
    pathh5 = os.listdir(selected_color)

    selected_depth ='F:/Daten1/Proband{0}\GAITWCOG\CB7_Depth\selected'.format(i+23)
    try:
        os.makedirs(selected_depth)
    except FileExistsError:
        # directory already exists
        pass
    pathh6 = os.listdir(selected_depth)

    mat = 'F:/Daten1/Proband{0}\GAITWCOG\CB7_color\mat'.format(i+23)
    try:
        os.makedirs(mat)
    except FileExistsError:
        # directory already exists
        pass
    pathh7 = os.listdir(mat)

    results = 'F:/Daten1/Proband{0}\GAITWCOG\CB7_results'.format(i+23)
    try:
        os.makedirs(results)
    except FileExistsError:
        # directory already exists
        pass
    pathh8 = os.listdir(results)

    Openpose2D = 'F:/Daten1/Proband{0}\GAITWCOG/CB7_color/2dOutput'.format(i+23)
    if not os.path.exists('Openpose2D'):
        os.makedirs('Openpose2D')
    pathh9 = os.listdir(Openpose2D)



    for item in pathh1:
        if item.endswith(".bmp"):
            os.remove(os.path.join(Color_img, item))

    for item in pathh2:
        if item.endswith(".bmp"):
            os.remove(os.path.join(depth_img, item))

    for item in pathh3:
        if item.endswith(".json"):
            os.remove(os.path.join(json, item))

    for item in pathh4:
        if item.endswith(".png"):
            os.remove(os.path.join(twoDOutput, item))

    for item in pathh5:
        if item.endswith(".png"):
            os.remove(os.path.join(selected_color, item))

    for item in pathh6:
        if item.endswith(".png"):
            os.remove(os.path.join(selected_depth, item))

    for item in pathh7:
        if item.endswith(".mat"):
            os.remove(os.path.join(mat, item))


    shutil.rmtree(selected_color)
    #shutil.rmtree('/path/to/folder')

    skeleton = 'F:/Daten1/Proband{0}\GAITWCOG\CB7_results\skeleton'.format(i+23)
    try:
        os.makedirs(skeleton)
    except FileExistsError:
        # directory already exists
        pass
    pathh10 = os.listdir(skeleton)

    for item in pathh10:
        if item.endswith(".bmp"):
            os.remove(os.path.join(skeleton, item))
