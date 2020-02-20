# Ask 1

import codecs
import os

# checking if the file name is valid and can be read
while True:
    f1 = input("Give the name of the file: ")
    if os.access(f1, os.R_OK):
        break
file = codecs.open(f1, "r", encoding='utf-8')
wordlist = []
word = ""

# importing the words into a list
for letter in file.read():
    if letter.isalpha():
        word += letter
    elif letter in "0123456789":
        word = ""
    else:
        wordlist.append(word)
        word = ""
file.close()

# list sorting
word = ""
for i in range(len(wordlist)-1):
    for j in range(len(wordlist)-1, i-1, -1):
        if len(wordlist[j]) > len(wordlist[j-1]):
            wordlist[j],wordlist[j-1] = wordlist[j-1],wordlist[j]

# removing the smaller words
for i in range(len(wordlist)):
    if i>=5:
        wordlist[i] = ""

# list reversing
for i in range(len(wordlist)-1):
    for j in wordlist[i]:
        word = j + word
    wordlist[i] = word
    word = ""

# removing vowels from list items
word = ""
for i in range(len(wordlist)-1):
    for j in wordlist[i]:
        if j in "aeyuioAEYUIO":
            word += ""
        elif j in "αεηιυοωάέήίύόώΑΕΗΙΥΟΩΆΈΉΊΎΌΏ":
            word += ""
        else:
            word += j
    wordlist[i] = word
    word = ""

# printing the 5 biggest words reversed with the vowels removed
if len(wordlist) >= 5:
    for i in range(5):
        print(wordlist[i])
else:
    for i in wordlist:
        print(i)