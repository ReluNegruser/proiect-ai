import nltk
# nltk.download('all')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('words')
# nltk.download('treebank')
# nltk.download('stopwords')
# nltk.download('wordnet')

imgandkey = {
    'img1': ['ficat', 'stomac', 'ulcer'],
    'img2': ['plamani', 'pneumonie', 'artera pulmonara'],
    'img3': ['Deltoid', 'muschi', 'retina', 'Triceps superior', 'Trapez'],
    'img4': ['deltoid', 'osul bazinului', 'retina', 'triceps superior', 'trapez', 'abductorii coapsei'],
    'img5': ['osul bazinului', 'osul coxal', 'coccis']
}

questions_dictionary = {
    'Ce tip de acid se gaseste in stomac?': ('HCl', 'NaCl', 'NaOH'),
    'Muschii scheletici nu asigura ...': ('Postura', 'Mimica', 'Echilibrul', 'Miscarile involuntare'),
    'Care muschi apartine membrului superior': ('Deltoid', 'Triceps superior', 'Trapez', 'Pectoral mare si mic'),
    'Care din urmatorii muschi apartine membrului inferior': ('Deltoid', 'Triceps superior', 'Abductorii coapsei', 'Abductorii gambei'),
    'Cate coaste are un om?': (26, 24, 22, 20, 18),
    'Care este cel mai lat os al scheletului uman?': ('Femurul', 'Sternul', 'Osul coxal (osul bazinului)', 'Maxilarul Craniul')
}

random_question = questions_dictionary['Care muschi apartine membrului superior']
# print(random_question)

sentence = "Ana merge la munte cu prietenii sai"

tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)

from nltk.corpus import stopwords

clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('romanian'):
        clean_tokens.remove(token)

# print(clean_tokens)

# English stemmer
# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# print(stemmer.stem('doctorul'))

# Romanian stemmer
# from nltk.stem import SnowballStemmer
# ro_stemmer = SnowballStemmer('romanian')
# print(ro_stemmer.stem("incercuit"))


# from nltk.corpus import wordnet
# synonyms = []
# for syn in wordnet.synsets('inima'):
#     for lemma in syn.lemmas():
#         synonyms.append(lemma.name())
# print(synonyms)


# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("orice"))

with open("date.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

questiondict = dict()
for c in content:
    qanda = c.split(":")
    q = qanda[0]
    ans = qanda[1].split("|")
    ans = tuple(ans)
    questiondict[q] = ans

qstring = 'Care este cel mai lat os al scheletului uman?'
ansstring = ""
for a in questiondict[qstring]:
    ansstring = ansstring + a + " "
fullstring = qstring + " " + ansstring

print('\n')
print(fullstring)
print('\n')

tokens = nltk.word_tokenize(fullstring)
for t in tokens:
    if len(t) <= 1:
        tokens.remove(t)

tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)

from nltk.corpus import stopwords

clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('romanian'):
        clean_tokens.remove(token)

print(clean_tokens)
print('\n')

# Romanian stemmer
from nltk.stem import SnowballStemmer
ro_stemmer = SnowballStemmer('romanian')
stemmed = list()
for ct in clean_tokens:
    stemmed.append(ro_stemmer.stem(ct))

print(stemmed)
print('\n')

maxcontor = -1
correctimg = ""

for key, value in imgandkey.items():
    contor = 0
    for j in value:
        for word in stemmed:
            if word in j:
                contor = contor + 1
    if contor > maxcontor:
        maxcontor = contor
        correctimg = key

print(correctimg)