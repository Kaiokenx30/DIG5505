#%%
import nltk

#noise removal
not_needed = ["about", "pants"]

text = "There is just something about pants that really don't quite add up."

def noise_removed (text):
    words = text.split()
    final_text = [word for word in words if word not in not_needed]
    final_text = " ".join(final_text)
    return final_text

#tokenization

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print (tokens)

#remove punctuation

words = [word for word in tokens if word.isalpha()]
print (words)
#%%
