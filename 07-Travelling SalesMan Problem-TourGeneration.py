#-------------------------------------------------------------
# To solve Travelling Sales Man Problem:
# Generate Random Tours
#-------------------------------------------------------------
# Problem Statement:
# Cover all the cites with minimum distance.
#
# City=['A', 'B', 'C', 'D', 'E', 'F']
#-------------------------------------------------------------
# Python version: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random


#-------------------------------------------------------------
# Step 2: Parameter Setting
#-------------------------------------------------------------
city=['A', 'B', 'C', 'D', 'E', 'F']
iterations  = 10  # Number of Inerations


#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------

# Generate Random Tours
for i in range(iterations):
    tours = "".join(random.sample(city,len(city)))
    tours = tours + tours[0]    # Adding First City to the End of Tour
    print tours












