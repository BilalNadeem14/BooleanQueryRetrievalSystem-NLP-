# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:41:20 2020

@author: BILAL khan
"""
"""
IMPORTANT NOTE:
    I did sorting after lemmitization and stemming
    So whenever I get a query, first apply lemmitization and stemming AND THEN SORTING(NEVER VICE VERSA):
        Phir querry AUR inverted index ki sorting same type ki hogi:
            find out its benefits???

"""

import functools
from functools import reduce
import nltk
nltk.download('punkt')

import glob
list_of_text_files_names = glob.glob("G:/bbcsport-fulltext/bbcsport/cricket/*.txt")
#print(list_of_text_files_names)

documents = []
for filename in list_of_text_files_names:
    with open(filename,"r") as file:
            documents.append(file.read())    
print("no. of doucments", len(documents))
print("length of document 1", len(documents[0]))

wordsList = []
for d in documents: #documents is a list containing all documents: one by one each document will be saved in variable d in each iteration
    for w in nltk.word_tokenize(d):
        wordsList.append(w)
        """Remove punctuation marks from wordslist"""
print("length words list", len(wordsList))
#print(wordsList)

uniqueWords = list(set(wordsList))
print("unique words", len(uniqueWords))

"""
we will apply 

steming: 2 types prefix and suffix:       Yeh kuch rules k through suffix ya prefix cut kardeta hai:
    For this purpose we should know computational linguistics of that language, should know grammar and should know how words are formed

lemmatizer: goes, went: go       Yeh mapping karta hai through key,value pairs
stop words removal: is, am, are jesay words remove karaingay
"""

from nltk.corpus import stopwords
#nltk.download('stopwords')

for word in uniqueWords:
    if word in stopwords.words():
        uniqueWords.remove(word)

print("unique words", len(uniqueWords))

"""Pehle lematization karo phir Stemming karo"""

"""wordNet  aik word ka different words k sath kya relation hai, isska pura graph hai"""

#nltk.download('wordnet')


from nltk.stem import WordNetLemmatizer
WordNetLemmatizer = WordNetLemmatizer() #word kay root words store karta hai
lemmatizedWordList = []
for word in uniqueWords:
    lemmatizedWordList.append(WordNetLemmatizer.lemmatize(word))
print("length of lemmatized word list", len(lemmatizedWordList))

#print(WordNetLemmatizer.lemmatize('goes'))
lemmatizedWordList = list(set(lemmatizedWordList))
print("after removing duplicates in lematized word list\n", len(lemmatizedWordList))


"""
FOUND SOLUTION:
    THERE ARE DUPLICATES TABHI LIST KA SIZE CHOTA NAE HORAHA, JUST PASS IT THROUGH A SET FUNC
"""

from nltk.stem import PorterStemmer
porter = PorterStemmer()
StemmedWordsList = []
for word in lemmatizedWordList:
    StemmedWordsList.append(porter.stem(word))
    
print("length of stemmed word list", len(StemmedWordsList))
StemmedWordsList = list(set(StemmedWordsList))
print("after removing duplicates in Stemmed words list\n", len(StemmedWordsList))
"""issko dict mein store karna hai aur indexing karni hai"""

#print(StemmedWordsList)
StemmedWordsList.sort()
#print(StemmedWordsList)

def searching_term_from_document(term):

    freq = 0
    document_number = 0
    documents_containing_term = []
    for document in documents:
        if term in document:
            freq += 1
            documents_containing_term.append(document_number)
        document_number +=1
    return (freq, documents_containing_term)



for word in StemmedWordsList:
    if word in stopwords.words():
        StemmedWordsList.remove(word)

#print(StemmedWordsList[0:10])
print("length of stemmed word list", len(StemmedWordsList))

inverted_index_list = []    
for i in range(len(StemmedWordsList)):
    tuplee = searching_term_from_document(StemmedWordsList[i])
    freq, no_of_doc_list = tuplee
    freq_and_documents = [freq, no_of_doc_list]    
    #print(freq_and_documents)
    term = StemmedWordsList[i]
    inverted_index = {
        term : freq_and_documents
     }
    #print(inverted_index)
    inverted_index_list.append(inverted_index)

print(len(inverted_index_list))
print(inverted_index_list[:5])
