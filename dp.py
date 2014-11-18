#!/usr/bin/env python3
#Alec Snyder
#Diassociation algorithm
import sys
import random


def usage():
    print("Usage: dp.py [inputFile]")
    print("")

def remPunc(word):
    new=""
    for c in word:
        if(c.isalpha()):
            new+=c.lower()
        elif(c.isnumeric()):
            new+=c.lower()
    return new

if len(sys.argv)>2:
    usage()

if len(sys.argv)==2:
    f=open(sys.argv[1], "r")
else:
    f=sys.stdin

dp={}
words=[]
for line in f:
    for wd in line.split():
        words.append(remPunc(wd))
words.append("END")


for i in range(len(words)):
    if(words[i]=="END"):
        dp["END"]="END"
    elif(words[i] in dp):
        dp[words[i]].append(words[i+1])
    else:
        dp[words[i]]=[]
        dp[words[i]].append(words[i+1])

start=words[0]
while(True):
    if(start=="END"):
        print("")
        break
    print(start, end=" ")
    nextIndex=random.randrange(0,len(dp[start]))
    start=dp[start][nextIndex]

exit(0)
