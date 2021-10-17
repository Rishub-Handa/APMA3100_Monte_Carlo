# Author: Rishub Handa 
from rng import randomNumberGenerator
from numpy import log as ln 


# Log all times it took to realize call 
rng_idx = 1
l = 1/12

times = []

# QUESTION: Did I do this right? 
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

            # Redefine probability for inv cdf on (0, 1)
            p = (rng - 0.5) * 2 
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


# QUESTION: Is this the right way to do this? 
# Return the first x such that F(x) >= p
def w_inv_cdf(p):

    n = len(times)

    for i in range(n): 
        if i/n >= p: 
            return times[i]


# QUESTION: Is this the right way to do this? 
# Return the % of times covered until w > n[i]
def w_cdf(w): 

    n = len(times)
    
    for i in range(n): 
        if w > n[i]: 
            return i/n



# Instructions: 
# Run python3 -i monte_carlo.py
# To get the cdf of w, run w_cdf(w) in the terminal 
# To get the inv_cdf of w, run w_inv_cdf(p) in the terminal 


