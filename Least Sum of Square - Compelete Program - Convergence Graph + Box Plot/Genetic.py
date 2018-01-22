#-------------------------------------------------------------
#               Genetic Algorithm (GA)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using GA.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
from copy import deepcopy
import FitnessFunction as FF    # Fitness Function and Parameters
from __main__ import *          # Import 'q' variable from Merge.py where q defines which fitness function to use

FF.INIT(q)                      # INIT Function in FitnessFunction File 


#-------------------------------------------------------------
# Step 2: GA parameters
#-------------------------------------------------------------
AlgoName    = "GA"+str(q)   # Algo Name
Iterations  = 50            # Number of Iterations
PopSize     = 10            # Population Size(i.e Number of Chromosomes)
Pop         = []            # Store Population with Fitness
CR 	    = 0.9  	    # Crossover Rate
MR 	    = 0.8           # Mutation Rate
MaxFunEval  = 100000        # Maximum allowable function evaluations
FunEval	    = 0		    # Count function evaluations
GlobalBest  = []            # Rember Global Best after every iteration

Runs_GA=[]                  # No of iterations
Fitness_GA=[]               # Set of sets of best fitness for all iterations in each run eg:fitnesses in 1st run --(15,12,6),fitnesses in 2nd run --(17,15,12) so it has [[15,12,6],[17,15,12]]
Buffer=[]                   # Stores best fitness obtained in each run
Chromos=[]                  # Stores best chromosome obtained in each run
Runs=10                     # No of times the algo is repeated# Stores best chromosome obtained in each run
BestFitnessConv=[]          # Best fitnesses obtained in each iteration for the best run

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
# FitnessFunction is defined in fitnessFunction.py file


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


# Function 4: Perform Crossover Operation
def Crossover():
    global FunEval
    for i in range(0,PopSize):

        if (random.random() <= CR):

            # Choose two random indices
            i1,i2=random.sample(range(0,PopSize), 2)

            # Parents
            p1=Pop[i1]
            p2=Pop[i2]

            # Choose a crossover point 
            pt = random.randint(1,FF.D-2)

            # Generate new childs 
            c1=p1.Chromosome[0:pt] + p2.Chromosome[pt:]
            c2=p2.Chromosome[0:pt] + p1.Chromosome[pt:]

            # Get the fitness of childs 
            c1Fitness=FF.MyFitFun(q,c1)
            FunEval = FunEval + 1
            c2Fitness=FF.MyFitFun(q,c2)
            FunEval = FunEval + 1

            # Select between parent and child
            if c1Fitness < p1.Fitness:
                Pop[i1].Fitness=c1Fitness
                Pop[i1].Chromosome=c1
                
            if c2Fitness < p2.Fitness:
                Pop[i2].Fitness=c2Fitness
                Pop[i2].Chromosome=c2


# Function 5: Perform Mutation Operation
def Mutation():
    global FunEval,q
    
    for i in range(0,PopSize):

        if (random.random() <= MR):
            
            # Choose random index
            r=random.randint(0,PopSize-1)

            # Choose a parent
            p=deepcopy(Pop[r])

            # Choose mutation point 
            pt = random.randint(0,FF.D-1)    
            
            # Generate new childs
            c=deepcopy(p.Chromosome)

            # Mutation
            c[pt] = round(random.uniform(FF.LB,FF.UB),2)

            #Get the fitness of childs
            cFitness=FF.MyFitFun(q,c)
            FunEval=FunEval+1

            # Select between parent and child
            if cFitness < p.Fitness:
                Pop[r].Fitness=cFitness
                Pop[r].Chromosome=c
  

#-------------------------------------------------------------
# Step 5: Start Program
#-------------------------------------------------------------

for k in range(Runs):
    Pop         = []        # Store Population with Fitness
    MaxFunEval  = 100000    # Maximum allowable function evaluations
    FunEval	= 0	    # Count function evaluations
    GlobalBest  = []        # Rember Global Best after every iteration
    Init()
    GlobalBest=Pop[0]
    MemoriseGlobalBest()
    R=[]                    # No of iterations for a particular Run
    F=[]                    # Fitness Obtained in each iteration for a particular Run


        
    for i in range(0,Iterations): # Running till number of iterations
        Crossover()
        Mutation()
        MemoriseGlobalBest()
        R.append(i)
        F.append(GlobalBest.Fitness)
        
    Chromos.append(GlobalBest.Chromosome)    
    Buffer.append(GlobalBest.Fitness)
    Fitness_GA.append(F)

bestI=0                                 # Index for the best run
for m in range(Runs):                   # Finding Best Run
    if Buffer[bestI]>Buffer[m]:
        bestI=m

BestFitnessConv=Fitness_GA[bestI]       # Best Fitness List in different iterations for the best Run
Runs_GA=R

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
print "Genetic"
print "Buffer"
print Buffer
print "\nBest Chromosome:", GlobalBest.Chromosome, "\nBest Fitness:", GlobalBest.Fitness
print "Total Function FunEval: ",FunEval
print "\n\nResults in File Result"+AlgoName+".csv"
print "***********************************************************************************"




