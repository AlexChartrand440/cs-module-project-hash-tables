# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    words = f.read();

letters = {};

total = 0;

for c in words:
    total += 1;
    if len(c.strip()) <= 0 or c.isalpha() == False:
        continue;
    if c in letters:
        letters[c] = letters[c] + 1;
    else:
        letters[c] = 1;

print('Total letters: ' + str(total));
print(letters.items());

thingy = [ 'e', 't', 'a', 'o', 'h', 'n', 'r', 'i', 's', 'd', 'l', 'w', 'u', 'g', 'f', 'b', 'm', 'y', 'c', 'p', 'k', 'v', 'q', 'j', 'x', 'z'];
aaaa = {};

index = 0;

letters_sorted = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}

for i in letters_sorted.items():
    if i[0] == 'â':
        continue;
    aaaa[i[0]] = thingy[index];
    index += 1;
    # print(i[0] + ' - ' + str((i[1] * 100) / total) + '%');

new_words = '';

for c in words:
    if c.isalpha() and c != 'â':
        new_words += aaaa[c];
    else:
        new_words += c;

print(new_words);