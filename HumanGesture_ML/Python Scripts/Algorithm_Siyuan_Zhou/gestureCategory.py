# CSE535 Assignment 2
# Siyuan Zhou

import csv
from os import listdir
from os.path import isdir, join, splitext
from statistics import mode

import numpy as np
from dtw import *

# 135 practice videos
#path_to_videos = "C:/CSE535/Assignment2/Videos/"
path_to_videos = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/"
# new practice videos
#path_to_new_videos = "C:/CSE535/Assignment2/NewVideos/gateway_PRACTICE_20220630_150031_Zhou"
path_to_new_videos = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/uploads/GESTURE_PRACTICE_PREDICT_1657135777612_Gautham/"

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

k = 8

with open(splitext(path_to_new_videos)[0] + "/data.csv") as csv_file:
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

video_norm = [leftWrist_xnorm, leftWrist_ynorm, rightWrist_xnorm, rightWrist_ynorm]

knearest = []

for directory in [d for d in listdir(path_to_videos) if isdir(join(path_to_videos, d))]:
    newLeftWrist_xnorm = np.load(path_to_videos + directory + "/leftWrist_xnorm.npy")
    newLeftWrist_ynorm = np.load(path_to_videos + directory + "/leftWrist_ynorm.npy")
    newRightWrist_xnorm = np.load(path_to_videos + directory + "/rightWrist_xnorm.npy")
    newRightWrist_ynorm = np.load(path_to_videos + directory + "/rightWrist_ynorm.npy")

    newVideo_norm = [newLeftWrist_xnorm, newLeftWrist_ynorm, newRightWrist_xnorm, newRightWrist_ynorm]

    tuple = (directory, sum([dtw(video_norm[i], newVideo_norm[i]).distance for i in range(len(newVideo_norm))]))
    knearest.append(tuple)
    knearest.sort(key=lambda x: x[1], reverse=True)

    if len(knearest) > k:
        knearest = knearest[1:]

category = []

for tuple in knearest:
    with open(path_to_videos + tuple[0] + "/category.txt") as f:
        category.append(f.readline().rstrip())

# with open(splitext(path_to_new_videos)[0] + "/category_txt", "w") as f:
#     f.write(mode(category))

print("The category of the video " + path_to_new_videos + " is: " + mode(category))
