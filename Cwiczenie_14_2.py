# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:24:00 2017

@author: e543865
"""

from anagram_sets import all_anagrams, signature 
import shelve


    
def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.

    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')
    
    for key, value in anagram_map.items():
        shelf[key] = value

    shelf.close()


def read_anagrams(filename, word):
    '''Searches for a value for given key in a shelve
    
    filename: string file name of shelf
    word: word to look up
    '''
    
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []
        
    

def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))
    
#store_anagrams('anagrams.db', all_anagrams('words.txt'))
print(read_anagrams('anagrams.db', 'reset'))