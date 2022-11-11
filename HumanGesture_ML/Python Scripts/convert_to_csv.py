import json
import numpy as np
import pandas as pd
import os

path_to_videos = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/uploads/GESTURE_PRACTICE_PREDICT_1656548462041_Gautham/"


def convert_to_csv(path_to_video):
    columns = ['score','nose_score', 'Nose_X', 'Nose_Y', 'leftEye_score', 'leftEye_x', 'leftEye_y',
               'rightEye_score', 'rightEye_x', 'rightEye_y', 'leftEar_score', 'leftEar_x', 'leftEar_y',
               'rightEar_score', 'rightEar_x', 'rightEar_y', 'leftShoulder_score', 'leftShoulder_x', 'leftShoulder_y',
               'rightShoulder_score', 'rightShoulder_x', 'rightShoulder_y', 'leftElbow_score', 'leftElbow_x',
               'leftElbow_y', 'rightElbow_score', 'rightElbow_x', 'rightElbow_y', 'leftWrist_score', 'leftWrist_x',
               'leftWrist_y', 'RightWrist_score', 'RightWrist_X', 'RightWrist_Y', 'LeftHip_score', 'LeftHip_X',
               'LeftHip_Y', 'rightHip_score', 'rightHip_x', 'rightHip_y', 'leftKnee_score', 'leftKnee_x', 'leftKnee_y',
               'rightKnee_score', 'rightKnee_x', 'rightKnee_y', 'leftAnkle_score', 'leftAnkle_x', 'leftAnkle_y',
               'rightAnkle_score', 'rightAnkle_x', 'rightAnkle_y']
    data = json.loads(open(path_to_video + 'key_points.json', 'r').read())
    csv_data = np.zeros((len(data), len(columns)))
    for i in range(csv_data.shape[0]):
        one = []
        one.append(data[i]['score'])
        for obj in data[i]['keypoints']:
            one.append(obj['score'])
            one.append(obj['position']['x'])
            one.append(obj['position']['y'])
        csv_data[i] = np.array(one)
    pd.DataFrame(csv_data, columns=columns).to_csv(path_to_video + 'key_points.csv', index_label='Frames#')


if __name__ == '__main__':

    files = os.listdir(path_to_videos)
    megapath = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/uploads/GESTURE_PRACTICE_PREDICT_1656548462041_Gautham/"
    convert_to_csv(megapath)
    # for file in files:
    #     if not os.path.isdir(path_to_videos + file + "/"):
    #         new_path = path_to_videos + os.path.splitext(file)[0] + "/"
    #         print("---> ", new_path)
    #         convert_to_csv(new_path)
