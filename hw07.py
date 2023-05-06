# Problem A
'''
Purpose: take a sequence of dna and look for pairs of c and g to make 'cg'

Parameter(s): cg_pair is the number of 'cg' pairs found in the sequence
              cg_ratio is the ratio of 'cg' pairs to non 'cg' pairs
Return Value: returns the ratio of 'cg' pairs to non 'cg' pairs and the list of pairs found
'''
def cg_pairs(dna):
    i = 0
    cg_pair = 0
    pairs_list = []
    #dna.lower()
    for i in range(len(dna) - 1):
        if dna[i] != 'c' and dna[i] != 'g' and dna[i] != 'a' and dna[i] != 't' and dna[i] != 'C' and dna[i] != 'G' and dna[i] != 'A' and dna[i] != 'T':
            print('Error in DNA strand')
            return 0.0
        pair = dna[i] + dna[i + 1]
        pairs_list.append(pair)
    print(pairs_list)
    for z in range(len(pairs_list)):

        if pairs_list[z] == 'cg' or pairs_list[z] == 'Cg' or pairs_list[z] == 'cG' or pairs_list[z] == 'CG':
            cg_pair += 1
    cg_ratio = cg_pair / (len(pairs_list))
    return cg_ratio

# Problem B
'''
Purpose: to take a sequence of dna and split it up in 1 of 3 different ways

Parameter(s): dna_str is the sequence of string that is taken in and frame is choosing 1 of 3 different ways to split the string up

Return Value: returns a sliced string sliced the desired way the user inputted
'''
def segment(dna_str, frame):

    if frame == 0:
        str0 = []
        i = 0
        while i <= (len(dna_str)):
            a = dna_str[i:i + 3]
            str0.append(a)
            i += 3

        return str0

    if frame == 1:
        str1 = []

        i = 1
        first = dna_str[0]
        str1.append(first)
        while i < (len(dna_str)):
            a = dna_str[i:i + 3]
            str1.append(a)
            i += 3

        return str1

    if frame == 2:
        str2 = []
        i = 2
        first = dna_str[0] + dna_str[1]
        str2.append(first)
        while i < (len(dna_str)):
            a = dna_str[i:i + 3]
            str2.append(a)
            i += 3

        return str2

# Problem C
'''
Purpose: Finds a desired sequence in a longer sequence of dna

Parameter(s): DNA = a sequence of dna and search = whatever the user wants to find in the sequence of dna

Return Value: returns the dna sequence but with arrows pointing out the desired sequence the user wanted to find
'''
def mark_dna(DNA, search):
    Fstr = []
    L = (len(search))
    for i in range(len(DNA)):
        if DNA[i:L + i] == search:
            Fstr = DNA[0:i] + '>>' + search + '<<' + DNA[i + L::]
    return Fstr

# Problem D
'''
Purpose: To take a pages source code and pick out the URL within the code

Parameter(s): html = the pages source code entered in by the user to quickly find the URL

Return Value: returns only the URL from the page source code
'''
def find_url(html):
    url_str = []
    final_str = []
    url = html.find('href="')
    #print(url)
    url_str = html[url + 6:]
    end_num = url_str.find('"')
    final_str = html[url + 6:url + end_num + 6]
    #print(end_num)
    return final_str


























    #
