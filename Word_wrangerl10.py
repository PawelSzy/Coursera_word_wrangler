"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    new_list = []
    for elem in list1:
        if new_list == []:
            new_list.append(elem)
            continue
        if elem == new_list[-1]:
            continue
        else:
            new_list.append(elem)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    
    new_list = []
#    for elem in list1:
#        if elem in list2:
#          new_list.append(elem)  
    
    pointer1 = 0
    pointer2 = 0
       
    if type(list1)== int or type(list2) == int:
        len_list1 = 1
        len_list2 = 1
    elif type(list1)== float or type(list2) == float:
        len_list1 = 1
        len_list2 = 1
    else:
        len_list1 = len(list1)
        len_list2 = len(list2)

    while pointer1 <len_list1 and pointer2 < len_list2:
        if list1[pointer1] == list2[pointer2]:
            new_list.append(list1[pointer1])
            pointer1+=1
            pointer2+=1
            continue
        if list1[pointer1] < list2[pointer2]:
            pointer1+=1
            continue
        if list1[pointer1] > list2[pointer2]:    
            pointer2+=1
            continue
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    pointer1 = 0
    pointer2 = 0
    
    if type(list1)== int or type(list2) == int:
        len_list1 = 1
        len_list2 = 1
    elif type(list1)== float or type(list2) == float:
        len_list1 = 1
        len_list2 = 1
    else:
        len_list1 = len(list1)
        len_list2 = len(list2)
    
    new_list = []
    
    while True:
        if pointer1 >= len_list1:
            if pointer2 >= len_list2:
                break
            else:
                new_list += list2[pointer2:]
                break
                
        if pointer2 >= len_list2:
            new_list += list1[pointer1:]
            break           
        if list1[pointer1] == list2[pointer2]:
           new_list.append(list1[pointer1])
           new_list.append(list2[pointer2])
           pointer1+=1
           pointer2+=1
           continue
        if list1[pointer1] < list2[pointer2]:
            new_list.append(list1[pointer1])
            pointer1+=1
            continue
        if list1[pointer1] > list2[pointer2]: 
            new_list.append(list2[pointer2])
            pointer2+=1
            continue       
    return new_list
    

                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    
    list_len = len(list1)
    
    if list_len == 0 or list_len == 1:
        return list1
    
    if list_len == 2:
        
        if list1[0] > list1[1]:
            return list1[1] + list1[0]
        else:
            return list1
    
    
    half_list =  list_len/2
    
    first_list = list1[0:half_list]
    second_list = list1[half_list:]

    
    first_list = merge_sort(first_list)
    second_list = merge_sort(second_list)
    
    
    return merge(first_list, second_list)
                            
def generate_string(word, letter):
    """
    generator of string from word
    """
    

    
    for position in range(len(word)+1):
        word2 = word[:position]+ letter + word[position:]
        yield word2
# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return_string =[]
    
    if word == [] or word == '':
        return ""
    
    first = word[0]
    rest =  word[1:]
    
    rest_strings = gen_all_strings(rest)
    rest_strings = remove_duplicates(rest_strings)
    
    
    return_string.append(first)
    return_string.append(rest)
    
    for string in rest_strings:
        return_string.append(string)
        for string2 in generate_string(string, first):
            return_string.append(string2)
 
    return remove_duplicates(return_string)

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)

    word_list = []
    for line in netfile.readlines():
        word_list.append(line[:-1])
    
    return word_list

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

    
def test_word():
    lista = ["adam", "bathory", "Lucyfer", "Lucyfer", "X", "Zombie"]
    lista2 = ["adam", "bathory", "Lucyfer", "X","X", "Y", "Zeus", "Zombie"]
    
    lista3 = ["Adam", "Perun", "Bathory", "Vampir","Lucyfer", "Lucyfer", "X", "Strzyga", "Zombie"]
    print remove_duplicates(lista)
    print intersect([7, 10, 15], [10])
    
    print merge(lista, lista2)
    
    print "----------"
    
    #lista3.sort()
    print"merge_sort"
    #lista3 = ["Adam", "Perun", "Bathory", "Vampir"]
    print "lista3"
    print lista3
    print "merge\n", merge_sort(lista3)
    print "----------"
    
    #print load_words(WORDFILE)
    
    gen_strings = gen_all_strings("aab")
    print "gen_strings ", gen_strings
    print remove_duplicates(gen_strings)
    
    print load_words(WORDFILE)
        
test_word()    
# Uncomment when you are ready to try the game
#run()

    
    
