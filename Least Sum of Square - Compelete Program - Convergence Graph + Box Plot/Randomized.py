#-------------------------------------------------------------
#                       Randomization
#-------------------------------------------------------------
# To solve optimization problem (minimization) using randomly.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
import FitnessFunction as FF     # Fitness Function and Parameters
from __main__ import *           # Import 'q' variable from Merge.py where q defines which fitness function to use
 
FF.INIT(q)                       # INIT Function in FitnessFunction File 

#-------------------------------------------------------------
# Step 2: Random Algorithm  Parameters
#-------------------------------------------------------------
AlgoName    = "Random"+str(q)	# Algo Name
Iterations  = 50                # Number of Iterations
BestFitness = 9999999999        # Store Best Fitness Value
BestChromosome = []             # Store Best Chromosome

FunEval=0

Runs_Random=[]                  # No of iterations
Fitness_Random=[]               # Set of sets of best fitness for all iterations in each run eg:fitnesses in 1st run --(15,12,6),fitnesses in 2nd run --(17,15,12) so it has [[15,12,6],[17,15,12]]
Buffer=[]                       # Stores best fitness obtained in each run
Chromos=[]                      # Stores best chromosome obtained in each run
Runs=10                         # No of times the algo is repeated
BestFitnessConv=[]              # Best fitnesses obtained in each iteration for the best run

#-------------------------------------------------------------
# Step 3: Problem parameters
#-------------------------------------------------------------
# FitnessFunction is defined in FitnessFunction.py file



#-------------------------------------------------------------
# Step 4: Fitness Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in FitnessFunction.py file



#-------------------------------------------------------------
# Step 5: Start Program
#-------------------------------------------------------------


for k in range(Runs):                   # Multiple Runs of DE
        
        BestFitness = 9999999999        # Store Best Fitness Value
        BestChromosome = []             # Store Best Chromosome
        R=[]                            # No of iterations for a particular Run
        F=[]                            # Fitness Obtained in each iteration for a particular Run
        FunEval=0

        for i in range(0,Iterations):
                Chromosome = []
                for j in range(0,FF.D):
                    Chromosome.append(round(random.uniform(FF.LB,FF.UB),2))
                Fitness = round(FF.MyFitFun(q,Chromosome),2)
                FunEval=FunEval+1
                if Fitness < BestFitness:
                        BestFitness=Fitness
                        BestChromosome=Chromosome
                R.append(i)
                F.append(BestFitness)
        Chromos.append(BestChromosome)
        Buffer.append(BestFitness)
        Fitness_Random.append(F)

bestI=0                         # Index for the best run
for m in range(Runs):           # Finding Best Run
    if Buffer[bestI]>Buffer[m]:
        bestI=m
        
BestFitnessConv=Fitness_Random[bestI]
Runs_Random=R

BestChromosome=Chromos[bestI]
BestFitness=round(FF.MyFitFun(q,BestChromosome),2)

#-------------------------------------------------------------
# Step 6: Writing fitnesses obtaine for the best Run
#-------------------------------------------------------------
fp=open('Result'+AlgoName+'.csv','w')
fp.write("Iteration,Fitness\n")
for m in range(Iterations):
    fp.write(str(m)+','+str(BestFitnessConv[m])+'\n')
fp.close()


print "***********************************************************************************"
print "Randomized"
print "Buffer"
print Buffer
print "\nBest Chromosome:", BestChromosome, "\nBestFitness:", BestFitness
print "Function Evaluations:",FunEval
print "\n\nResults in File Result"+AlgoName+".csv"
print "***********************************************************************************"

