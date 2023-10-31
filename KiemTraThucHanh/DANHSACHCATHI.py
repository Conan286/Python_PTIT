from math import *
from functools import cmp_to_key
import re
import io
import os
import sys
import time
import array as arr
class CATHI:
    def __init__(self,id,day,hour,room):
        self.__id = id
        self.__day = day
        self.__hour = hour
        self.__room = room

    def GetId(self):
        return self.__id

    def getDay(self):
        return self.__day

    def getHour(self):
        return self.__hour

    def GetRoom(self):
        return self.__room

    def __str__(self):
        answer = self.__id+" "+self.__day+" "+self.__hour+" "+self.__room
        return answer

def cmp(a,b):
    t1 = a.getDay().split('/')
    t2 = b.getDay().split('/')
    if t1[-1]!=t2[-1]:
        return int(t1[-1])-int(t2[-1])
    if t1[-2]!=t2[-2]:
        return int(t1[-2])-int(t2[-2])
    if t1[-3]!=t2[-3]:
        return int(t1[-3])-int(t2[-3])
    t1 = a.getHour().split(':')
    t2 = b.getHour().split(':')
    if t1[0] != t2[0]:
        return int(t1[0]) - int(t2[0])
    if t1[1] != t2[1]:
        return int(t1[1]) - int(t2[1])
    return a.GetId()<b.GetId()
def main():
    file = open('CATHI.in','r')
    input = file.read().split()
    n = int(input[0])
    a = []
    id = 1
    for i in range(n):
        a.append(CATHI('C{:03d}'.format(i+1),input[id],input[id+1],input[id+2]))
        id += 3

    for cathi in sorted(a,key=cmp_to_key(cmp)):
        print(cathi)

if __name__ == '__main__':
    main()