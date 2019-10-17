#%%
#running through the practice programs in chapter 9 and progressing as much as possible through the exercise
import re

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

source = open('1342-0.txt', encoding="utf8")
pride = source.read()

print(pride[:1000])

#%%
result = re.findall(r'[!]', pride)

print(result)

len(result)
#there are 500 ! in P&P 

#%%
#finding all the quotes in P&P
quotes = re.findall(r'“[^”]*”', pride)

print(quotes)
len(quotes)

#%%
#percentage of quotes
len(''.join(quotes))

len(''.join(quotes)) / len(pride)

#(len(''.join(quotes)) / float(len(pride))) * 100

pride_percent = (len(''.join(quotes)) / float(len(pride))) * 100

print(pride_percent)

#%%
#finding wordcount in P&P
pride_words_2 = re.findall(r'[A-Za-z]+', pride)
len(pride_words_2)

pride_words_2[4000:4050]

#%%

#exercise 7-1
def exclaim (pride):
    full_exclaimed = re.findall(r'.*!', pride)
    
    print(full_exclaimed)

    len(full_exclaimed)
    exclaimed_percent = (len(''.join(full_exclaimed)) / len(pride)) * 100

    return exclaimed_percent


#%%
