"""Implementing some utility functions for dictionaries"""

__author__="730744485"

#The second part of the function where we had to actually invert the function was what I started with.
#I approached it by looking at what the dictionary was based upon in a for loop and realized that it was the keys
#Then I assigned a variable value to a[key] and inverted that relationship for inverted_dict
#For the Key Error part of the function, I thought of how to check if there were duplicate values and came up with a nested for loop
#This would check if key1 and key2 are equal and if the values each key has are the same.
def invert(a:dict[str,str])->dict[str,str]:
    """Inverting a dictionary (making the values become keys)"""
    for key1 in a:
        for key2 in a:
            if key1 != key2 and a[key1] == a[key2]:
                raise KeyError("Duplicate value found")
    inverted_dict={}
    for key in a:
        value=a[key]
        inverted_dict[value]=key
    return inverted_dict

#I started by creating a strategy where I would take all the values out of the dictionary and keep them in a list.
#Then I would check the list for the most popular value.
#I found out that this was way too difficult and approached a TA to get an implementation strategy
#This was the implementation strategy:
    #The first iteration is going to go through every key in the input dict and get the color(which is your key)
    #Then it's gonna add each to key colors dictionary
    #Each value associated will be the count
    #Iterate through the colors dict values to find the max value

def favorite_color(a:dict[str,str])->str:
    colors:dict[str,int]={}
    if a=={}:
        return ""
    for key in a:
        if a[key] not in colors:
            colors[a[key]]=1
        if a[key] in colors:
            colors[a[key]]+=1
    max=0
    fav_color:str=""
    for key in colors:
        if colors[key]>max:
            max=colors[key]
    for key in colors:    
        if colors[key]==max:
            fav_color=key
    return fav_color

#Since I was given an implemetation strategy for count, all I had to do was actually implement it. 
# All of it was laid out well enough for me to just have to translate english to code.
def count(a:list[str])->dict[str,int]:
    b:dict[str,int]={}
    for key in a:
        if key in b:
            b[key]+=1
        else:
            b[key]=1
    return b


#Alphabetizer was a very hard function to code because I didn't know how to make it such that one key would make a list
#that would have the same first letter. But after working on it for some time, I finally realized that I could use the for loop structure
#and the dictionary structure to create my dictionary. Since dictionaries can't have duplicate keys and the keys 
#will match up to the words in the for loop, the dictionary will come out with a list that would have the same first letter as the key.
def alphabetizer(words:list[str])->dict[str,list[str]]:
    alphabetized:dict[str,list[str]]={}
    for word in words:
        key=word[0].lower()
        if key not in alphabetized:
            alphabetized[key]=[]
        alphabetized[key].append(word)
    return alphabetized


#update_attendance was fairly easy to code compared to the rest of the utility functions in this exercise.
#All I had to do was mutate the dictionary to be updated. The only problems were the details such as a day not already being in attendance
#or a student already being in attendance for that day.
def update_attendance(attendance:dict[str,list[str]],day:str,student:str)->None:
    if day not in attendance:
        attendance[day]=[student]
    if student not in attendance[day]:
        attendance[day].append(student)