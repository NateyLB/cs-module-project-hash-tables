import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

words = words.split()

# TODO: analyze which words can follow other words
# Your code here
markov_dict = {}
for index,word in enumerate(words):
    if index == len(words)-1:
        break
    elif word not in markov_dict:
        markov_dict[word] = []
    markov_dict[word].append(words[index+1])
# TODO: construct 5 random sentences
# Your code here

def generate_sentence():
    random_word = random.choice(list(markov_dict))
    sentence = random_word
    value=random_word
    while (value[-1]!= "." and value[-1]!= "?" and value[-1]!= "!"):
        if len(value) >1:
            if ((value[-2]== "." or value[-2]== "?" or value[-2]== "!") and value[-1]== "\""):
                break
        new_value = markov_dict.get(value)
        if len(new_value) > 1:
            new_value = random.choice(new_value)
            sentence += " " + new_value
            value= new_value
        else:
            new_value = new_value[0]
            sentence += " " + new_value
            value= new_value
    return sentence

print(generate_sentence())
print("")
print(generate_sentence())
print("")
print(generate_sentence())
print("")
print(generate_sentence())
print("")
print(generate_sentence())