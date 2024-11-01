"""Testing the utility functions in utils.py"""

__author__="730744485"

import pytest

from exercises.ex05.utils import only_evens, sub, add_at_index 
#The import syntax is so long

#Testing only evens
#One use case for only evens testing what the function should return
def test_only_evens()->None:
    assert only_evens(a=[2,4,5,7,8,9])==[2,4,8]

#One use case for only evens demonstrating how the function should not mutate its input list
def test_only_evens1()->None:
    c=[0,2,4,5,6]
    only_evens(a=c)
    assert c==[0,2,4,5,6]

#One edge case for only evens testing if an empty list breaks down the code or not
def test_only_evens2()->None:
    c=[]
    assert only_evens(a=c)==[]


#Testing sub
#One use case for sub testing what the function should return
def test_sub()->None:
    assert sub(a=[2,4,6,8],start=1,end=3)==[4,6]

#One use case for sub testing how the function should not mutate its inpput list
def test_sub1()->None:
    c=[3,5,7,9]
    sub(a=c,start=1,end=3)
    assert c==[3,5,7,9]

#One edge case for sub testing if an empty list breaks down the code or not
def test_sub2()->None:
    assert sub(a=[],start=0,end=1)==[]

#One edge case testing if an start or end value larger or smaller than the actual list breaks it down
def test_sub3()->None:
    assert sub(a=[3,5,6,7,10],start=-1,end=7)==[3,5,6,7,10]  


#Testing add at index
#One use case for add at index testing what the function should return
def test_add_at_index()->None:
    assert add_at_index(a=[3,9,81],value=27,idx=2)==None

#One use case for add at index testing that the function mutates its input list
def test_add_at_index1()->None:
    c=[3,9,81]
    add_at_index(a=c,value=27,idx=2)
    assert c==[3,9,27,81]

#One edge case to check if the function raises an Index Error
def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    c=[1,2,4,8]
    with pytest.raises(IndexError):
        add_at_index(a=c,value=32,idx=6) 
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num> 
        # that is greater than the length of our <list_object>
