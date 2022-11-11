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


def cosine_similarity(x, y):

    # Ensure length of x and y are the same
    if len(x) != len(y) :
        return None

    # Compute the dot product between x and y
    dot_product = np.dot(x, y)

    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x**2))
    magnitude_y = np.sqrt(np.sum(y**2))

    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)

    return cosine_similarity

def calculate_similarity_cosine(path1,path2):
    #Sample 1
    CSV_T = path1+"data.csv"
    data = pd.read_csv (CSV_T)

    RW_X = data['RightWrist_X']
    RW_Y = data['RightWrist_Y']

    # Normalizing the raw data
    NX = data['Nose_X']
    NY = data['Nose_Y']


    RSHX = data['RightShoulder_X']
    LSHX = data['LeftShoulder_X']

    HIPY = data['LeftHip_X']


    RWXN = (RW_X - NX) / (abs(LSHX - RSHX))
    RWYN = (RW_Y - NY) / (abs(NY - HIPY))



    #Sample 2
    CSV_T_1 = path2+"data.csv"
    data1 = pd.read_csv (CSV_T_1)

    RW_X1 = data1['RightWrist_X']
    RW_Y1 = data1['RightWrist_Y']


    # Normalizing the raw data
    NX1 = data1['Nose_X']
    NY1 = data1['Nose_Y']

    RSHX1 = data1['RightShoulder_X']
    LSHX1 = data1['LeftShoulder_X']

    HIPY1 = data1['LeftHip_X']


    RWXN1 = (RW_X1 - NX1) / (abs(LSHX1 - RSHX1))
    RWYN1 = (RW_Y1 - NY1) / (abs(NY1 - HIPY1))


    # Trajectory

    TA = (RWXN[:]**2 + RWYN[:]**2)

    TA1 = RWXN1[:]**2 + RWYN1[:]**2


    if len(TA) > len(TA1):

        center = abs(len(TA)-len(TA1))

        TA = (RWXN[:int(len(TA)-center)]**2 + RWYN[:int(len(TA)-center)]**2)
        TA1 = RWXN1[:]**2 + RWYN1[:]**2
    elif len(TA) < len(TA1):
        center = abs(len(TA)-len(TA1))

        #print(newcenter , backcenter)
        TA = ((RWXN[:]**2 + RWYN[:]**2))
        TA1 = RWXN1[:len(TA1)-int(center)]**2 + RWYN1[:len(TA1)-int(center)]**2

    elif len(TA)==len(TA1):
        TA = (RWXN[:]**2 + RWYN[:]**2)
        TA1 = RWXN1[:]**2 + RWYN1[:]**2

    cos_sim = cosine_similarity(TA, TA1)
    #print(cos_sim)
    return cos_sim

#
#



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
    cs = df.sort_values('CosineSimilarity',ascending=False)
    cs = cs.head(10)
    for category in cs['Category']:
        if category in freqpred:
            freqpred[category] = freqpred.get(category,0)+1
        else:
            freqpred[category] = 1
    #print(freqpred)
    return (max(freqpred, key=freqpred.get))



def dataset_search(dataset_path):
    latest_folder = os.listdir(dataset_path)
    Data = ""
    Data = "TechnicalType,CosineSimilarity,Category\n"
    #Data = "TechnicalType,CosineSimilarity,Category\n"
    counts=0
    for folder in latest_folder:
        if ".mp4" not in folder and counts < 10:
            latest_folder = os.listdir(dataset_path+folder+"/")
            extractcat = dataset_path+folder+"/"
            category = original_type_extract(extractcat)
            cosine_metric = str(calculate_similarity_cosine(extractcat,pathA))

            #print(category+","+cosine_metric+","+dtwmetric)
            #Data = Data + category+","+cosine_metric+","+categorypredict[category.lower()]+"\n"
            Data = Data + category+","+cosine_metric+","+categorypredict[category.lower()]+"\n"
    print(pathA)
    with open(final_database_path+'Database.csv', 'w') as f:
        f.write(Data)
    result = analyse(final_database_path+'Database.csv')
    with open(pathA+'success.txt','w') as f:
        f.write("True - "+ result)
    print("\n")

    print("Gesture -"+ result)

    return ""


dataset_search(dataset_path)
