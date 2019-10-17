#%%

#Expanding upon the temperature conversion starter program to include more conversions some common and some less common/strange
#7-2 instructions: Use one of this chapter’s “starter programs” as a basis for your work, develop amodified program that you believe improves on the version presented here. As withthe original program, the program you create should be simple and should do onesimple thing.
#I am expanding on this a bit to include more than just one thing.
#converting to farenheit
def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature value is below absolute zero.")
    return ((9/5) * c) + 32

#converting to celcius
def to_c(f):
    return (5/9) * (f-32)

#convery human years to dog years
def dog_years(y):
    if y > 0:
        y = y * 15
        print(y, "dog years")
    else:
        return ("Invalid Input")

#cooking conversions
def ounce_to_gram(a):
    if a > 0:
        a = a * 28
        print(a,"grams")
    else:
        return ("Invalid Input")



#%%
