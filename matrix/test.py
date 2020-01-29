"""def makeInverseIndex(strlist):

    
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    
    # create an empty dictionary
    dictionary = {}

    # we iterate through the documents comprising the strList
    for i in range(0,len(strlist)):

        # for a given iterate i, we create a list of lists where each list is a word
        str2list = strlist[i].split()

        # we iterate over the words in the newly created list 
        for word in str2list:

            # we check whether the word is already in the dictionary or not
            if not word in dictionary:
                set_memb = {i}

                # we iterate over all the strings that are remaining in the strList
                for j in range(i+1,len(strlist)):

                    # if the word exists in a document then add it to the set membership
                    if not strlist[j].find(word,0,len(strlist[j])) == -1:
                        set_memb.add(j)

                # once the set is fully built we add it to the dictionary
                dictionary[word] = set_memb

    # return the dictionary
    return dictionary"""

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
