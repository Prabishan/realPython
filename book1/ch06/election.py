from random import random
total_A_win = 0
total_B_win = 0

trials = 10000
for trial in range(0,trials):
    A_win = 0
    B_win = 0
    if random() < 0.65 : # 1st reason
        A_win += 1
    else:
        B_win+= 1
    if random() < 0.65: # 2nd region
        A_win += 1
    else:
        B_win += 1
    if random() <0.35: # 3rd region
        A_win += 1
    else:
        B_win += 1
    # overall election outcome
    if A_win>B_win:
        total_A_win+=1
    else:
        total_B_win+=1
print("Total Canditate A wins: {}".format(total_A_win))
print("Total Canditate B wins: {}".format(total_B_win))
print("Probability canditate A wins: ", total_A_win/ trials)
print("Probability candidate B wins: ", total_B_win/ trials)

    
