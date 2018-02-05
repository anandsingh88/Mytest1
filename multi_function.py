lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def revlst(lst):
    
    rlst = lst[::-1]
    return rlst

print(revlst(lst))


def evenlst(lst):
    
    evlst = []
    for x in lst:
        if x % 2 == 0:
            evlst.append(x)
    return(evlst)

print(evenlst(lst))


def oddlst(lst):
    
    odlst = []
    for x in lst:
        if x % 2 == 1:
            odlst.append(x)
    return(odlst)

print(oddlst(lst))


