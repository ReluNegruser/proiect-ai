f = open('words', 'r')
lines = f.readlines()
words = []
for i in lines:
    words.append(i.split(" "))
f.close()
for i in range(0, len(words)):
    print(words[i])