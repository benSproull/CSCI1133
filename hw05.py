import math
#val = [3, 5, 18, 66, 188]
def closest(val):
    '''
    Purpose:
        to find the 2 closest number in a string
    Parameters:
        b = opan string
        closest = keeps track of the value
    Return:
        returns the differece between the 2 closest numbers
    '''
    i = 1
    closest = val[0]
    b = []
    s_sum = 0

    for i in range(len(val)):
        closest = (val[i - 1] - val[i])
        z = math.fabs(closest)
        b.append(z)
    s_sum = min(b)

    return s_sum
scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
def change_key(notes, up):
    '''
    Purpose:
        Take the 12 cords and move then up when they shift keys
    Parameters:
        new_scale = an open string to write the new chords on
    Return:
        returns the new chords after being moved up
    '''
    i = 0
    new_scale = []
    a = []
    x = 0
    #         0    1     2    3    4     5    6     7    8    9     10   11
    #scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    for i in range(len(notes) - up):
        v = scale[(i + up)]
        new_scale.append(v)

    a = notes[len(notes) - up:len(notes)]
    new_scale.append(a)
    return new_scale



#names = ['Jessica Thorne', 'Manan Mrig', 'Elijha Gordon', 'Daniel Binsfeld', 'Abdullahi Abdullahi', 'Chris Park', 'Nathan Stearley', 'Aishwarya Belhe']
def avoid_sz(names_list):
    '''
    Purpose:
        To help the vice princle not say names with with an 's' or a 'z'
    Parameters:
        o = odd number names strings
        e = even number strings
        names = new string being made
    Reutrn:
        returns list of names in the order where the VP doesn't have to say names with s and z
    '''
    o = []
    e = []
    names = []
    x = len(names_list) // 2

    if len(names_list) % 2 == 1:
        x = x + 1
    for i in names_list:
        if 's' in i or 'z' in i:
            o.append(i)
        else:
            e.append(i)
    if len(e) < names:
        print('Impossible')
        return []
    else:
        for x in range(len(o)):
            names.append(e[i])
            names.append(o[i])
        if len(e) > len(o):
            for x in range(len(o),len(e)):
                names.append(e[i])
    return names
