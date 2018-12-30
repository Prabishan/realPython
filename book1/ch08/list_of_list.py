def enrollment_stats():
    std_enroll = []
    tut_fee = []
    for i in universities:
        std_enroll.append(i[1])
    for i in universities:
        tut_fee.append(i[2])
    print(std_enroll)
    print(tut_fee)
    return std_enroll,tut_fee
def mean(enrol_stats):
    sum = 0
    for i in range(len(enrol_stats)):
        sum += enrol_stats[i]
    return int(sum/len(enrol_stats))


universities = [ ['California Institute of Technology', 2175, 37704],
                 ['Harvard', 19627, 39849],
                 ['Massachusetts Institute of Technology', 10566, 40732],
                 ['Princeton', 7802, 37000],
                 ['Rice', 5879, 35551],
                 ['Stanford', 19535, 40569],
                 ['Yale', 11701, 40500]]



total = enrollment_stats()
print(mean(total[0]))
