import operator
d={1:2,4:6,6:3,7:5,9:4}
print(d)
d=sorted(d.items(),key=lambda x: x[1])
d=dict(d)
print(d)
print(d.keys())