import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Main_Array = []

disptype = {
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



def test_set(path):
    Test_CSV = path
    data = pd.read_csv(Test_CSV+"data.csv")

    RW_X = data['RightWrist_X']
    RW_Y = data['RightWrist_Y']


    # Normalizing the raw data
    NX = data['Nose_X']
    NY = data['Nose_Y']

    RSHX = data['RightShoulder_X']
    LSHX = data['LeftShoulder_X']

    HIPY = data['LeftHip_Y']


    RWXN = (RW_X - NX) / (abs(LSHX - RSHX))
    #RWXN = np.divide(RW_X - NX,abs(LSHX - RSHX))
    RWYN = (RW_Y - NY) / (abs(NY - HIPY))

    TA = (RWXN[1:]**2 + RWYN[1:]**2)
    _finder = path[136:]
    removal = (_finder[_finder.find("_"):])
    category = (_finder.replace(removal,""))
    newcat = disptype.get(category.strip())


    return [TA,newcat]


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


#Test set 1

TA = test_set("C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/GESTURE_PRACTICE_email_1654378950418_Gautham/")
TA1 = TA[0]
TA1_Category = TA[1]

#Sample 1
TA = test_set("C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/GESTURE_PRACTICE_email_1654378950418_Gautham/")
TA2 = TA[0]

TA = test_set("C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/GESTURE_PRACTICE_email_1654378950418_Gautham/")
TA3 = TA[0]


Main_Array.append([cosine_similarity(TA1,TA2),TA1_Category])


print(Main_Array)
