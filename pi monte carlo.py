
import random
import time

def pi(iterations):
    start = time.time()
    centre = iterations/2
    radius = iterations/2
    counter=0
    for i in range(1,iterations):
        x=random.uniform(1,iterations)
        y=random.uniform(1,iterations)

        if (x-centre)**2 + (y-centre)**2 < radius**2:
            counter+=1

    result=4*(counter/iterations)
    print(result)
    print("Needed %ss" % (time.time() - start))
            
