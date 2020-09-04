def no_dups(s):
    thingy = {};
    a = '';

    if len(s.split()) <= 0:
        return "";

    for i in s.lower().split(' '):
        if i not in thingy:
            thingy[i] = i;
            if len(a) <= 0:
                a += i;
            else:
                a += ' ' + i;

    return a;

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))