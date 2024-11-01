"""Testing the find and remove max function"""

__author__="730744485"

from CQs.cq07.find_max import find_and_remove_max
#These were relatively easy to write. The only problem I encountered was making sure the syntax was right.
def test_find_and_remove_max()->None: 
    a=[1,2,3,2,1]
    assert find_and_remove_max(a)==3
def test_find_and_remove_max1()->None:
    a=[1,2,3,3,2,1]
    find_and_remove_max(a)
    assert a==[1,2,2,1]
def test_find_and_remove_max2()->None:
    a=[]
    assert find_and_remove_max(a)==-1
