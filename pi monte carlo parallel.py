

import random
import time
import multiprocessing
from multiprocessing import Pool





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
    start = time.time()
    iterations=1600000

    #detarmine number of cores
    np = multiprocessing.cpu_count()
    print ('You have {0:1d} CPUs'.format(np))

#determine how many processes each core gets
    part_count=[iterations/np for j in range(np)]

        #Create the worker pool
    # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
    pool = Pool(processes=np)

        # parallel map
    count=pool.map(monte_carlo, part_count)

    print ("Estimated value of Pi:: ", sum(count)/(iterations*1.0)*4 )
    print("Needed %ss" % (time.time() - start))
