def skeleton_fun(mat,skeleton):

    import cv2
    #import glob
    import numpy as np
    import scipy.io
    import os
    
    path = mat #G:\\SENDA\\Proband_172\\GAIT\\RG1_color\\mat\\'
    file_lists = os.listdir(path)  
    
    path4 =skeleton # 'G:\\SENDA\\Proband_172\\GAIT\\RG1_results\\skeleton\\'
    #file_lists4 = os.listdir(path4) 
   
    for files in sorted(file_lists):
        if files.endswith(".mat"):              
                mat2 = scipy.io.loadmat(os.path.join(path,files))
                centers2 = mat2['b2']
                centers =np.array(centers2).tolist()
                if centers[8] == [0,0] or centers[10] == [0,0] or centers[11] == [0,0] or centers[13] == [0,0] or centers[14] == [0,0] :
                    continue
                else:  
                    BodyPairs = [
        			(1,2), (1,5), (2,3), (3,4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (10, 11), (11, 24), (11, 22), (22, 23), 
        			(8, 12), (12, 13), (13, 14), (14, 21), (14, 19), (19, 20),(0, 15), (15, 17), (0, 16), (16, 18), (0, 1) 
        				]
                    npimg=np.zeros((1080,1920,3))
                    for pair in BodyPairs:
                        ab = tuple((centers[pair[0]]))
    #                   
                        ac = tuple((centers[pair[1]]))
                        if (ab == (0,0)) or (ac == (0,0)):
                               print(centers[pair[0]])
                        else: 
                                npimg = cv2.line(npimg, tuple((centers[pair[0]])), tuple((centers[pair[1]])),(0,255,0), 2)
                
                #ab = os.path.splitext(os.path.basename(filenames))
                abc= files.split('.dat',2)[0]
                #cv2.imwrite(tuple(os.path.splitext(os.path.basename(filenames))) + '.png',npimg)

                cv2.imwrite(os.path.join(path4 , abc + '.bmp'),npimg)
