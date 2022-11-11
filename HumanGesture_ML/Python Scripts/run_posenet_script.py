from subprocess import call
import os
# Note that you have to specify path to script
count=0
path = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/uploads/"
dir_list = os.listdir(path)
for i in dir_list:
    if ".mp4" not in i and count < 135:
        newpath = path+i+"/"
        dir_list = os.listdir(newpath)
        if "data.csv" in dir_list:
            pass
        else:
            #print("---",i,"--",count)
            call(["node", "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/posenet_nodejs_setup-master/posenet_nodejs_setup-master/posenet_keypoints.js",i])
        count+=1
#call(["node", "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/posenet_nodejs_setup-master/posenet_nodejs_setup-master/posenet_keypoints.js","GESTURE_PRACTICE_acpower_1654375422648_Gautham"])
