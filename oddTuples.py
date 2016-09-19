def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return tuple(aTup[x] for x in range(0, len(aTup), 2))
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))