# Author: Rishub Handa 
from rng import randomNumberGenerator
from numpy import log as ln 

# Log all times it took to realize call 
rng_idx = 1
l = 1/12

times = []

# Calculating inverse cdf 
# p = 1-e^(-lx)
# 1-p = e^(-lx)
# ln(1-p) = -lx
# -ln(1-p)/l = x

def x_inv_cdf(p): 
    return -ln(1-p) / (1/12)


# For each customer figure out time to pick up or not 
for c in range(500): 

    t = 0

    # For each call iteration (up to 4) 
    for i in range(4):

        # Dial up phone 
        t += 6 

        # Generate rng 
        rng = randomNumberGenerator(rng_idx)
        rng_idx += 1

        # Parition 0, 1 space on RV outcomes 

        if rng < 0.2: 
            # Busy signal 
            t += 3 

        elif rng < 0.5: 
            # Unavailable 
            t += 25 

        else: 
            # Available 

            # Generate a completely new random number [0, 1] (available is independent of X)
            p = randomNumberGenerator(rng_idx)
            rng_idx += 1

            pick_up_time = x_inv_cdf(p)
            # print(pick_up_time)

            # If available, end the call and break 
            if pick_up_time <= 25: 
                t += pick_up_time
                t += 1 
                break 

            # Else keep going 
            else: 
                # Wait a max of 25 seconds 
                t += 25 

        # End the call 
        t += 1

    times.append(t)


times.sort()

# Return the x such that F(x) = p. If p is between increments of 1/500, return the average of the two closest values. 
# P(W <= some w) = 0.909, figure out w 

def w_inv_cdf(p):

    n = len(times)

    if p == 0: return times[0]

    for i in range(n): 
        if (i+1)/n == p: 
            return times[i]
        
        elif (i+1)/n > p: # This will crash on p = 0.9999, but it should be fine for this 
            return (times[i]+times[i+1])/2

    if p == 1: return times[-1]



# Return the % of times covered until w > n[i]
# P(W <= some_time) = some probability 
# P(W <= 50)
def w_cdf(w): 

    n = len(times)

    if w < times[0]: return 0
    
    for i in range(n): 
        if w >= times[i] and w < times[i+1]: 
            return (i+1)/n
    
    return 1



# Instructions: 
# Run python3 -i monte_carlo.py
# To get the cdf of w, run w_cdf(w) in the terminal 
# To get the inv_cdf of w, run w_inv_cdf(p) in the terminal 

import numpy as np 
print("mean", np.mean(times))

import pandas as pd 

df = pd.DataFrame(times, columns=["times"])
df.to_csv("times.csv")


