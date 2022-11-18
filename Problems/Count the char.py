length = input()
letters = input()
dict = {}
for i in range(97, 97+26+1):
    dict[chr(i)] = 0;
for letter in letters:
    if letter in dict.keys():
        dict[letter] += 1
for i in range(97, 97+26):
    print(f"{chr(i)}: {dict[chr(i)]}")