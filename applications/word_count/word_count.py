def word_count(s):
    
    thingy = {};

    #: ; , . - + = / \ | [ ] { } ( ) * ^ &

    if len(s.strip()) <= 0:
        return thingy;

    s = s.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ');

    for i in s.lower().split(' '):
        mod = i.replace('"', '').replace(',', '').replace('.', '').replace(':', '').replace(';', '');
        mod = mod.replace('-', '').replace('+', '').replace('=', '').replace('/', '');
        mod = mod.replace('\\', '').replace('(', '').replace(')', '').replace('[', '');
        mod = mod.replace(']', '').replace('|', '').replace('{', '').replace('}', '');
        mod = mod.replace('*', '').replace('^', '').replace('&', '');
        # mod = mod.replace('\r', ' ').replace('\t', ' ').replace('\n', ' ');
        if mod == ' ' or mod == '':
            continue;
        if mod in thingy:
            thingy[mod] = thingy[mod] + 1;
        else:
            thingy[mod] = 1;

    print(thingy);

    return thingy;

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))