#-------------------------------------------------------------
#                   Merge Results and Plotting
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------

import os


#-------------------------------------------------------------
# Step 2: Algorithm Execution
#-------------------------------------------------------------

print "Executing Random Algo"
os.system("python 01-Random-Optimization.py")

print "Executing GA"
os.system("python 02-GA-Part-III.py")

print "Executing DE"
os.system("python 04-DE.py")


#-------------------------------------------------------------
# Step 3: Result Merging and Plotting
#-------------------------------------------------------------

# Merge the result files and plot the convergence graph.
print "Merging and Plotting Done"








