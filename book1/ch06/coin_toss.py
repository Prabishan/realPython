#simulating the results of series of coin tosses and tracking their results
from random import randint

flips = 0
trials = 10000

for trial in range(1,trials):
    toss = randint(0,1)
    flips+=1
    while randint(0,1) == toss:
        flips+=1
    flips+=1
print("Total flips: ",flips)
print("Average flips:{0}".format(flips/trials))
