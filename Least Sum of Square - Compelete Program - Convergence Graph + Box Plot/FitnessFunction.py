import math as m
import csv
import numpy as np

#----------------------------------------------
#Problem Parameters
#----------------------------------------------


D=0
LB=0
UB=0
OV=0
totalCount=0
dataSet=None
inputFileName   = None

def INIT(q):
    global dataSet,totalCount,D,LB,UB,inputFileName
    if q==1:            #1st Function
        
        inputFileName   = "inputData.csv"   # input data file name

        # Reading Data: from CSV to Matrix
        dataSet=np.loadtxt(open(inputFileName,"r"),delimiter=",",skiprows=1)

        # Re assinging problem parameters
        D       = dataSet.shape[1] - 1      # Problem Dimension
        totalCount=dataSet.shape[0]
        LB      = -10  # Set Size Lower Bound
        UB      = 10   # Set Size Upper Bound

       
    elif q==2:       #2nd Function
        D=20
        LB=-30
        UB=30
        OV=0

def MyFitFun(q,x):
    global dataSet,totalCount,D,LB,UB
    if q==1:            #1st  Function
        s=0
        for i in range(totalCount):
            s = s + abs(dataSet[i][0] - dataSet[i,1:].dot(x))
        return round(s,2)
             

    elif q==2:       #2nd Function
        D=50
        LB=-30
        UB=30
        s=0
        
        for i in range(0,D):
            s=s+x[i]
        return s
            
        

        

