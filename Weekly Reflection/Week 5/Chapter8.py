#%%

'hello world' [0:500]

'hello world' [450:500]

greeting = 'hello world'

greeting[0].upper() + greeting[1:]

#step: 0 starts at beginning going to the end up to but not including character 9 but skipping by 2
'abcdefgh' [0:9:2]

#go over whole thing
'abcdefgh'[::2]
#all even digits
'0123456789'[::2]

#determining the last characters of a string
'hello world'[-1:]

'hello world'[-5:]

#lowercase all characters
'HELLO World'.lower()

original = 'Burma Shave'

lowercase = original.lower()

#%%

wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber.'

wyatt = wyatt.lower()

#double letter detection
for c in wyatt:
    print(c)

for i in range(len(wyatt)):
    print(wyatt[i])

for i in range(len(wyatt)):
    print(i, wyatt[i])

#find the range of a string
range(len(wyatt))

#break into paors of letters
for i in range(len(wyatt)):
    print (wyatt[i:i+2])

#count pairs of ee
pairs = 0
for i in range(len(wyatt)):
    if wyatt[i:i+2] == 'ee':
        pairs = pairs + 1

#count pairs of each double letter
pairs = 0
for i in range(len(wyatt)-1):
    if wyatt[i] == wyatt[i+1]:
        pairs = pairs + 1

#%%

#exercise 8-1
#detects double letters in a string input
def twin(input):
    pairs = 0
    input = input.lower()
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            pairs = pairs +1
            return pairs

#%%

#larger strings
text = 'All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.'

len(text)
#splitting text into words
text.split(' ')

#determine the amount of words in a string
len(text.split(' '))

#separated based on the word and
text.split('and')

#joining and sorting strings
names = ['Bob', 'Carol', 'Ted', 'Alice']
#%%
