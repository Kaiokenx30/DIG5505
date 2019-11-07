#%%
def median (data):
    return (sum(data)/2)

test = [1, 2, 3, 4, 5]

median(test)
# %%
#found online, dont understand the if else at the end
def med(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

med(test)

# %%
#found by looking up the statistics socumentation
from statistics import median
median([3, 7, 14, 6, 9, -5])


# %%
