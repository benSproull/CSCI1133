# Problem A
def collatz(n):
    '''
    Purpose: Count how many steps it takes to get a starting number n down to 1
    Parameter(s): n = the starting number, if n is even it will ÷ it by 2 until it reaches 1
        and if n is odd it will start out by taking n * 3 and adding 1 to make it an even number
    Return Value: Returns the amount of steps it took to get the number 'n' down to 1
    '''

    count = 0
    if n == 1:
        return 1
    elif n % 2 == 0:
        i = n//2
        count += 1
        return count + collatz(i)
    elif n % 2 != 0:
        i = (n*3) + 1
        count += 1
        return count + collatz(i)


def is_target(lines):
    '''
    Purpose: To find out if the message inputted is a decoy or not
    Parameter(s): lines = a list of strings inputted by the user to check if it is a decoy message
    Return Value: Returns either True or False depending on wheather or not the message is a decoy
    '''

    if len(lines) == 0:
        return True
    if lines[0][0] in ['A','C','M','E']:
        return True
    return is_target(lines[1:])


import os
def all_targets(path):
    '''
    Purpose: Does the same as 'is_target()' but looks at multiple txt files at once
    Parameter(s): path = a folder with .txt files within that the user wants to check for decoy messages
    Return Value: Returns the .txt files that have a decoy message within them
    '''

    for file in os.listdir(path):
        if os.path.isfile(path+'/'+file):
            print(path+'/'+file)  #This is a file, print out the path
            fp = open(file)
            lines = fp.readlines()
            print(lines)
            return is_target(lines)
        else:
            all_targets(path+'/'+file)  #Go into a subdirectory

























    #
