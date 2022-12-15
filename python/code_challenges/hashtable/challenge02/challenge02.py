def find_first_repeated_word(string):
    '''
    A function that takes a string and then splits it to a list,the function also creates a hashset. Then we loop through the list, if the 
    '''
    list = string.split()
    hash = set()
    for repeated_word in list:
        if repeated_word in hash:
            return repeated_word
        else:
            hash.add(repeated_word)
    return 'No Repetition'

