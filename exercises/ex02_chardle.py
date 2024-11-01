"""EX02 - Chardle - A cute step toward Wordle."""

__author__="730744485"

#I knew that I had to implement a checking system to make sure that the amount of characters in the word was 5.
# To do this I was initially going to implement an if and elif statement with < and > to exclude numbers less than and greater than 5.
# But then I realized I could just use the not equal to operator (!=). That simplified the code to an if else statement.
def input_word() ->str:
    word=input("Enter a 5-character word: ")
    if len(word)!=5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        print(word)
        return word
#I only realized a little later that to make the contain_char function work, I needed to return word.

#Here, I applied the same logic, quickly using the not equal to operator (!=).
def input_letter() ->str:
    character=input("Enter a single character: ")
    if len(character)!=1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print(character)
    return character
#Same here. Quickly realized I needed to return character.

def contains_char(word:str, letter:str) ->None:
    print("Searching for "+letter+" in "+word)
    count=0
    if letter==word[0]:
        print(letter+" found at index 0")
        count=count+1
    if letter==word[1]:
        print(letter+" found at index 1")
        count=count+1
    if letter==word[2]:
        print(letter+" found at index 2")
        count=count+1
    if letter==word[3]:
        print(letter+" found at index 3")
        count=count+1
    if letter==word[4]:
        print(letter+" found at index 4")
        count=count+1
    if count==0:
        print("No instances of "+letter+" found in "+word)
    if count==1:
        print(str(count)+" instance of "+letter+" found in "+word)
    if count>1:
        print(str(count)+" instances of "+letter+" found in "+word)
#Ran into an error with count + "instances of" and realized I needed to make count a str.

#I know that the main function really ties it all together but the chardle game was working just fine without it.
# Was it really necessary?
def main() ->None:
    contains_char(word=input_word(),letter=input_letter())
if __name__ == "__main__":
    main()