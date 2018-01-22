import os

''' Fitness Function Number

q == 1      for Least Sum of Squares

q == 2      for minimum Sum of parameters

'''

q=1

import Randomized as R
import Genetic as G
import Differential as D
import PSO as P
import matplotlib.pyplot as plt
import pylab as pl


#----------------------------
#Function for saving Files----boxplot and Convergence graphs stored in same folder as this file
#-----------------------------

def save(path, ext='png', close=True, verbose=True):
    """Save a figure from pyplot.
    Parameters
    ----------
    path : string
        The path (and filename, without the extension) to save the
        figure to.
    ext : string (default='png')
        The file extension. This must be supported by the active
        matplotlib backend (see matplotlib.backends module).  Most
        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.
    close : boolean (default=True)
        Whether to close the figure after saving.  If you want to save
        the figure multiple times (e.g., to multiple formats), you
        should NOT close it in between saves or you will have to
        re-plot it.
    verbose : boolean (default=True)
        Whether to print information about when and where the image
        has been saved.
    """
    
    # Extract the directory and filename from the given path
    directory = os.path.split(path)[0]
    filename = "%s.%s" % (os.path.split(path)[1], ext)
    if directory == '':
        directory = '.'

    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # The final path to save to
    savepath = os.path.join(directory, filename)

    if verbose:
        print("Saving figure to '%s'..." % savepath),

    # Actually save the figure
    plt.savefig(savepath)
    
    # Close it
    if close:
        plt.close()

    if verbose:
        print("Done")

#---------------------------------------------------------------------------
# Running all algos...
#---------------------------------------------------------------------------

os.system("python Randomized.py")       # Running Randomized Algo
os.system("python Genetic.py")          # Running Gentic Algo
os.system("python Differential.py")     # Running Differential Algo
os.system("python PSO.py")              # Running PSO Algo

#---------------------------------------------------------------------------
# Generating Convergence Graph...
#---------------------------------------------------------------------------

Randomized=plt.plot(R.Runs_Random,R.BestFitnessConv,'r',label='Randomized')
Genetic=plt.plot(G.Runs_GA,G.BestFitnessConv,'b',label='Genetic')
Differential=plt.plot(D.Runs_DE,D.BestFitnessConv,'g',label="Differential")
Pso=plt.plot(P.Runs_PSO,P.BestFitnessConv,'y',label="PSO")

#---------------------------------------------------------------------------
# Labelling x and y axis of Convergence Graph...
#---------------------------------------------------------------------------

plt.xlabel("Runs")
plt.ylabel("Fitness")

#---------------------------------------------------------------------------
# Title for Convergence Graph...
#---------------------------------------------------------------------------

if q==1:
    a="Least Sum of Squares"
elif q==2:
    a="Least Sum of Parameters"

plt.title("Random Vs GA Vs DE Vs PSO-"+a+"-function")

#---------------------------------------------------------------------------
# Grid in the background of COnvergence graph
#---------------------------------------------------------------------------

plt.grid(True)

#---------------------------------------------------------------------------
# Legend Box on the upper right corner of Convergence Graph defining what color represents what algo
#---------------------------------------------------------------------------

plt.legend([Randomized,Genetic,Differential,Pso],['Randomized','Genetic','Differential','PSO'])
plt.legend(bbox_to_anchor=(0.9, 0.87),bbox_transform=plt.gcf().transFigure)

#---------------------------------------------------------------------------
# Saving Convergence Graph
#---------------------------------------------------------------------------

save("Convergence", ext="png", close=False, verbose=True)
save("Convergence", ext="svg", close=True, verbose=True)

#---------------------------------------------------------------------------
# Input for box plot array-comprising of buffers of all algos
#---------------------------------------------------------------------------

Data=[R.Buffer,G.Buffer,D.Buffer,P.Buffer]

#---------------------------------------------------------------------------
# Seperate figure for plotting Box Plot
#---------------------------------------------------------------------------

plt.figure()

#---------------------------------------------------------------------------
# Generating Boxplot
#---------------------------------------------------------------------------

plt.boxplot(Data)

#---------------------------------------------------------------------------
# Indicating which boxplot belongs to which algo
#---------------------------------------------------------------------------

plt.xticks([1,2,3,4],['Random','GA','DE','PSO'])

#---------------------------------------------------------------------------
# Saving Box Plot
#---------------------------------------------------------------------------

save("BoxPlot", ext="png", close=False, verbose=True)
save("BoxPlot", ext="svg", close=True, verbose=True)


