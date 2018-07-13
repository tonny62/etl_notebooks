def isTH(stringInput):
    ''' This function check whether it contains TH char > EN char or not '''
    thainess = 0
    for i in stringInput:
        thainess +=  ((ord(i) in range(3585, 3675+1)) or (ord(i) in range(44, 57+1)))
    if (thainess/len(stringInput) >= 0.5):
        return 1
    else:
        return 0
