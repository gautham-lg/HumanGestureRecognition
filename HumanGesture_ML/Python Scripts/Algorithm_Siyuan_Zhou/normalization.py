# CSE535 Assignment 2
# Siyuan Zhou

import os
import csv
from os import listdir
from os.path import isdir, join

import numpy as np

# 135 practice videos
path_to_videos = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/"

for directory in [d for d in listdir(path_to_videos) if isdir(join(path_to_videos, d))]:
    leftWrist_x = 0
    leftWrist_y = 0
    rightWrist_x = 0
    rightWrist_y = 0

    leftWrist_xnorm = []
    leftWrist_ynorm = []
    rightWrist_xnorm = []
    rightWrist_ynorm = []

    nose_x = 0
    nose_y = 0

    leftShoulder_x = 0
    rightShoulder_x = 0

    rightHip_y = 0
    leftHip_y = 0

    with open(path_to_videos + directory + "/data.csv") as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        line = 0

        for column in data:
            if not line:
                line = line + 1
                continue
            line = line + 1

            nose_x = float(column[3])
            nose_y = float(column[4])

            leftShoulder_x = float(column[18])
            rightShoulder_x = float(column[21])

            leftWrist_x = float(column[30])
            leftWrist_y = float(column[31])
            rightWrist_x = float(column[33])
            rightWrist_y = float(column[34])

            leftHip_y = float(column[37])
            rightHip_y = float(column[40])

            leftWrist_xnorm.append((leftWrist_x - nose_x) / abs(leftShoulder_x - rightShoulder_x))
            leftWrist_ynorm.append((leftWrist_y - nose_y) / abs(nose_y - (rightHip_y + leftHip_y) / 2))
            rightWrist_xnorm.append((rightWrist_x - nose_x) / abs(leftShoulder_x - rightShoulder_x))
            rightWrist_ynorm.append((rightWrist_x - nose_y) / abs(nose_y - (rightHip_y + leftHip_y) / 2))

    leftWrist_xnorm = np.asarray(leftWrist_xnorm)
    leftWrist_ynorm = np.asarray(leftWrist_ynorm)
    rightWrist_xnorm = np.asarray(rightWrist_xnorm)
    rightWrist_ynorm = np.asarray(rightWrist_ynorm)

    np.save(path_to_videos + directory + '/leftWrist_xnorm.npy', leftWrist_xnorm)
    np.save(path_to_videos + directory + '/leftWrist_ynorm.npy', leftWrist_ynorm)
    np.save(path_to_videos + directory + '/rightWrist_xnorm.npy', rightWrist_xnorm)
    np.save(path_to_videos + directory + '/rightWrist_ynorm.npy', rightWrist_ynorm)
