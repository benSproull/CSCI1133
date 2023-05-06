# Problem A
def sound(weight):



    if weight < 13:
        type = "Yip"
    elif weight > 13 and weight <= 30:
        type = 'Ruff'
    elif weight > 31 and weight <= 70:
        type = 'Bark'
    elif weight > 70:
        type = 'Boof'
    else:
        print("no")
    return type

# Problem B
def sound2(weight, is_cat):
    if is_cat == True:
        return 'Meow'

    elif is_cat == False:

        w = sound(weight)
        return w
# Problem C
def selection(text, optionA, optionB, optionC):


    print(text)
    print('A.) ',optionA)
    print('B.) ',optionB)
    print('C.) ',optionC)

    txt = (input('Choose A, B, or C: '))
    if txt == 'A':
        return 'A'
    elif txt == 'B':
        return 'B'
    elif txt == 'C':
        return 'C'
    else:
        print('Invalid option, defaulting to A')
        return 'A'

def adventure():


    print('Welcome to the maze')

    text1 = 'Someone is chasing you'
    op1_1 = 'go left'        #A
    op1_2 = 'go right'       #B
    op1_3 = 'go straight'    #C

    text2 = 'you are still being chased'
    op2_1 = 'go left'
    op2_2 = 'go right'
    op2_3 = 'go straight'

    text3 = 'you are still being chased'
    op3_1 = 'go left'
    op3_2 = 'go right'
    op3_3 = 'go straight'

    run = selection(text1, op1_1, op1_2, op1_3)
    print(run)
    if 'A':
        print(text1)
        print('A. ', op1_1)
        print('B. ', op1_2)
        print('C. ', op1_3)
        if 'A':
            print(text2)
            print('A. ', op2_1)
            print('B. ', op2_2)
            print('C. ', op2_3)
            if 'A':
                print('You have made it out of the maze!!')
            if 'B':
                print('You have been caught and killed')
            if 'C':
                print('You have been caught and killed')
        if 'B':
            print('You have been caught and killed')
        if 'C':
            print('You have made it out of the maze!!')
    if 'B':
        print(text1)
        print('A. ', op1_1)
        print('B. ', op1_2)
        print('C. ', op1_3)
        if 'A':
            print('You have made it out of the maze!!')
        if 'C':
            print('You have made it out of the maze!!')
        if 'B':
            print(text2)
            print('A. ', op2_1)
            print('B. ', op2_2)
            print('C. ', op2_3)
            if 'A':
                print('You have made it out of the maze!!')
            if 'B':
                print('You have been caught and killed')
            if 'C':
                print('You have been caught and killed')
    if 'C':
        print('You have been caught and killed')
