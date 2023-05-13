def isAc(S) :
    # Sの先頭の文字がAであるか
    if S[0] != 'A' :
        return False
    
    # Sの先頭から3文字目と末尾から2文字目の間Cが1個含まれるか
    if S[2:-1].count('C') != 1 :
        return False
    
    #  A,Cを除くSのすべての文字は小文字であるか
    if sum(map(str.isupper, S)) != 2 :
        return False
    
    return True
    
print('AC' if isAc(input()) else 'WA')