import os
from os.path import isdir, join
from utility import compare


def compare_using_set(path_dir1: str, path_dir2: str):
    list_dir1 = os.listdir(path_dir1)
    list_dir2 = os.listdir(path_dir2)

    diff = list(set(list_dir1) - set(list_dir2))
    print(diff)


def list_dir(path: str) -> list:
    return os.listdir(path)


def recursive_list_dir(path: str):
    pass


def compare_two_list(list_1: list, list_2: list):

    list_1.sort()
    list_2.sort()

    min_lenght = min(len(list_1), len(list_2))

    next_r = 0
    next_l = 0

    diff_dic = {"left": [], "right": []}

    for i in range(min_lenght):
        print(f"---------------- {i} ------------------")
        while True:
            if list_1[i+next_l] == list_2[i+next_r]:
                print(f"SAME: {list_1[i+next_l]}  <-->  {list_2[i+next_r]}")
                break
            elif list_1[i+next_l] < list_2[i+next_r]:
                print(f"ONLY LEFT: {list_1[i+next_l]}")
                diff_dic["left"].append(list_1[i+next_l])
                next_l += 1
            elif list_1[i + next_l] > list_2[i + next_r]:
                print(f"ONLY RIGHT: {list_2[i + next_r]}")
                diff_dic["right"].append(list_2[i + next_r])
                next_r += 1

            if not i+next_l < len(list_1):
                print(f"ALL RIGHT: {list_2[i + next_r:]}")
                diff_dic["right"] += list_2[i + next_r:]
                break
            if not i+next_r < len(list_2):
                print(f"ALL LEFT: {list_1[i + next_l:]}")
                diff_dic["left"] += list_1[i + next_l:]
                break
    return diff_dic


def main():

    # path = "C:/Users/k.korwiel/Desktop/P2P5CompareThisFiles"
    # path_dir_L = join( path, 'PrzedUpgradem' )
    # path_dir_R = join( path, 'Clean' )
    #
    # list_dir_L = os.listdir(path_dir_L)
    # list_dir_R = os.listdir(path_dir_R)
    #
    #
    # compare(list_dir_L, list_dir_R,path_dir_L, path_dir_R)

    l1 = ['a', 'b', 'c', 'd', 'h', 'i', 'j', 'k']
    l2 = ['a', 'b', 'g']

    result_dic = compare_two_list(l1, l2)
    print("============================")
    print(result_dic)


if __name__ == '__main__':
    main()

