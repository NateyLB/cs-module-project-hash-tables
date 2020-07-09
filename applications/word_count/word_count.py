import re
def word_count(s):
    # Your code here
    counts={}
    words = s.split()
    for index, word in enumerate(words):
        only_alpha = ""
        for char in word:
            if ord(char.lower()) >= 97 and ord(char.lower()) <= 122 or ord(char) == 39:
                only_alpha += char.lower()
        words[index] = only_alpha
    if len(words) > 0:
        if words[0] == '':
            return counts
    def getCount(words):
        if len(words) == 0:
            return
        elif words[0] in counts:
            counts[words[0]] += 1
            return getCount(words[1:])
        else:
            counts[words[0]] = 1
            return getCount(words[1:])
    getCount(words)
    print(counts,"counts")
    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))