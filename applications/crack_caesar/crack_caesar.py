# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
import re
# Your code here
# | Letter | Percentage |
# |:------:|-----------:|
# |   E    |    11.53   |
# |   T    |     9.75   |
# |   A    |     8.46   |
# |   O    |     8.08   |
# |   H    |     7.71   |
# |   N    |     6.73   |
# |   R    |     6.29   |
# |   I    |     5.84   |
# |   S    |     5.56   |
# |   D    |     4.74   |
# |   L    |     3.92   |
# |   W    |     3.08   |
# |   U    |     2.59   |
# |   G    |     2.48   |
# |   F    |     2.42   |
# |   B    |     2.19   |
# |   M    |     2.18   |
# |   Y    |     2.02   |
# |   C    |     1.58   |
# |   P    |     1.08   |
# |   K    |     0.84   |
# |   V    |     0.59   |
# |   Q    |     0.17   |
# |   J    |     0.07   |
# |   X    |     0.07   |
# |   Z    |     0.03   |
frequency= {
    11.52: "E",
    9.75: "T",
    8.46: "A",
    8.08: "O",
    7.70: "H",
    6.73: "N",
    6.29: "R",
    5.84: "I",
    5.56: "S",
    4.74: "D",
    3.92: "L",
    3.07: "W",
    2.59: "U",
    2.48: "G",
    2.42: "F",
    2.19: "B",
    2.18: "M",
    2.02: "Y",
    1.58: "C",
    1.08: "P",
    0.84: "K",
    0.59: "V",
    0.17: "Q",
    0.07: "J",
    0.03: "Z"
}
with open("applications/crack_caesar/ciphertext.txt") as f:
    text = f.read()
words = text.split()
chars=[]
for char in text:
    if char ==" " or char =="!" or char =="," or char =="." or char =="\""or char == "\n" or char == "\'" or char == ";" or char == "—" or char == "?" or char == ":" or char == "(" or char == ")" or char == "1" :
        pass
    else:
        chars.append(char)

cipher_freq ={}
for char in chars:
    if char not in cipher_freq:
        cipher_freq[char] = 0
    cipher_freq[char] += 1

for key in cipher_freq:
    cipher_freq[key] = (cipher_freq[key]/len(chars)) * 100
    cipher_freq[key] = float(format(cipher_freq[key], '.2f'))
cipher={}
for key, value in cipher_freq.items():
    cipher[key] = frequency.get(value)
for index,word in enumerate(words):
    new_word = ''
    for char in word:
        decoded_char = cipher.get(char)
        if decoded_char is None:
            new_word += char
        else:
            new_word += decoded_char
    words[index] = new_word

decoded_sentence = ""
for word in words:
    decoded_sentence += word + " "
print(decoded_sentence)

