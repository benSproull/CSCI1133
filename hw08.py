# Problem A
def get_word_list(filename):
    '''
    Purpose: To get a list of words from a file
    Parameter(s): filename = the name of the file that the user wants to get the text from
    Return Value: returns a list of words from a file
    '''

    wlist = []
    fp = open(filename)
    words = fp.readlines()

    for lines in words:
        word = lines.split()
        wlist.append(word)
    print(wlist)

# Problem B
def durdle_game():
    import random
    '''
    Purpose:
        Lets the user play a game where they try to match a target word
    Parameters:
        None
    Return Value:
        The number of guesses it took the user to get the correct word.
    '''
    fp = open('words_full.txt')
    random_word = fp.readlines()
    a = random_word.split()
    target = str(random.choice(random_word))
    print(target)


    print("Welcome to Durdle!")
    guess = ''
    count = 0


    while guess != target:
        guess = input("Enter a guess:")

        print('              '+durdle_match(guess, target))
        count += 1
        if durdle_match(guess, target) == 'GGGGG':
            return "Congratulations, you got it in",count,"guesses!"


    return count

def durdle_match(guess, target):
    '''
    Purpose:
        Determines which letters in the user's guess match the target
    Parameters:
        guess - a 5-letter string representing the user's guess
        target - a 5-letter string representing the target word
    Return Value:
        A 5-letter string, where each letter represents whether or not
        the letter in that position is correct.  'B' means the letter
        is not present in the target, 'Y' means that it's present in
        a different location, 'G' means it's in the correct location.
    '''
    fp = open('words_full.txt')
    words = fp
    matches = ''
    for i in range(5):
        if guess[i] not in target:
            matches += 'B'
        elif guess[i] == target[i]:
            matches += 'G'
        else:
            matches += 'Y'
    #if matches == 'GGGGG':

    return matches

# Problem C
def grade_quiz(filename):
    '''
    Purpose: To make life easier by creating an automatic grading function
    Parameter(s): filename = the name of the file that a student would submit to be ran through the program to check their answers
    Return Value: Returns the students score for the quiz as a string
    '''

    score = [0,0,0]

    try:
        fp = open(filename)
    except FileNotFoundError:
        return score

    answers = fp.read()
    z = answers.split()

    try:
        if z[0] == '':
            score[0] = 0

        elif z[0] == '42':
            score[0] = 2
        else:
            score[0] = 1

        if z[1] == '':
            score[1] = 0
        elif z[1] == 'Belgium':
            score[1] = 2
        else:
            score[1] = 1

        if z[2] == '':
            score[2] = 0
        elif z[2] == 'Towel':
            score[2] = 2
        else:
            score[2] = 1
    except IndexError:
        return score

    return score

#Problem D
def grade_all(grade_file):
    '''
    Purpose: to take the scores and put them into a csv file that can be opened as a spreadsheet for automatic grading
    Parameter(s): grade_file = the file that is going to be copied and written on too for the grades
    Return Value: returns nothing but makes a copy of the file with the transcribed data written to it
    '''

    fp = open(grade_file)
    for line in fp:
        z = line.split(",")
        print(z)


























#
