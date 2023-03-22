import pytest
from utility import compare


@pytest.mark.parametrize("left_list, right_list, expected_output", [
    # 1
    (['a','b','c','d','e','f','g','h','i','j','k'],
     ['a','b','c','d','e','f','g','h','i','j','k'],
     {
         "left":[],
         "right":[]
     }),
    # 2
    (['a','b','c','d','e','f',                'k'],
     ['a','b',        'e','f','g','h','i','j','k'],
     {
         "left": ['c','d',],
         "right": ['g','h','i','j',]
     }),
    # 3
    (['a'],
     [],
     {
         "left": ['a'],
         "right": []
     }),
    # 4
    ([],
     ['a'],
     {
         "left": [],
         "right": ['a']
     }),
    # 5
    ([],
     [],
     {
         "left": [],
         "right": []
     }),
    # 6
    (['a','b','c','d','e','f','g','h','i','j','k'],
     ['a'],
     {
         "left": ['b','c','d','e','f','g','h','i','j','k'],
         "right": []
     }),
# 5
    # 1
    ([     'b',      'd',      'f',      'h',      'j',    ],   # l
     ['a',      'c',      'e',      'g',      'i',      'k'],   # r
     {
         "left": ['b','d','f','h','j',],
         "right": ['a','c','e','g','i','k']
     }),


])
def test_compare_two_list(left_list, right_list, expected_output):
    assert compare(left_list, right_list) == expected_output
