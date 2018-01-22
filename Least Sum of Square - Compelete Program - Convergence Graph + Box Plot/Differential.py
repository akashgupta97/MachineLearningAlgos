#-------------------------------------------------------------
#               Differential Evolution (DE)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using DE.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------


import random
import time
from copy import deepcopy
import FitnessFunction as FF     # Fitness Function and Parameters
from __main__ import *           # Import 'q' variable from Merge.py where q defines which fitness function to use
 
FF.INIT(q)                       # INIT Function in FitnessFunction File 

#-------------------------------------------------------------
# Step 2: DE Algorithm Parameters
#-------------------------------------------------------------
AlgoName    = "DE"+str(q)	# Algo Name
Iterations  = 50                # Number of Iterations 
PopSize     = 10                # Population Size(i.e Number of Chromosomes)
Pop         = []                # Store Population with Fitness
CR 	    = 0.9  	        # Crossover Rate
F_Inertia  = 0.5                # Inertiea
MaxFunEval  = 100000            # Maximum allowable function evaluations
FunEval	    = 0		        # Count function evaluations
GlobalBest  = []                # Rember Global Best after every iteration

Runs_DE=[]                      # No of iterations
Fitness_DE=[]                   # Set of sets of best fitness for all iterations in each run eg:fitnesses in 1st run --(15,12,6),fitnesses in 2nd run --(17,15,12) so it has [[15,12,6],[17,15,12]]
Buffer=[]                       # Stores best fitness obtained in each run
Chromos=[]                      # Stores best chromosome obtained in each run
Runs=10                         # No of times the algo is repeated
BestFitnessConv=[]              # Best fitnesses obtained in each iteration for the best run

#-------------------------------------------------------------
# Step 3: Problem parameters
#-------------------------------------------------------------
# FitnessFunction is defined in fitnessFunction.py file


class Individual:
    def __init__(self, C, F):
        self.Chromosome=C
        self.Fitness=F


#-------------------------------------------------------------
# Step 4: Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in FitnessFunction.py file


# Function 2: Generate Random Initial Population
def Init():
    global FunEval
    for i in range (0, PopSize):
        Chromosome = []
        for j in range(0,FF.D):
            Chromosome.append(round(random.uniform(FF.LB,FF.UB),2))
        Fitness = FF.MyFitFun(q,Chromosome)
        FunEval = FunEval + 1
        NewIndividual = Individual(Chromosome,Fitness)
        Pop.append(NewIndividual)
        

# Function 3: Remember Global BEST in the Pop;
def MemoriseGlobalBest():
    global GlobalBest
    for p in Pop:
        if p.Fitness < GlobalBest.Fitness:
            GlobalBest=p


# Function 4: Perform DE Operation
def DEOperation():
    global FunEval
    for i in range(0,PopSize):

        # Choose three random indices
        i1,i2,i3=random.sample(range(0,PopSize), 3)

	# Iterate for every Dimension
        NewChild=[]
        for j in range(FF.D):
            if (random.random() <= CR):
                k = Pop[i1].Chromosome[j] + F_Inertia * (Pop[i2].Chromosome[j] - Pop[i3].Chromosome[j])

                # If new dimention cross LB
                if k < FF.LB:
                    k = random.uniform(FF.LB,FF.UB)

                # If new dimention cross LB
                if k > FF.UB:
                    k = random.uniform(FF.LB,FF.UB)
                
                NewChild.append(round(k,2))
                
            else:
                NewChild.append(Pop[i].Chromosome[j])

	# Child Fitness
        NewChildFitness=round(FF.MyFitFun(q,NewChild),2)
        FunEval = FunEval + 1
		
        # Select between parent and child
        if NewChildFitness < Pop[i].Fitness:
            Pop[i].Fitness=NewChildFitness
            Pop[i].Chromosome=NewChild
                


#-------------------------------------------------------------
# Step 5: Start Program
#-------------------------------------------------------------

for kk in range(Runs):      # Multiple Runs of DE

    Pop         = []        # Store Population with Fitness
    MaxFunEval  = 100000    # Maximum allowable function evaluations
    FunEval     = 0	    # Count function evaluations
    GlobalBest  = []        # Rember Global Best after every iteration
    Init()
    GlobalBest=Pop[0]
    MemoriseGlobalBest()
    R=[]                    # No of iterations for a particular Run
    F=[]                    # Fitness Obtained in each iteration for a particular Run

    for i in range(0,Iterations): # Running till number of iterations
        DEOperation()
        MemoriseGlobalBest()
        R.append(i)         
        F.append(GlobalBest.Fitness)
    
    Chromos.append(GlobalBest.Chromosome)
    Buffer.append(GlobalBest.Fitness)
    Fitness_DE.append(F)

bestI=0                                 # Index for the best run
for m in range(Runs):                   # Finding Best Run
    if Buffer[bestI]>Buffer[m]:
        bestI=m

BestFitnessConv=Fitness_DE[bestI]       # Best Fitness List in different iterations for the best Run
Runs_DE=R

GlobalBest.Chromosome=Chromos[bestI]
GlobalBest.Fitness=round(FF.MyFitFun(q,GlobalBest.Chromosome),2)

#-------------------------------------------------------------
# Step 6: Writing fitnesses obtaine for the best Run
#-------------------------------------------------------------
fp=open('Result'+AlgoName+'.csv','w')
fp.write("Iteration,Fitness\n")
for m in range(Iterations):
    fp.write(str(m)+','+str(BestFitnessConv[m])+'\n')
fp.close()

print "***********************************************************************************"
print "Differential"
print "Buffer"
print Buffer
print "\nBest Chromosome:", GlobalBest.Chromosome, "\nBest Fitness:", GlobalBest.Fitness
print "Total Function FunEval: ",FunEval
print "\n\nResults in File Result"+AlgoName+".csv"
print "***********************************************************************************"


