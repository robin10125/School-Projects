words = open("Dictionary.txt", "r")

dict = {"first entry": "first value"}
noun_dict = {}
verb_dict = {}
adjective_dict = {}
adverb_dict = {}
preposition_dict = {}
other_dict = {}
check = False
lines = words.readlines()
print(lines[26])
subTitles = {"Defn:", "Note:", "Syn.\n", "[Obs.]", "(6).", "Syn.", "10\n"}

for a in range(20):
    subTitles.add(str(a) + ".")
    subTitles.add(str(a) + ".\n")
print(subTitles)
deletStop = lines[27]
while lines[1] != deletStop:
    del lines[0]

lineCollection = ""
linePrevious = "first entry"
count = 0
import random
for indLine in lines:

    lineSeperate = indLine.split(" ")
    if indLine == "\n":
        check = True

    elif check == True and lineSeperate[0] not in subTitles and len(lineSeperate) == 1:
        dict[linePrevious] = lineCollection
        if indLine in dict:
            entry = indLine + "~~~~~" + str(int(100000 * random.random()))
            dict[entry] = ""
            linePrevious = entry
        else:
            dict[indLine] = ""
            linePrevious = indLine
        check = False

        lineCollection = ""
    else:
        lineCollection += indLine
    count += 1
    if check == True and indLine != "\n":
        check = False




inputCheck = False
while inputCheck == False:
    inputWord = input("Enter a word.")
    inputWord = inputWord.upper()
    if inputWord == "CANCEL PROGRAM":
        inputCheck = True

    else:
        inputWord += "\n"
    if inputWord in dict:
        print(dict[inputWord])


newText = True
if newText == True:
    newDict = open("Newdict.txt", "w")
    w
    defnIndicator = {"1.", "2.","3.","4.","5.","6.","7.", "8.", "9.", "10.", "--", "Defn:"}

    for indWord in dict:
        wordText = dict[indWord]
        wordtextSplit = wordText.split("\n")
        firstLine = wordtextSplit[0].split(" ")
        wordType = ""
        for firstLineElements in firstLine:
            if firstLineElements == "Etym:":
                break
            elif firstLineElements != firstLine[0]:
                wordType += firstLineElements + ","

        defnCheck = False
        definition = ""
        for wordTextLines in wordtextSplit:
            wordTextLineElements = wordTextLines.split(" ")
            if wordTextLineElements[0] in defnIndicator:
                defnCheck = True
            if defnCheck == True:
                definition += wordTextLines

        newDict.write(indWord + " " + wordType + definition + "\n")
    newDict.close()
words.close()






