from copy import deepcopy
from random import randint

DEBUG = False

def shuffle(arr):
    tmp_arr = deepcopy(arr)
    for i, _ in enumerate(tmp_arr):
        d = randint(0, i)
        tmp_arr[i], tmp_arr[d] = tmp_arr[d], tmp_arr[i]
        if DEBUG: print(tmp_arr)
    return tmp_arr


if __name__ == "__main__":
    assert shuffle([1, 2, 3, 4, 5, 6]) != [1, 2, 3, 4, 5, 6]
    assert set(shuffle([1, 2, 3, 4, 5, 6])) == set([1, 2, 3, 4, 5, 6])
    