import math as m
D=100
LB=-1
UB=1
def FitnessFunction(x):
    s=0
    p=0
    q=0
    for i in range(1,D-1):
        a=x[i-1]*m.sin(x[i])+m.sin(x[i+1])
        b=((x[i-1]**2)-2*x[i]+3*x[i+1]-m.cos(x[i])+1)
        p = p + (20 * i * (m.sin(a) ** 2))
        q = q + (i * m.log10(1 + i * (b ** 2)))
    for i in range(0,D):
        s = s + (i * x[i] * x[i])




    return round(s+p+q,2)