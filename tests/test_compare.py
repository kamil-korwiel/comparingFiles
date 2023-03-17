import pytest
from utility import compare_two_list_v2


@pytest.mark.parametrize("left_list, right_list, expected_output", [
    (['a','b','c','d','e','f','g','h','i','j','k'],
     ['a','b','c','d','e','f','g','h','i','j','k'],
     {
         "left":[],
         "right":[]
     }),
    (['a','b','c','d','e','f','k'],
     ['a','b','e','f','g','h','i','j','k'],
     {
         "left": ['c','d',],
         "right": ['g','h','i','j',]
     }),
    (['a'],
     [],
     {
         "left": ['a'],
         "right": []
     }),
    ([],
     ['a'],
     {
         "left": [],
         "right": ['a']
     }),
    ([],
     [],
     {
         "left": [],
         "right": []
     }),
])
def test_compare_two_list(left_list, right_list, expected_output):
    assert compare_two_list_v2(left_list, right_list) == expected_output
