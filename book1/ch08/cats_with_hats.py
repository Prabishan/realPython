def cats_with_hats(cats):
    cats_with_hats_on = []
    for i in range(1,1001):
        for j in range(1,1001):
            if j%i == 0:
                if cats[j] == True:
                    cats[j] = False
                else:
                    cats[j] = True
    for i in range(1,1001):
        if cats[i] == True:
            cats_with_hats_on.append(i)
    return cats_with_hats_on

cats = [False] * (1000+1)

print(cats_with_hats(cats))
