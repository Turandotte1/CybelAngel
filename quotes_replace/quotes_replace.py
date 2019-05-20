#!/usr/bin/python3

##      Tech case for Cybel Angel
##
##      Write a Python 3 function that takes a string, replaces each '
##      by \' and each \ by \\, and returns the result.
##      Use only the language features and standard library.
##
##      Author: Mariya Rychkova

import sys
import re

def quotes_replace(s1):
    '''
        Initializes  dictionary in order to map each old pattern to its
        rempalcement pattern.
    '''
    replacements = { r"'" : r"\'"
                     r"\\" : r"\\\\",
                   }

    '''
        Makes a substitution using each key-value pair
    '''
    for key, value in replacements.items():
        s1 = re.sub(key, value, s1)
    return (s1)

## Small main test : python3 quote_replacing.py s1
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('String without remplacement : '+str(sys.argv[1]))
        print('String with remplacement : '+quotes_replace(str(sys.argv[1])))
    else:
        print ('Not enough arguments. Please enter at least 2 strings')
