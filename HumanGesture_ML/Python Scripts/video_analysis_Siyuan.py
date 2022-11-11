import pandas as pd
import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt
from numpy import dot
import math
from numpy.linalg import norm
import os

from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

server_path = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/uploads/"
dataset_path = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/"
final_database_path = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/posenet_nodejs_setup-master/posenet_nodejs_setup-master/"
counts=0
Data = ""

categorypredict = {
"acpower":"Hardware",
"algorithm": "Programming",
"antenna" :"Hardware",
"authentication": "Cryptography",
"authorization" :"Cryptography",
"bandwidth" : "Networking",
"bluetooth" : "Networking",
"browser" : "Networking",
"cloudcomputing" : "Data",
"datacompression" : "Data",
"datalinklayer" : "Data",
"datamining" : "Data",
"decryption" : "Cryptography",
"domain" : "Networking",
"email" : "Networking",
"exposure" : "Cryptography",
"filter" : "Programming",
"firewall" : "Cryptography",
"flooding" : "Networking",
"gateway" : "Networking",
"hacker" : "Cryptography",
"header" : "Data",
"hotswap" : "Hardware",
"hyperlink" : "Networking",
"infrastructure" : "Hardware",
"integrity" : "Cryptography",
"internet" : "Netoworking",
"intranet" : "Netoworking",
"latency" : "Data",
"loopback" : "Networking",
"motherboard" : "Hardware",
"network" : "Networking",
"networking" : "Netoworking",
"networklayer" : "Netoworking",
"node" : "Programming",
"packet" : "Data",
"partition" : "Hardware",
"passwordsniffing" : "Cryptography",
"patch" : "Programming",
"phishing" : "Cryptography",
"physicallayer" : "Networking",
"ping" : "Networking",
"portscan" : "Networking",
"presentationlayer" : "Netwroking",
"protocol" : "Networking"
}


def CalculateDTW(path1, path2):
    #Sample 1
    CSV_A = path1+"data.csv"
    data = pd.read_csv (CSV_A)
    #df = pd.DataFrame(data, columns= ['RightWrist_X'])

    #data[['RightWrist_X','RightWrist_Y']].plot()
    RW_X = data['RightWrist_X']
    RW_Y = data['RightWrist_Y']


    # Normalizing the raw data
    NX = data['Nose_X']
    NY = data['Nose_Y']

    RSHX = data['RightShoulder_X']
    LSHX = data['LeftShoulder_X']


    HIPY = data['LeftHip_X']
    # HIPY = data['leftHip_x']


    RWXN = (RW_X - NX) / (abs(LSHX - RSHX))
    RWYN = (RW_Y - NY) / (abs(NY - HIPY))

    # plt.plot(RWXN[10:],RWYN[10:])
    # plt.show()

    #Sample 2
    CSV_A_1 = path2+"data.csv"
    data1 = pd.read_csv (CSV_A_1)
    #df = pd.DataFrame(data, columns= ['RightWrist_X'])

    #data[['RightWrist_X','RightWrist_Y']].plot()
    RW_X1 = data1['RightWrist_X']
    RW_Y1 = data1['RightWrist_Y']
    # RW_X1 = data1['rightWrist_x']
    # RW_Y1 = data1['rightWrist_y']

    # plt.plot(RW_X,RW_Y)

    # Normalizing the raw data
    NX1 = data1['Nose_X']
    NY1 = data1['Nose_Y']
    # NX1 = data1['nose_x']
    # NY1 = data1['nose_y']

    RSHX1 = data1['RightShoulder_X']
    LSHX1 = data1['LeftShoulder_X']
    # RSHX1 = data1['rightShoulder_x']
    # LSHX1 = data1['leftShoulder_x']

    HIPY1 = data1['LeftHip_X']
    # HIPY1 = data1['leftHip_x']


    RWXN1 = (RW_X1 - NX1) / (abs(LSHX1 - RSHX1))
    RWYN1 = (RW_Y1 - NY1) / (abs(NY1 - HIPY1))


    # Trajectory

    TA = (RWXN[:]**2 + RWYN[:]**2)
    mainTA = TA
    TA1 = (RWXN1[:]**2 + RWYN1[:]**2)
    mainTA1 = TA1
    return DTWDistance(TA,TA1)


def DTWDistance(s1, s2):
    DTW={}

    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])

    return math.sqrt(DTW[len(s1)-1, len(s2)-1])


def find_latest(server_path):
    latest_folder = os.listdir(server_path)
    for folder in latest_folder:
        if ".mp4" not in folder:
            latest_folder = os.listdir(server_path+folder+"/")
            if "success.txt" not in latest_folder:
                return server_path+folder+"/"



pathA = find_latest(server_path)



def original_type_extract(path):
    toreplace = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/GESTURE_PRACTICE_"
    newitem = path.replace(toreplace,"")
    replacevalue = newitem.find("_")
    #print(newitem[:replacevalue])
    return newitem[:replacevalue]


def DatabaseSET(value):
    Data = Data + value+"\n"
    return Data

def analyse(path_database):
    freqpred = {}
    df=pd.read_csv(path_database)
    dtw = df.sort_values('DTWScore',ascending=True)
    dtw = dtw.head(10)
    for category in dtw['Category']:
        if category in freqpred:
            freqpred[category] = freqpred.get(category,0)+1
        else:
            freqpred[category] = 1
    #print(freqpred)
    return (max(freqpred, key=freqpred.get))



def dataset_search(dataset_path):
    latest_folder = os.listdir(dataset_path)
    Data = ""
    Data = "TechnicalType,DTWScore,Category\n"
    counts=0
    for folder in latest_folder:
        if ".mp4" not in folder and counts < 10:
            latest_folder = os.listdir(dataset_path+folder+"/")
            extractcat = dataset_path+folder+"/"
            category = original_type_extract(extractcat)

            dtwmetric = str(CalculateDTW(extractcat,pathA))

            Data = Data + category+","+dtwmetric+","+categorypredict[category.lower()]+"\n"
    print(pathA)
    with open(final_database_path+'Database.csv', 'w') as f:
        f.write(Data)
    result = analyse(final_database_path+'Database.csv')
    with open(pathA+'success.txt','w') as f:
        f.write("True - "+ result)
    print("\n")

    print("Answer is "+ result)

    print("\n")
    return ""



dataset_search(dataset_path)
