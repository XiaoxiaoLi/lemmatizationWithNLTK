#Do lemmatization for each file in a folder using nltk in python

#Xiaoxiao Li, May 2012, cindyxiaoxiaoli@gmail.com

#prerequisite: has to have the nltk python package installed

import os #for file reading
import re #regular expression
import nltk#for lemmatization
import string
from sys import argv
import errno

from nltk.stem.wordnet import WordNetLemmatizer
lmtzr=WordNetLemmatizer()#create a lemmatizer object

#check is a word is capitalized, if you want
def iscapitalize(str):
    def containLetter():
        return len(string.letters) != len(string.letters.translate(string.maketrans('', ''), str))
    return str == str.capitalize() and containLetter()

def makeSurePathExists(path):
    try:
        os.makedirs(path)
    except OSError:
        pass

inputDir = argv[1]
outputDir = argv[2]

filenameArray=os.listdir(inputDir)
makeSurePathExists(outputDir)

#to check the results
ori_lemma_HoH={}#key is original word form, small key is lemma, value is freq

for filename in filenameArray:#for each file
    print ('beginning '+filename+'\n');#info in console
    inputpath = os.path.join(inputDir,filename)
    inputContent = open(inputpath)
    outputFilename='LEMMA_'+filename#put lemma before the file name
    outputpath = os.path.join(outputDir,outputFilename)
    outputContent=open(outputpath,'w')
    
    for line in inputContent:
        line = line.replace('\'','-');#filter
        line=line.strip()#chomp
        
        lemmaArray=[]#initialize an array for output for each line
        wordsArray=line.split()#store words in this line in a array
        for word in wordsArray:                              
            # if (iscapitalize(word)):#if the first is upper and the others are not, then
            #     word = word.lower();                      
            lemma=lmtzr.lemmatize(word)#DO LEMMATIZATION, only line needed to do lemmatization on a word with nltk

            #store ori form and lemma for manual examination
            if (word not in ori_lemma_HoH):
                ori_lemma_HoH[word] = {}
            if (lemma not in ori_lemma_HoH[word]):
                ori_lemma_HoH[word][lemma] = 1
            else:
                ori_lemma_HoH[word][lemma] += 1

            lemmaArray.append(lemma)
        outputContent.write(' '.join(lemmaArray)+'\n')
    inputContent.close()
    outputContent.close()

# #print ori word and its lemma if they are different, to check if lemmatization works
# oriLemmaPath='ori_lemma_hash.txt';
# oriLemmaFile = open(oriLemmaPath,'w')
# for word in ori_lemma_HoH.keys():# an lemma
#     for lemma in ori_lemma_HoH[word]:#each original form, actually there is only one
#         value = ori_lemma_HoH[word][lemma]
#         if(lemma != word):#only print if there are not the same
#             oriLemmaFile.write(word + '\t'+lemma + '\t' + str(value)+'\n')
# oriLemmaFile.close()
