def sortlist(list):
    print(list)
    xchange = True
    while(xchange):
        xchange = False
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                
                list[i], list[i+1] = list[i+1], list[i]
                xchange = True
    return list




