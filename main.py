import os
from os.path import isdir, join
from utility import compare, compare_and_copy


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
    path = "C:/Users/k.korwiel/Desktop/P2P5CompareThisFiles"
    path_dir_r = join(path, 'Clean')
    path_dir_l = join(path, 'PoUpgradzie')
    path_dir_target = join(path, 'TARGET')

    diff_dic = compare_and_copy(path_dir_l, path_dir_r,path_dir_target,0)

    print(diff_dic)


if __name__ == '__main__':
    main()
