def get_first(input:list[str])->str:
    return input[0]
def remove_first(input:list[str])->None:
    input.pop(0)
def get_and_remove_first(input:list[str])->str:
    a=input.pop(0)
    return a