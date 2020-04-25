import math
import sys
from PIL import Image
import numpy as np
import scipy.io as sio
import os
import time
import re
import cupy as cp
import multiprocessing as mp
from openpyxl import load_workbook
import pandas as pd

% Kinect Camera Calibration Parameters
scalingFactor = 5000.0
fx_d = 365.3768
fy_d = 365.3768
cx_d = 253.6238
cy_d = 211.5918
fx_rgb = 1054.8082
fy_rgb = 1054.8082
cx_rgb = 965.6725
cy_rgb = 552.0879

RR = np.array([
    [0.99991, -0.013167, -0.0020807],
    [0.013164, 0.99991, -0.0011972],
    [-0.0020963, 0.0011697, 1]
])
TT = np.array([0.052428, 0.0006748, 0.000098668])
extrinsics = np.array([[.99991, -0.013167, -0.0020807, 0.052428], [0.013164, 0.99991, -0.0011972, 0.0006748], [-0.0020963, 0.0011697, 1, 0.000098668], [0, 0, 0, 1]])


def init_maxvalue():
    for center in centers3:
        if center == (0, 0):
            continue
        min_xy.append(sys.float_info.max)
        min_vex.append((0, 0))
        p_vex.append((0, 0, 0))


def depth_rgb_registration(rgb, depth):

    init_maxvalue()
    rgb = Image.open(rgb)
    depth = Image.open(depth).convert('L')  # convert image to monochrome
    if rgb.mode != "RGB":
        raise Exception("Color image is not in RGB format")

    for v in range(depth.size[0]):
        for u in range(depth.size[1]):
            try:
                (p, x, y) = depth_to_xyz_and_rgb(v, u, depth)  # this gives p = [pcx, pcy,pcz]
                # aligned(:,:,0) = p
            except:
                continue

            if (x > rgb.size[0] - 1 or y > rgb.size[1] - 1 or x < 1 or y < 1 or np.isnan(x) or np.isnan(y)):
                continue
            x = round(x)
            y = round(y)
            color = rgb.getpixel((x, y))
            # print(color)
            min_distance((x, y), p)

            if color == (0, 0, 0):
                p[0] = 0
                p[1] = 0
                p[2] = 0
                continue
            # if.write("%f .%f %f \n"%(p[0],p[1],p[2]))
            points.append(" %f %f %f %d %d %d 0\n" % (p[0], p[1], p[2], 255, 0, 0))

        i = 0
        x = []
        y = []
        z = []

    for val in min_vex:

        gait_list1.append(val[0])
        gait_list1.append(val[1])
        gait_list1.append(p_vex[i][0])
        gait_list1.append(p_vex[i][1])
        gait_list1.append(p_vex[i][2])


        points.append(" %f %f %f %d %d %d 0\n" % (p_vex[i][0], p_vex[i][1], p_vex[i][2], 0, 255, 0))
        x.append(p_vex[i][0])
        y.append(p_vex[i][1])
        z.append(p_vex[i][2])
        i = i + 1


def min_distance(val, p):
    i = 0
    for center in centers3:
        if center == (0, 0):
            continue
        temp = math.sqrt(math.pow(center[0] - val[0], 2) + math.pow(center[1] - val[1], 2))
        if temp < min_xy[i]:
            min_xy[i] = temp
            min_vex[i] = val
            p_vex[i] = p
        i = i + 1



def depth_to_xyz_and_rgb(uu, vv, dep):
    # t1.tic()
    # get z value in meters
    pcz = dep.getpixel((uu, vv))
    if pcz == 60:
        return

    pcx = (uu - cx_d) * pcz / fx_d
    pcy = ((vv - cy_d) * pcz / fy_d)

    # apply extrinsic calibration
    P3D = np.array([pcx, pcy, pcz])
    P3Dp = np.dot(RR, P3D) - TT

    # rgb indexes that P3D should match
    uup = (P3Dp[0] * fx_rgb / P3Dp[2] + cx_rgb)
    vvp = (P3Dp[1] * fy_rgb / P3Dp[2] + cy_rgb)

    # t1.toc()

    # return a point in point cloud and its corresponding color indices
    return P3D, uup, vvp


def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return res


def display_fun(mat, selected_depth, selected_color, results, excel):
    global min_xy, min_vex, p_vex, p_xyz, image_list, image_list2, points, centers3, gait_list1, data1, gait_list2
    writer = pd.ExcelWriter(excel, engine='openpyxl')
    wb = writer.book
    path = mat
    file_lists = os.listdir(path)

    path3 = selected_depth
    included_extensions = ['png']
    file_lists3 = [fn for fn in os.listdir(path3)
                   if any(fn.endswith(ext) for ext in included_extensions)]

    path4 = selected_color
    file_lists4 = os.listdir(path4)

    path6 = results
    file_lists6 = os.listdir(path6)

    gait_list1 = []
    gait_list2 = []
    data1 = []

    for idx, list1 in enumerate(file_lists4):
        # Iterate through items of list2
        for i in range(len(file_lists3)):
            if list1.split('.')[0] == file_lists3[i].split('.')[0]: 
                rgb = os.path.join(path4, list1)
                depth = os.path.join(path3, sorted(file_lists3)[i])
                m = sorted(file_lists)[idx]
                mat2 = sio.loadmat(os.path.join(path, m))
                abc = list1.split('.')[0]
                gait_list1 = []

                fnum = convert(re.findall("(\d+)", abc))
                gait_list1.append(fnum)
                # f.write(str(fnum) + ' ')
                # fnum = int(str.isdigit, abc)
                centers2 = mat2['b1']
                centers3 = np.array(centers2).tolist()

                min_xy = []
                min_vex = []
                p_vex = []
                p_xyz = []
                image_list = []
                image_list2 = []
                points = []

                depth_rgb_registration(rgb, depth)
                gait_list2.append(gait_list1)
                data1 = pd.DataFrame(gait_list2)
                data1.to_excel(writer, index=False)
                wb.save(excel)
    #f.close
