"""This is a program to help me plan a cozy tea party"""


__author__: str = "730744485"

#Comment: Creating the main_function was hard as I had to mix strings and ints. 
# I initially thought I could concatenate strings and ints but I quickly found that it didn't work. 
# Then, I tried to put a string quotation "" like so on guests but that just returned the word guests. 
# Then, I realized I had to put str(guests). Thus, I figured out how to make an int a str to work with this code.

#Comment: Another note is that figuring out how to print the cost function and make it work was the hardest for me. 
# I again did not realize that I needed to equate the function to anything, initially typing tea_count=tea_bags().
# But then, looking at trailhead, I figured out that I had to input something in the functions to gain the return value of tea_bags 
# and treats. Alternatively, I wonder if I could've set a variable equal to the return value of teabags so that tea_count=x where 
# x=tea_bags(guests) instead of the redundant tea_count=tea_bags(guests). Although, that improvement is minor.
# I guess it would only be helpful for clarity's sake.
def main_planner(guests:int) -> None:
    """This will display the functions all together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: "+str(int(tea_bags(guests))))
    print("Treats: "+str(int(treats(guests))))
    print ("Cost: $"+str(float(cost(tea_count=tea_bags(guests), treat_count=treats(guests)))))
    return None
    


def tea_bags(people:int) -> int:
    """This will return the number of teabags I should get for my tea party"""
    return 2*people


#Comment: I initially struggled in starting this function. 
# But I figured out that instead of simply having tea_bags(), I should have teabags(people=people) 
# to link the treats function and the tea_bags function.

def treats(people:int) -> int:
    """"This will return the number of treats I should get for my tea party"""
    return int(1.5*tea_bags(people=people))
    

def cost(tea_count:int,treat_count:int) -> float:
    """This will return the total cost of the tea bags and treats"""
    return 0.5*tea_count+0.75*treat_count

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))