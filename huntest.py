import hunspell
import argparse
import time

start = time.clock()

parser = argparse.ArgumentParser()
parser.add_argument("--lang", help="choose language de or en")
parser.add_argument("text", help="sentence to test")
args = parser.parse_args()

lang = args.lang or "en"
text = args.text or ""

dics = None
if lang == 'de':
    dics = hunspell.HunSpell('dics/de_DE_frami.dic', 'dics/de_DE_frami.aff')
    print dics.spell("hund")
    print dics.suggest("hund")
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
        suggestions = dics.suggest(word)
        print("Correcting " + word + " with suggestions " + u", ".join(suggestions))

        # take first suggestion
        finalList.append(suggestions[0])
    else:
        print(word + " is correct")
        finalList.append(word)

# print output
print "====FINAL OUTPUT===="
print " ".join(finalList)

end = time.clock()
print("Time elapsed : " + str(end-start))