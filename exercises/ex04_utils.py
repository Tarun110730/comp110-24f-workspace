"""Learning how to use the list functionality through an exercise"""

__author__="730744485"

def all(a:list[int],check:int)->bool:
    idx=0
    counter=0 #Realized that I had to make a counter so that I could check if it was all equal.
    if a==[]: #Realized that this had to return false per the autograder and typed a line as such before the while loop
        return False
    while idx<len(a):
        if a[idx]==check:
            counter+=1
        idx+=1
    if counter==len(a):
        return True
    else:
        return False


#I initially tried to make max work with a lot of changing of the max variable but I realized that the while loop code could be simplified and I did so.
def max(b:list[int])->int:
    if len(b) == 0:
        raise ValueError("max() arg is an empty List")
    idx=0
    max=b[0]
    while idx<len(b): 
        if b[idx]>max:
            max=b[idx]
        idx+=1
    return max


def is_equal(c:list[int],d:list[int])->bool:
    #Also here had to find the common link between my errors with the autograder. 
    #Found it to be that it has to be the same lengths and coded it accordingly 
    if len(c) != len(d): 
        return False
    idx=0
    counter=0 #Learning from the function all, I also made a counter here to check if everything is equal.
    while idx<len(c):
        if c[idx]==d[idx]:
            counter+=1
        idx+=1
    if counter==len(c):
        return True
    else:
        return False

def extend(e: list[int],f: list[int])->None:
    #This was very simply to code. The only thing that I missed initially was not including the idx+=1 in the while loop.
    #Perhaps this was because it was out of if loops so I got used to backspacing a tab. However, there was no if loop here.
    idx=0
    while idx<len(f):
        e.append(f[idx])
        idx+=1
    print(e)

