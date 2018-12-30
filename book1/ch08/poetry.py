from random import choice

noun = ["fossil","horse","aardvark","judge","chef","mango","extrovert","gorilla"]
verb = ["kicks", "jingles","bounces","slurps","meows","explodes","curdles"]
adjective = ["furry","balding","incredulous","fragrant","exuberant","glistening","pale","enormous black","piercing blue","dark night"]
prep = ["againt","after","into","beneath","upon","for","in","like","over","within"]
adverb = ["curiously","extravagantly","tantalizingly","furiously","sensuously"]

def makePoem():
    #choosing noun
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)

    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)
    #choosing verb
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)

    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 == choice(verb)
     #choosing adjective
    adj1 = choice(adjective)
    adj2 = choice(adjective)
    adj3 = choice(adjective)

    while adj1 == adj2:
        adj2 = choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 == choice(adjective)
    #choosing adverb
    adv1 = choice(adverb)

    #chosing preposition
    p1 = choice(prep)
    p2 = choice(prep)

    while p1 == p2:
        p2 = choice(prep)

    if "aeiou".find(adj1[0])!= -1 :
        strt = "An"
    else:
        strt = "A"

    poem = "{} {} {}\n\n".format(strt,adj1,n1)
    poem = poem + "{} {} {} {} {} the {} {} \n".format(strt, adj1,n1,v1,p1,adj2,n2)
    poem = poem + "{}, the {} {}\n".format(adv1,n1,v2)
    poem = poem + "the {} {} {} a {} {}".format(n2,v3,p2,adj3,n3)

    return poem
print(makePoem())

    

























    
