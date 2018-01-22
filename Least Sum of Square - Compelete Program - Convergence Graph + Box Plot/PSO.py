#-------------------------------------------------------------
#               Particle Swarm Optimization (PSO)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using PSO.
#-------------------------------------------------------------
# Python version used: 2.7
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
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 PSO Parameters
AlgoName    = "PSOBasic"+str(q) # Algo Name
c1	    = 1.5               # Acceleration constant
c2	    = 1.5               # Acceleration constant
w	    = 0.8               # Inertia weight
vLB         = -1                # Velocity Lower Bound
vUB         = 1                 # Velocity Upper Bound

# 2.2 Global Parameters
iterations  = 50                # Number of iterations
PopSize     =  10               # Population Size(i.e Number of Chromosomes)
Pop         = []                # Store Population with Fitness
maxFunEval  = 100000            # Maximum allowable function evaluations
funEval	    = 0		        # Count function evaluations
gBest       = []                # Rember Global Best chromosome
gBestFitness = []               # Rember fitness of Global Best chromosome


Runs_PSO=[]                     # No of iterations
Fitness_PSO=[]                  # Set of sets of best fitness for all iterations in each run eg:fitnesses in 1st run --(15,12,6),fitnesses in 2nd run --(17,15,12) so it has [[15,12,6],[17,15,12]]
Buffer=[]                       # Stores best fitness obtained in each run
Chromos=[]                      # Stores best chromosome obtained in each run
Runs=10                         # No of times the algo is repeated
BestFitnessConv=[]              # Best fitnesses obtained in each iteration for the best run


# 2.4 Stores Particle, ParticleFitness, Velocity, PBest,PBestFitness collectively;
class Individual:
    def __init__(self, P, PF, V, PB, PBF):
        self.particle=P
        self.particleFitness=PF
        self.velocity=V
        self.pBest=PB
        self.pBestFitness=PBF

    def Print(self):
        print "Particle :",self.particle
        print "Particle Fitness :",self.particleFitness
        print "Velocity :",self.velocity
        print "Best Particle :",self.pBest
        print "Best Particle Fitness:",self.pBestFitness



# 2.5 Problem parameters
# Problem Parameters are defined in in fitnessFunction.py file


#-------------------------------------------------------------
# Step 3: Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
# FitnessFunction is defined in fitnessFunction.py file


# Function 2: Generate Random Initial Population
def Init():
    global funEval
    for i in range (0, PopSize):
        particle=[]
        velocity=[]
        for j in range(0,FF.D):
            particle.append(round(random.uniform(FF.LB,FF.UB),2))
            velocity.append(round(random.uniform(vLB,vUB),2))
        
        particleFitness = round(FF.MyFitFun(q,particle),2)
        funEval = funEval + 1
        newIndividual = Individual(particle, particleFitness, velocity, deepcopy(particle), particleFitness)
        Pop.append(newIndividual)
        

# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest():
    global gBest, gBestFitness
    for p in Pop:
        if p.pBestFitness < gBestFitness:
            gBest = deepcopy(p.pBest)
            gBestFitness=deepcopy(p.pBestFitness)
            

# Function 4: Perform PSO Operation
def PSOOperation():
    global funEval

    for i in range(0,PopSize):
        for j in range(0,FF.D):

            # Choose two random numbers
            r1=random.random()
            r2=random.random()

            # Velocity update
            Pop[i].velocity[j] = w * Pop[i].velocity[j] + \
                                c1 * r1 * (Pop[i].pBest[j] - Pop[i].particle[j]) + \
                                c2 * r2 * (gBest[j] - Pop[i].particle[j])

            if Pop[i].velocity[j] < vLB:
                Pop[i].velocity[j] = random.uniform(vLB, vUB)
                                                    
            if Pop[i].velocity[j] > vUB:
                Pop[i].velocity[j] = random.uniform(vLB, vUB)

            # Particle update
            Pop[i].particle[j] = Pop[i].particle[j] + Pop[i].velocity[j]

            if Pop[i].particle[j] < FF.LB:
                Pop[i].particle[j] =  round(random.uniform(FF.LB, FF.UB),2)

            if Pop[i].particle[j] > FF.UB:
                Pop[i].particle[j] =  round(random.uniform(FF.LB, FF.UB),2)


        Pop[i].particleFitness = round(FF.MyFitFun(q,Pop[i].particle),2)
        funEval = funEval + 1

        # Select between particle and pBest
        if Pop[i].particleFitness <= Pop[i].pBestFitness:
            Pop[i].pBest=deepcopy(Pop[i].particle)
            Pop[i].pBestFitness=deepcopy(Pop[i].particleFitness)

        

#-------------------------------------------------------------
# Step 4: Start Program
#-------------------------------------------------------------

for kk in range(Runs):
    Pop         = []        # Store Population with Fitness
    MaxFunEval  = 100000    # Maximum allowable function evaluations
    FunEval     = 0	    # Count function evaluations
    Init()
    gBest=deepcopy(Pop[0].pBest)
    gBestFitness=Pop[0].pBestFitness
    MemoriseGlobalBest()

    R=[]
    F=[]

    for i in range(0,iterations): # Running till number of iterations
        PSOOperation()   
        MemoriseGlobalBest()
        R.append(i)
        F.append(gBestFitness)

    Chromos.append(gBest)
    Buffer.append(gBestFitness)
    Fitness_PSO.append(F)

bestI=0                                 # Index for the best run
for m in range(Runs):                   # Finding Best Run
    if Buffer[bestI]>Buffer[m]:
        bestI=m

BestFitnessConv=Fitness_PSO[bestI]      # Best Fitness List in different iterations for the best Run
Runs_PSO=R

gBest=Chromos[bestI]
gBestFitness=round(FF.MyFitFun(q,gBest),2)

#-------------------------------------------------------------
# Step 6: Writing fitnesses obtaine for the best Run
#-------------------------------------------------------------
fp=open('Result'+AlgoName+'.csv','w')
fp.write("Iteration,Fitness\n")
for m in range(iterations):
    fp.write(str(m)+','+str(BestFitnessConv[m])+'\n')
fp.close()

print "***********************************************************************************"
print "PSO"
print "Buffer"
print Buffer
print "Best particle:", gBest
print "\nBestFitness:", gBestFitness
print "Total Function funEval: ",funEval
print "\n\nResults in File Result"+AlgoName+".csv"
print "***********************************************************************************"


