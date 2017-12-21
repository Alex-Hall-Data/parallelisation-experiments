#require pp module to be in working directory in order to run
#must run ppserver.py on each of the working nodes
#to run ppserver: python ppserver.py -w -<NUMBER OF CORES> -a -d
#number of local cores and number of iterations per core must be changed below

from __future__ import division
import random
import time
import multiprocessing
from multiprocessing import Pool
import pp





#function to perform Monte Carlo simulation
def monte_carlo(iterations):
    
    centre = iterations/2
    radius= iterations/2
    global counter
    counter=0
    for i in range (int(iterations)):
        x=random.uniform(1,iterations)
        y=random.uniform(1,iterations)

        if (x-centre)**2 + (y-centre)**2 < radius**2:
            counter +=1

    return(counter)
    print(counter)


  #  print(result)
   # print("Needed %ss" % (time.time() - start))
            
if __name__=='__main__':

	start=time.time()
    	
#number of iterations PER CORE
	n=1000000

#split job into 12 - 1 for each core in network (MAY NOT BE USING LOCAL SERVER ATM)
	NBR_JOBS=16
#quad core processors
	NBR_LOCAL_CPUS=4
#can autodiscover by using ("*"). DONT THINK THIS USES LOCAL SERVER
	ppservers=("*",)
	job_server=pp.Server(ppservers=ppservers,ncpus=NBR_LOCAL_CPUS)

#number of trials per process. total number of iterations/number of cpus
	nbr_trials_per_process =[n]*NBR_JOBS 

#send jobs to servers - not sure what last 2 arguments are
	jobs=[]
	for n in nbr_trials_per_process:
            job=job_server.submit(monte_carlo,(n,),(),("random",))
            jobs.append(job)

	#vector of results from each job
	nbr_in_circles=[job() for job in jobs]

	print(4*sum(nbr_in_circles)/(NBR_JOBS*n))
	print("required", (time.time()-start),"seconds")
