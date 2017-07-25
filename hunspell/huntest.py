# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import hunspell
import argparse
import datetime
from collections import Counter

start = datetime.datetime.now()

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="choose language de or en")
parser.add_argument("text", help="sentence to test")
args = parser.parse_args()

lang = args.lang or "en"
text = args.text or ""

dics = None
if lang == 'de':
    dics = hunspell.HunSpell('dics/de_DE_frami.dic', 'dics/de_DE_frami.aff')
else:
    dics = hunspell.HunSpell('dics/en_US.dic', 'dics/en_US.aff')

print("Text input: " + text)
print("Language: " + lang)

# break sentence into list of words to process
wordList = text.split()
finalList = []

print("====CORRECTION START========")

for word in wordList:
    if not dics.spell(word):
        lettersList = list(word.lower())
        suggestions = dics.suggest(word)
        print("Correcting " + word + " with suggestions ")
        print(suggestions)

        try:
            if(len(suggestions) == 0):
                finalList.append(word)
            else:
                # check for words with the most same letters first
                sameletterSuggestion = None
                maxSameLetter = 0
                currentSuggestionIsUppercase = False

                for suggestion in suggestions:
                    matchLetterCount = 0
                    isUpperCase = False

                    if suggestion.istitle():
                        isUpperCase = True

                    suggestionLetters = list(suggestion.lower())
                    for letter in suggestionLetters:
                        if letter in lettersList:
                            matchLetterCount += 1

                    if matchLetterCount > maxSameLetter and not currentSuggestionIsUppercase:
                        maxSameLetter = matchLetterCount
                        sameletterSuggestion = suggestion
                        if isUpperCase:
                            currentSuggestionIsUppercase = True
                
                finalList.append(sameletterSuggestion)

        except:
            finalList.append(word)

    else:
        print(word + " is correct")
        finalList.append(word)

# print output
print("====FINAL OUTPUT====")
print(" ".join(finalList))

end = datetime.datetime.now()
delta = end - start
print("Time elapsed : " + str(delta.total_seconds()))