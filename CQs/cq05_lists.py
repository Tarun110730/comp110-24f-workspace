"""Mutating functions"""

__author__="730744485"

def manual_append(x:list[int],new:int)->None:
    x.append(new)
    #Was going to include print(x) in the function definition but testing it in the repl, I realized I didn't need it.
    #This function is really simple! It just appends a list, given that the list is a list of integers.

def double(y:list[int])->None:
    idx=0
    while idx<len(y): #This was a very simple while loop to construct using the familiar index variables and length fucntion
        y[idx]=y[idx]*2
        idx+=1

list_1:list[int]=[1,2,3]
list_2:list[int]=list_1
double(list_2)
print(list_1)
print(list_2)
#My theory is that list_1 will be [1,2,3] and list_2 will be [2,4,6]. 
#The theory was proven wrong because I assumed that lists work like variables in memory.
#However,the lists work more complexly than variables.
#Essentially, the lists are like reference data types while varaibles are more primitive data types.
