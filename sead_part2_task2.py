# Part-2: (Python program)

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
# input keyword
keyword = input("Enter a word: ")
# input number
number = input("Enter a number: ")
# convert number string to integer number
try:
    number = int(number)
    if number < 1:
        number = 1
except ValueError e:
    number = 1
# get tagged words from brown corpus
brown_tagged = brown.tagged_words()
# get bigrams from brown corpus
word_tag_pairs = list(nltk.bigrams(brown_tagged))

# find words with specific POS tag before another specific POS tag
def find_before_words(before_pos, after_pos, keyword,reverse=False):
    before_list = None
    # reverse means whether the word is before or after
    # if reverse is False, find before word with before_pos POS tagg which appears before after_pos POS tag with keyword
    # for instance, if you want adjective word before noun word 'shool', before_pos starts with 'JJ', after_pos starts with 'NN'
    # and find prior word(in below code, a)
    # if reverse is True, find next word (in below code, b)
    if reverse:
        before_list = [b[0] for (a, b) in word_tag_pairs if a[1].startswith(before_pos) and b[1].startswith(after_pos) and a[0]==keyword]
    else:
        before_list = [a[0] for (a, b) in word_tag_pairs if a[1].startswith(before_pos) and b[1].startswith(after_pos) and b[0]==keyword]
    before_list = list(set(before_list))
    return before_list

# calculate frequence of founded word
# this logic is like above
def calc_bigram_frequency(before_pos, after_pos, keyword, before_list, reverse=False):
    freq_list = []
    for before in before_list:
        dist = None
        if reverse:
            dist = nltk.FreqDist(b[0] for (a, b) in word_tag_pairs if a[1].startswith(before_pos) and b[1].startswith(after_pos) and a[0]==keyword and b[0] == before)
        else:
            dist = nltk.FreqDist(a[0] for (a, b) in word_tag_pairs if a[1].startswith(before_pos) and b[1].startswith(after_pos) and b[0]==keyword and a[0] == before)
        freq_list.append((dist.N(), before))
    return freq_list

def find_most_before_words(before_pos, after_pos, keyword, number, reverse=False):
    # find words with specific POS tag before another specific POS tag
    words_list = find_before_words(before_pos, after_pos, keyword, reverse)
    # calculate frequence of founded word
    freq_list = calc_bigram_frequency(before_pos, after_pos, keyword, words_list, reverse)

    # get valid length
    max_len = min(len(freq_list), number)

    # sort by frequency
    freq_list = sorted(freq_list, key=lambda x: x[0], reverse=True)[0:max_len]
    return freq_list
# (a) asks the user to enter a word and identifies all its occurrences in the Brown corpus 
# where it is used as a noun. Display how many times the word appears as a noun in the Brown corpus.

freqs = nltk.FreqDist(w.lower() for w, pos in brown.tagged_words() if w == keyword and pos.startswith('NN'))
print("Frequency of ", keyword ," : ", freqs.N())

# (b) & (d) finds which adjective appears the most often immediately before the given noun. Display the frequency of this adjective. 
most_adjective_list = find_most_before_words('JJ', 'NN', keyword, number)
print("Adjectives that appear before ", most_adjective_list)

# (c) Using similar processing, take this adjective and find which noun appears most frequently after this adjective in the Brown corpus. 
for (freq, adjective) in most_adjective_list:
    most_noun_list = find_most_before_words('JJ', 'NN', adjective, 1, True)
    if most_noun_list:
        print('The most frequent noun that follows the adjective '+ adjective + ' is ' + most_noun_list[0][1] + ' frequency: ' + str(most_noun_list[0][0]))
    









