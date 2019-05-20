#!/usr/bin/python3

##      Tech case for Cybel Angel
##
##      Write a Python 3 function that takes 2 strings as arguments, and returns
##      true if they are anagrams of each other, and false otherwise.
##      Use only the language features and standard library.
##
##      Author: Mariya Rychkova

import sys

def is_anagram(s1, s2):

    '''
        Trims whitespaces and spaces between the words.
        Then, forces a string to lowercase format.
    '''
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    '''
        Checks if the strings have the same size, as otherwise they
        cannot be anagrams.
    '''
    if len(s1) != len(s2):
        return False

    '''
        Initializes dict hash table.
        Iterates over each string.
    '''
    hashtable = dict()
    for i in s1:
        '''
            For each new occurence of letter in the string, it increments
            it by one in a hashtable, if new letter it initializes it at 1
        '''
        if i in hashtable:
            hashtable[i] += 1
        else:
            hashtable[i] = 1

    for i in s2:
        '''
            For each new occurence of letter in the string, it decrements
            it by one in a hashtable, if new letter it initializes it at 1
        '''
        if i in hashtable:
            hashtable[i] -= 1
        else:
            hashtable[i] = 1

    '''
        If hashtable is empty, then each letter has the exact same number of
        occurences in each string, so they are anagrams.
    '''
    for i in hashtable:
        if hashtable[i] != 0:
            return False
    return True

## Small main test : python3 is_anagram.py s1 s2
if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(is_anagram(str(sys.argv[1]), str(sys.argv[2])))
    else:
        print ('Please make sure you have entered at least 2 strings')
