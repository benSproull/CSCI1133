import math

#TODO: Fill out the Purpose, Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

# Example functions for background reading

def nickels_to_cents(nickels):
    '''
    Purpose:
        Converts from a given number of nickels to
        the number of cents they represent
    Parameter(s):
        nickels: The number of nickels we have
    Return Value:
        The amount in cents we have
    '''
    total = nickels * 5
    return total

def degrees_to_radians(deg):
    '''
    Purpose:
        Converts from degrees to radians
    Parameter(s):
        deg: The number of degrees in a given angle
    Return Value:
        The given angle's measure in radians
    '''
    radians = deg * math.pi / 180
    return radians




# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Covert degrees in celsius to degrees in fahrenheit
    Parameter(s):
        celsius: The temperature in degrees celsius
    Return Value:
        The temperature in degrees fahrenheit
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def print_25_stars():
    '''
    Purpose:
        Print out 25 stars onto the screen
    Parameter(s):
        No parameters, no input needed to run program
    Return Value:
        Prints out 25 stars onto the screen in 5 rows of 5
    '''
    print('*****')
    print('*****')
    print('*****')
    print('*****')
    print('*****')


# Part B: Write out a few simple conversions

def area_circle(radius):
    import math
    '''
    Purpose:
        Find the area of a circle
    Parameters:
        radius: The total radius of the circle
    Return Value:
        The total area of the circle
    '''
    area = math.pi * radius**2
    return area

    print("TODO: Document and write this function")

def meters_to_feet(meters):
    '''
    Purpose:
        To convert meters into feet
    Parameters:
        meters: input how many meters something is
    Return Value:
        How many feet the amount of meters the user inputed is
    '''
    feet = meters * 3.28084
    return feet

    print("TODO: Document and write this function")

def minutes_to_days(minutes):
    '''
    Purpose:
        To convert minutes into days
    Parameters:
        minutes: input how many minutes
    Return Value:
        How many days the amount of minutes that was inputed
    '''
    days = minutes / 1440
    return days

    print("TODO: Document and write this function")

# Part C: Simulate changes in fish population over three weeks

def population(small, middle, big):
    '''
    Purpose:
        To simulate how 3 different groups of fish will do in a lake over the span of 3 weeks
    Parameters:
        es: the amount of small fish that were eaten by middle fish
        ms: the amount of middle fish that were eaten by middle fish
        total_fish: returns the total amount of fish after 3 weeks
    Return Value:
        How many feet the amount of meters the user inputed is
    '''
    small = small * 1.1
    middle = middle * 0.95
    big = big * 0.9

    es = 0.0001 * small * middle
    small = small - es
    middle = middle + es*2

    em = 0.0002 * middle * big
    middle = middle - em
    big = big + em

    small1 = small
    middle1 = middle
    big1 = big

    print('Week 1 = Small fish: ',round(small1,0),'   Middle fish:',round(middle1,0),'   Big fish:',round(big1,0))

    small = small * 1.1
    middle = middle * 0.95
    big = big * 0.9

    es = 0.0001 * small * middle
    small = small - es
    middle = middle + es*2

    em = 0.0002 * middle * big
    middle = middle - em
    big = big + em

    small2 = small
    middle2 = middle
    big2 = big

    print('Week 2 = Small fish: ',round(small2,0),'   Middle fish:',round(middle2,0),'   Big fish:',round(big2,0))

    small = small * 1.1
    middle = middle * 0.95
    big = big * 0.9

    es = 0.0001 * small * middle
    small = small - es
    middle = middle + es*2

    em = 0.0002 * middle * big
    middle = middle - em
    big = big + em

    small3 = small
    middle3 = middle
    big3 = big

    print('Week 3 = Small fish: ',round(small3,0),'   Middle fish:',round(middle3,0),'   Big fish:',round(big3,0))
    total_fish = small3 + middle3 + big3
    return round(total_fish,0)
    
