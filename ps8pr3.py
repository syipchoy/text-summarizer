#stephany yipchpy
#working alone not even by choice this time i jsut dont trust others lol
#rip

import random

#task 1
def create_dictionary(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()
    
    d = {}
    current_word = '$'
    
    for next_word in words:

        if current_word[-1] in '.?!':
            current_word = '$'
        if current_word not in d:
            d[current_word] = [next_word]
            current_word = next_word
        else:
            d[current_word] += [next_word]
            current_word = next_word
     
    return d

#task 2    
def generate_text(word_dict, num_words):
    """uses word_dict to generate and print a string of num_words"""
    current_word = '$'

    for x in range(num_words):
        next_word = random.choice(word_dict[current_word])
        print(next_word, end = ' ')
        if next_word not in word_dict:
            current_word = '$'
        else:
            current_word = next_word
    print () 
