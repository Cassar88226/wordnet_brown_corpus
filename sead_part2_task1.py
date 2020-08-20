# Part-2: (Python program)

# Displays all the senses and their definitions corresponding to the keyword as a noun as they appear in WordNet. 
# If the keyword does not appear in WordNet as noun, the program displays a message and does not go to the next step.

import nltk
from nltk.corpus import wordnet as wn
import sys
# get keyword
keyword = input("Enter a word: ")
# get Noun synsets from wordnet 
keyword_synsets = wn.synsets(keyword, pos=wn.NOUN)

# check if keyword does not appear in WordNet as noun
if not keyword_synsets:
    print("keyword :", keyword, " is not a Noun")
    sys.exit()

# display Sense list
senses_list = []
for i, syn in enumerate(keyword_synsets):
    senses_list.append(syn)
    print("Sense " + str(i+1) + ' is ' + syn.definition())

# • If the keyword has at least one sense as noun in WordNet, 
# checks whether it appears as a noun in the Brown corpus. 
# If the word is used as a noun, the program asks the users to enter a number which indicates which sense they want to select. 
# Ensure you deal with unexpected and erroneous input.

# checks whether it appears as a noun in the Brown corpus.
from nltk.corpus import brown
brown_keyword_tokens = [(word, pos) for word, pos in brown.tagged_words() if word == keyword and pos.startswith('NN')]
# If the word is used as a noun
sense_index = 0
if len(brown_keyword_tokens):
    # the program asks the users to enter a number which indicates which sense they want to select. 
    sense_index = input("Select a sense: ")
    # Ensure you deal with unexpected and erroneous input.
    try:
        sense_index = int(sense_index)
        if sense_index < 1 or sense_index > len(senses_list):
            print("Please input the valid sense number")
            sys.exit()
    except ValueError as e:
        print("Please input the correct sense number as a integer")
        sys.exit()
else:
    print("Keyword :", keyword, " doesn't appear as a noun in the Brown Corpus")
    sys.exit()

# •	Displays the frequency of the keyword in the Brown corpus and of all the synonyms of the keyword for the selected sense. 
# In all the cases, only the occurrences as nouns should be counted. 
# For this step ignore the synonyms that are multi-word expressions.

# get all synonyms of the keyword for selected sense 
print("The frequencies of the keyword and it synonyms for sense {}".format(sense_index))
selected_sense = senses_list[sense_index - 1]
for lemma in selected_sense.lemmas():
    # only the occurrences as nouns should be counted
    # For this step ignore the synonyms that are multi-word expressions.
    if '_' not in lemma.name():
        freqs = nltk.FreqDist(w.lower() for w, pos in brown.tagged_words() if w == lemma.name() and pos.startswith('NN'))
        print(lemma.name(), ":", freqs.N())

# •	Discuss why counting the frequency of the multi-word expressions 
# which are synonyms with the keyword is difficult in Brown corpus using the code you wrote

# why it is difficult

# if we want to count the frequency of the multi-word expressions,
# first, we should tokenize all the text of brown corpus
# next, find the matched multi-words expressions according to words ordering
# last, calculate the frequency of them

# my solution 1

# we can use n-grams method for multi-words expressions
# if phrase has two words, we can use bi-gram, for three words, tri-gram, so on.

# my solution 2
# we can use MWETokenizer in nltk.tokenize package
# A MWETokenizer takes a string which has already been divided into tokens and retokenizes it, merging multi-word expressions into single tokens, using a lexicon of MWEs







