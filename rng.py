# Author: TJ 
# Random number generator with constants from project instructions
# x is the iteration (i in the context of the instructions)
def randomNumberGenerator(i):
    curr = 0
    x = 1000
    a = 24693
    c = 3517
    K = 2 ** 15

    while curr < i: 
        x = (a*x + c) % K 
        curr += 1

    return x / K

# for x in range(1,54):
#     print(str(x)+"   "+str(randomNumberGenerator(x)))

print("u51 u52 u53: {} {} {}".format(randomNumberGenerator(51), randomNumberGenerator(52), randomNumberGenerator(53)))