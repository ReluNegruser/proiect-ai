import glob, os
from collections import defaultdict
import cv2
from matplotlib import pyplot as plt, cbook
import nltk
from nltk.corpus import wordnet as wn

path = 'C:\\Users\Ayush\PycharmProjects\AI\Proiect'
image_dict = dict()
imageNText = defaultdict()


for i,infile in enumerate(glob.glob(os.path.join(path,'*.png'))):
    img = cv2.imread(infile)
    my_key = i
    image_dict[my_key] = img

imageNText[0] = []
imageNText[0].append('cartilaj al coastei')
imageNText[0].append('corpul sternal')
imageNText[0].append('procesul xifoid')
imageNText[0].append('promontoriul sacral')

imageNText[1] = []
imageNText[1].append('muschiul pectoral mare')
imageNText[1].append('linia alba')
imageNText[1].append('muschiul mare dorsal')
imageNText[1].append('fibre intercrurale')

imageNText[2] = []
imageNText[2].append('muschiul dintat anterior')
imageNText[2].append('muschiul oblic extern')
imageNText[2].append('muschiul drept abdominal')
imageNText[2].append('muschiul transvers abdominal')

imageNText[3] = []
imageNText[3].append('spina iliaca antero-superioara')
imageNText[3].append('muschiul oblic intern')
imageNText[3].append('muschiul cremaster')
imageNText[3].append('tendonul conjunct')

question = "Din ce muschi este alcatuit abdomenul?" \
           "Abdomenul este alcatuit din muschiul cremaster, spina iliaca antero-superioara, muschiul oblic intern, tendonul conjunct."


def imageIndex(image, imageText, question):
    tokensQuestion = nltk.word_tokenize(question)
    print(wn.synsets('os'))
    countersList = []
    counter = 0
    tokenCounter = 0
    imageCounter = 0
    while imageCounter < len(imageText):
        while (tokenCounter < len(tokensQuestion)):
            for i in range (0, len(imageText)):
                if (tokensQuestion[tokenCounter] in imageText[imageCounter][i]):
                    counter = counter + 1
            tokenCounter = tokenCounter + 1
        countersList.append(counter)
        counter = 0
        imageCounter = imageCounter + 1
        tokenCounter = 0
    maxVal = max(countersList)
    
    index = 0
    for i  in range (0, len(countersList)):
        if (countersList[i] == maxVal):
            index = i
    
    plt.imshow(image[index], cmap='copper', interpolation='bilinear')
    plt.show()

imageIndex(image_dict, imageNText, question)
