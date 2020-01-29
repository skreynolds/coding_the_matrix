from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    # create an empty dictionary
    res_dict = {}
    # create a dictionary that give an ordered integer value to each book and
    # splits the book string into a list of strings
    my_dict = {i:v.split() for i,v in enumerate(strlist)}

    # iterate over each book in the dictionary
    for i in my_dict:
        # for a given book in the dictionary iterate over each word
        for word in my_dict[i]:
            # for a given word in a given book check to see if the word is
            # listed already
            if not word in res_dict:
                set_memb = {i}
                # if the word is not listed already then iterate over the
                #remaining books to see if the word is in them
                for j in range(i+1,len(my_dict)):
                    # if the word is in a book then add that book to the set
                    if my_dict[j].count(word) != 0:
                        set_memb.add(j)
                # for the given word add it to the dictionary with the created
                # set holding the book numbers that it appears in
                res_dict[word] = set_memb
    return res_dict
            

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    s = set()
    for word in query:
        if word in inverseIndex:
            s.update(inverseIndex[word])
    return s

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    
    return set.intersection(*[inverseIndex[word] for word in query if word in inverseIndex])
