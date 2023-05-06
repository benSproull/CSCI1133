#Problem A
def cookie_order(cookie_dict):
    '''
    Purpose: To figure out how many boxes of cookies a person should buy to get a desired amount
    Parameter(s): cookie_dict = a user inputted dictionary with what cookies they want and how many
    Return Value: returns the number of boxes to buy for each type of cookie
    '''

    import math
    order = {}
    #order = []
    for cookie, count in cookie_dict.items():
        #boxes = f'{cookie}: {(math.ceil(count / 30))}'
        boxes = math.ceil(count / 30)
        order[cookie] = boxes
        #order.append(boxes)
    return order

#Problem B
def follow_words(text):
    '''
    Purpose: To find the outcome of words that come after words in a sentence string
    Parameter(s): text is the user entered string
    Return Value: returns a dictionary of a word and what word/s come after it in a sentence
    '''

    final_dict = {}
    text = text.split()
    for i in range(1,len(text)):
        final_dict[text[i - 1]] = text[i]
    return final_dict


#Problem C
def auto_complete(follows_dict, current):
    '''
    Purpose: takes in a dictionary and finds the key value of the current
    Parameter(s): follows_dict is the dictionary inputted by the user
    Return Value: returns the dictionary value that matches with the current
    '''

    if current in follows_dict.keys():
        x = follows_dict[current]
        return x
    else:
        return follows_dict.keys()

#Problem D
def random_sent(fname, max_length):
    '''
    Purpose: To take a txt file and choose random words with a length of how many words
    Parameter(s): fname is the file name that the user wants to get a random sentence from
    Return Value: returns a random sentence
    '''

    import random
    fp = open(fname)
    text = fp.read()
    text = text.split()
    B = follow_words(text)
    result = []
    for i in range(max_length):
        choice = random.choice(list(B.keys()))
        C = auto_complete(B,choice)
        result.append(C)
    sent = ''.join(result)
    return sent

















    #
