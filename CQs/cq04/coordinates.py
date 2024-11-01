"""Creating a function that creates coordinates with strings"""

__author__="730744485"

def get_coords(xs:str, ys:str) -> None:
    index_x=0
    while index_x<len(xs):
        index_y=0
        while index_y<len(ys):
            print((xs[index_x],ys[index_y]))
            index_y=index_y+1
        index_x=index_x+1
