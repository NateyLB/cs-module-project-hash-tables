# Your code here
with open("applications/histo/robin.txt") as f:
    words = f.read()

words = words.split()
# stripping symbols and normalizing to all lowercase
for index, word in enumerate(words):
    only_alpha = ""
    for char in word:
        if ord(char.lower()) >= 97 and ord(char.lower()) <= 122 or ord(char) == 39:
            only_alpha += char.lower()
        words[index] = only_alpha

count={}
# build histogram
for word in words:
    if word not in count:
        count[word] = ""
    count[word] += "#"
# get order of sorted keys
sorted_keys = sorted(count, key=lambda i: len(count[i]), reverse=True)
# print histogram by sorted keys/ in order
for key in sorted_keys:
    print(count.get(key), key)