"""Writing the find and remove max function"""

__author__="730744485"

#I had a lot of issues coding this. Firstly I thought I could use the max function from ex04 
# but I later changed it to a for loop that achieved the same thing.
#Secondly, one of the problems I had was with the second loop which was a while loop bc I had it written as such
"""if max==a
        a.pop(idx1)
    idx1+=1"""
#However, after much deliberation with the TA, he figured out that we should write it as the way it is written now
#He explained that it was an error in memory that caused the idx variable to skip over an index after we popped a certain index.
#After all of this, it was smooth sailing.
def find_and_remove_max(a:list[int])->int:
    if len(a) == 0:
        a=a
        return -1
    max:int =-1 #changed this from a[0] 
    for x in a:
        if x>max:
            max=x
    idx1:int=0
    while idx1<len(a):
        if max==a[idx1]:
            a.pop(idx1)
        else:
            idx1+=1
    return max

