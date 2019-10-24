#%%

import re 

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)



#%%

print(x)

#%%

zipcode = "31245"
zipcode2 = "32145-2432"
zipcode3 = "3214874538476"
zipcode4 = "oue23"

print(re.search("\d+", zipcode))
print(re.search("^\d{5}$|^\d{5}-\d{4}$", zipcode))
print(re.search("\d{5}[-]\d{4}", zipcode2))
print(re.search("\d{5}", zipcode3))
print(re.search("\d{5}", zipcode4))

#create a variable to use
regexpression = "^(\d{5}|^\d{5}-\d{4})$"

def zipcodecheck(y):
    print(re.search("^(\d{5})(-\d{4})?$", y))
#%%

#time of day stuff 
#side note: ascii check [a-zA-Z]

time = "5pm"
time2 = "12:00pm"
time3 = "13:00am"
time4 = "00:02pm"
time5 = "6am"

timecheck = "^([1-9]|1[0-2])(:\d\d)?[ap]m?$"

print(re.search(timecheck, time))
print(re.search(timecheck, time2))
print(re.search(timecheck, time3))
print(re.search(timecheck, time4))
print(re.search(timecheck, time5))

#%%
