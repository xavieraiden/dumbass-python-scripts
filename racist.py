# please ignore all the dumbass spelling mistakes

# imports random
import random

# establishes the racist syllables used in the sentences (you can add more or remove some if you want lol)
racism = ["ching","chong","ling",'xi','cha','hao','bing','wing','long']

# input to specify how many syllables in generated sentence
amnt = input("How many syllables? ")

# idek if i needed to do this but it's just and empty string
sentence = ""

# adds together random words from racism until it reaches specified length.
for x in range(int(amnt)):
    sentence = sentence + " " + random.choice(racism)
    
# outputs sentence
print(sentence)

# pauses until input so you can read your sentence
input("Press literally anything to make this go away, preferrably forever")
