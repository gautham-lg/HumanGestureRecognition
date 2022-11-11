# CSE535 Assignment 2
# Siyuan Zhou

import os
from os import listdir
from os.path import isdir, join

path_to_videos = "C:/Users/glakkava/Documents/ASU/CS535/AssignmentGestureDetection/HumanGesture/HumanGesture/public/Gautham_L_Recordings/"

categorization = [["acpower", "Hardware"], ["algorithm", "Programming"], ["antenna", "Hardware"],
                  ["authentication", "Cryptography"], ["authorization", "Cryptography"], ["bandwidth", "Networking"],
                  ["bluetooth", "Networking"], ["browser", "Networking"], ["cloudcomputing", "Data"],
                  ["datacompression", "Data"], ["datalinklayer", "Data"], ["datamining", "Data"],
                  ["decryption", "Cryptography"], ["domain", "Networking"], ["email", "Networking"],
                  ["exposure", "Cryptography"], ["filter", "Programming"], ["firewall", "Cryptography"],
                  ["flooding", "Networking"], ["gateway", "Networking"], ["hacker", "Cryptography"],
                  ["header", "Data"], ["hotswap", "Hardware"], ["hyperlink", "Networking"],
                  ["infrastructure", "Hardware"], ["integrity", "Cryptography"], ["internet", "Networking"],
                  ["intranet", "Networking"], ["latency", "Data"], ["loopback", "Networking"],
                  ["motherboard", "Hardware"], ["network", "Networking"], ["networking", "Networking"],
                  ["networklayer", "Networking"], ["node", "Programming"], ["packet", "Data"],
                  ["partition", "Hardware"], ["passwordsniffing", "Cryptography"], ["patch", "Programming"],
                  ["phishing", "Cryptography"], ["physicallayer", "Networking"], ["ping", "Networking"],
                  ["portscan", "Networking"], ["presentation Layer", "Networking"], ["protocol", "Networking"]]

for gesture in categorization:
    for directory in [d for d in listdir(path_to_videos) if isdir(join(path_to_videos, d))]:
        if gesture[0] in directory:
            with open(path_to_videos + directory + "/category.txt", "w") as f:
                f.write(gesture[1])
