"""Testing functions in list_fns.py"""

from exercises.lessons.lists_fns import get_first # type: ignore
def test_get_first()->None:
    assert get_first(input=["Viktorya","Samy","Izzi"])=="Viktorya"
test_get_first()
