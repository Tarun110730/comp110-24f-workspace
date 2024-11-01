""""In this exercise, I am practicing using a while loop to iterate over a string!"""

__author__="730744485"

def num_instances(phrase:str,search_char:str)->None:
    count=0
    x=0
    while x<len(phrase):
        element=phrase[x]
        if search_char==element:
            count=count+1
        x=x+1
    print(count)

num_instances(phrase="Happy Tuesday",search_char="y")