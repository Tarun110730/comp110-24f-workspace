"""Implementing functions that run wordle's main game loop"""

__author__="730744485"

#Originally did this with string concatenation but realized that I had to do it with f strings.
def input_guess(secret_word_len:int)->str: # type: ignore
    """Makes sure that the input guess is the right amount of characters"""
    y:str=input(f"Enter a {secret_word_len} character word: ")
    while len(y)!=secret_word_len:
        y=input(f"That wasn't {secret_word_len} chars! Try again: ")
    if len(y)==secret_word_len:
        return y
    

def contains_char(secret_word:str,guess_char:str)->bool:#type:ignore 
    """A function to check if a character is in the input_str"""
    assert len(guess_char)==1
    index=0
    while index<len(secret_word):
        if secret_word[index]==guess_char:
            return True
        else:
            index=index+1
    #Took me a whille to figure out why this if statement was working as I set it as if index > len(secret_word)
    #but then I figured out I had to set it as >= to make sure that it worked.
    if index >= len(secret_word):
            return False
#Also figured out that I didn't have to do print(False) or print(True) since I was going to print in the repl. It simplified things.

def emojified(input_word:str,secret:str)->str:
     """A function to compare the input with the secret word to check if the input is the same as the secret word.
     The function will use emojis to denote different results."""
     assert len(input_word)==len(secret)
     
     WHITE_BOX: str = "\U00002B1C"
     GREEN_BOX: str = "\U0001F7E9"
     YELLOW_BOX: str = "\U0001F7E8"
     
     result_string=""#To store the emojis
     i=0
     while i<len(input_word):
        if input_word[i]==secret[i]: 
            result_string+=GREEN_BOX  #Adding to the result string 
        elif contains_char(secret,input_word[i]): #if secret contains input word[i], then it will add a yellow box to the result string
            result_string+=YELLOW_BOX 
        else:
            result_string+=WHITE_BOX
        i=i+1
     return result_string

def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns=1
    guessed= False
    while turns<7 and not guessed:
        print(f"=== Turn {turns}/6 ===")
        input=input_guess(secret_word_len=len(secret))#Took me a minute to figure out that I should set input_guess equal to a variable
        #This helped me easily create the if then statement with input==secret and input!=secret
        print(emojified(input_word=input,secret=secret))
        if input==secret:
            print(f"You won in {turns}/6 turns!")
            guessed=True
        if input!=secret:
            turns=turns+1
    if turns>=7: #Learned from earlier in the code with contains char that I had to set it >=7
        print(f"X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
        main(secret="codes")
