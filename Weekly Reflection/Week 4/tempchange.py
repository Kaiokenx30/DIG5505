#%%

def to_f(c):
    return ((9/5)*c) + 32

def to_c(f):
    return (5/9) * (f-32)

#lower temps

def to_f2(c):
    if c < -273.15:
        raise ValueError('Temp value is below absolute zero')
    return ((9/5) * c) + 32


#%%
