import math as m
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 50    # Problem Dimension
LB      = -512   # Set Size Lower Bound
UB      = 512    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s1=0
    for i in range(0,D-2):
        s1=s1 + (-(x[i+1]+47)m.sin(m.sqrt(m.abs(x[i+1]+ x[i]/2 + 47))) - (x[i]*m.sin(m.sqrt(m.abs(x[i] - (x[i+1] + 47))))))
    return s1
        














