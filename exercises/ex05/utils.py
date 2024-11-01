"""Implementing some more utility functions"""

__author__="730744485"

#Originally tried to code this with a for loop but upon trying it I found out that using the pop function would make it ineffective
#Therefore I wrote it with a while loop instead
def only_evens(a:list[int])->list:
    """Creating a function that returns a list of only even numbers based on the input list"""
    if a==[]:
        return []
    #Added this part while I was unit testing and figured out that my function was actually mutating the input list because I originally just did b=a.
    #I knew this before but it was interesting to see still that lists don't function like variables. I just forgot that when I was coding this.
    #Based on that fact, I decided to create an empty list called b that appended all the values of a into b.
    #That passed the unit test :)
    b=[]
    for x in range(0,len(a)):
        b.append(a[x])    
    idx=0
    while idx<len(b):
        if b[idx]%2!=0:
            b.pop(idx)
        else:
            idx+=1
    return b

#The edge case here took a minute to figure out but I got it in the end. I had to use a little bit of creativity to figure out how to overcome the index error use case.
#The actual function also took a minute to figure out, but once I remembered how range and append worked it was fairly simple. The real trick was realizing it was easier
#to use append than pop.
def sub(a:list[int],start:int,end: int)->list:
    """Creating a function that returns a subset of the input list based on the start and end indices inputted"""
    b=[]
    if a==[] or start>=len(a) or end<=0:
        return []
    if start<0:
        start=0
    if end>len(a):
        end=len(a)
    for x in range(start,end):
        b.append(a[x])
    return b
 
#The edge case took about a minute to figure out how to raise the index error. But I figured that if idx>len(a) that would raise an index error.
#Writing the code for this function was particularly challenging as I had to think outside of the box to assign idx1=idx.
#Additionally, I ran into errors with Index Errors in a simple use case so I realized that once I had appended a to include 0, I had to do while idx1<len(a)-1
#That finally did the trick.
def add_at_index(a:list[int], value:int, idx:int)->None:
   """Creating a function that adds a value at a certain index"""
   if idx<0 or idx>len(a):
       raise IndexError("Index is out of bounds for input list")
   a.append(0)
   for elem in range(len(a)-1,idx,-1):
       a[elem]=a[elem-1]
   a[idx]=value