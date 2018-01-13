import os, random

def random_line(fisier, no=1):
	line = ''
	while (no >= 1):
		line = line + random.choice(open(fisier).readlines())
		no = no - 1
	return line


def generare():
	filename = random.choice(os.listdir("intrebari"))
	os.chdir("intrebari")
	sentence = random_line('intrebari.txt')
	no = sentence.split()[0]
	sentence = sentence.split(' ', 1)[1]
	words = random_line(filename, int(no))

	for i in range(0, int(no)):
		sentence = sentence.replace("_", words[i], 1)

	print sentence

generare()





