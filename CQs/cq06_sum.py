"""Summing the elements of a list using different loops"""

__author__="730744485"

def w_sum(vals:list[float])->float:
    if vals==[]: #Simple, but useful way to take away the edge case with the while loop
        return 0.0
    idx=0
    a:float=0.0
    #This took a few minutes to figure out but I realized that I could set a variable to be updated
    #It reminded me exactly of the empty string that we used to put the emojis in for wordle
    while idx<len(vals):
        a=a+vals[idx]
        idx+=1
    return a

def f_sum(vals:list[float])->float:
    a:float=0.0
    for elem in vals:
        a+=elem #I figured out by talking to someone that I could do this. I had some sort of intuition that this might work but I wasn't sure. 
    return a

def f_range_sum(vals:list[float])->float:
    a:float=0.0
    for elem in range (0,len(vals)):
        a+=vals[elem] #This was very simple because range just makes it indices instead of actual values 
        #so instead of adding elems together, I was adding vals[elems] together.
    return a