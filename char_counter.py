import re

def vowel_count(sentence):
    dictionary = {}
    lowerletters = sentence.lower()
    vowels = re.findall('[aeiou]', lowerletters)
    for i in vowels:
        dictionary[i] = dictionary.get(i,0) + 1
    print(dictionary)
vowel_count("Mary learns programming.")

def vowel_count2(sentence):
    dictionary = {}
    vowels = 'aeiou'
    for i in sentence:
        lowercase = i.lower()
        if lowercase in vowels:
            dictionary[lowercase] = dictionary.get(lowercase,0) + 1
    print(dictionary)
vowel_count2("Mary learns programming.")