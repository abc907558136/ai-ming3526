from numpy import *
import operator

def createDayaSet():
    group = array([[1,0,1,1],[1,0,1,0],[0,0],[0,0,1]])
    labels = ['A','B','C','D']
    print(group)
    return group, labels

createDayaSet()
