def no_dups(s):
    # Your code here
    words = s.split()
    no_dups_set=[]
    if len(words) < 1:
        return ""
    for word in words:
        if word in no_dups_set:
            pass
        else:
            no_dups_set.append(word)
    string = ""
    for word in no_dups_set:
        string += word + " "
    return string.strip()



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))