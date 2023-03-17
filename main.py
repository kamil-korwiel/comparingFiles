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

