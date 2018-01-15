import os, random

def random_line(fisier, no=1):
	line = []
	while (no >= 1):
		one_line = random.choice(open(fisier).readlines())
		line.append(one_line.rstrip())
		no = no - 1
	return line


def generare():
	filename = random.choice(os.listdir("intrebari"))
	sentence = random_line('intrebari.txt')
	os.chdir("intrebari")
	no = sentence[0].split()[0]
	sentence = sentence[0].split(' ', 1)[1]
	words = random_line(filename, int(no))
	for i in range(0, int(no)):
		sentence = sentence.replace("_", words[i], 1)

	print sentence

generare()





