


def glorious(val):

    '''
    Purpose:
        To find out wheather a number is glorious or not
    Parameters:
        val = user inputed number
        i = the range that the program runs through
        t = true if the val number is not glorious
        f = false if the val number is glorious
    Return Value:
        Returns either true or false, true if it is not glorious and false if the number is
    '''

    t = True
    f = False
    i = 10
    for i in range(10,50):
        if val % i == 0:
            return f


    else:
         return t

def count_glorious(low, high):
    a = 0
    i = 0
    glo = glorious(a)
    if low > high:
        return 0
    else:
        for a in range(low, high + 1):
            if glorious(a):
                i += 1

        return i

def durdle_match(guess, target):

    '''
    Purpose:
        A guessing game where the user guesses a word then the program outputs a code to help the user
    Parameters:
        guess = the users guess to what the target word is
        target = the 5 letter word that the user is trying to guess
    Return Value:
        Program returns a 5 letter combanation usimg the letters G, Y, and B
            G = the guessed letter is correct and in the correct location
            Y = the guessed letter is correct but in the wrong location
            B = the guessed letter is wrong

    '''

    g = str(guess)
    t = str(target)

    if g[0] == t[0]:
        print("'G", end = '')
    elif g[0] == t[1] or g[0] == t[2] or g[0] == t[3] or g[0] == t[4]:
        print("'Y", end = '')
    else:
        print("'B", end = '')

    if g[1] == t[1]:
        print('G', end = '')
    elif g[1] == t[0] or g[1] == t[2] or g[1] == t[3] or g[1] == t[4]:
        print('Y', end = '')
    else:
        print('B', end = '')

    if g[2] == t[2]:
        print('G', end = '')
    elif g[2] == t[0] or g[2] == t[1] or g[2] == t[3] or g[2] == t[4]:
        print('Y', end = '')
    else:
        print('B', end = '')

    if g[3] == t[3]:
        print('G', end = '')
    elif g[3] == t[0] or g[3] == t[1] or g[3] == t[2] or g[3] == t[4]:
        print('Y', end = '')
    else:
        print('B', end = '')

    if g[4] == t[4]:
        print("G'")
    elif g[4] == t[0] or g[4] == t[1] or g[4] == t[2] or g[4] == t[3]:
        print("Y'")
    else:
        print("B'")

def durdle_game(target):
    '''
    Purpose:
        A guessing game where the user guesses a word then the program outputs a code to help the user guess the original word
    Parameters:
        target = a 5 letter word that the user is trying to guess
        guess = the users guess to what the target word is
    Return Value:
        program returns once the user has guessed the target word correctly and returns how many guesses it took
    '''
    guess = input('Guess a 5 letter word: ')
    durd = durdle_match(guess, target)
    i = 1
    while str(guess) != str(target):
        guess = input('Guess again: ')
        durd = durdle_match(guess, target)
        i += 1
    print('It took', i,'guesses')
    return i
    
