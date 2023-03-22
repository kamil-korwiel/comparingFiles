from os.path import isdir, join
import os

def isdir_print(path):
    if isdir(path):
        print("DIR")
    else:
        print("FILE")

def isdir_operation(path):
    if isdir(path):
        pass
        # diff = compare()
        # if diff is empty
            # return
        # else
            # copy(diff,path,target_folder_path)
    else:
        return


def copy_print(copy_form:str,copy_to:str,c):
    print(' '*c*2 + f"COPY FROM: {copy_form}")
    print(' '*c*2 + f"COPY TO: {copy_to}")


def compare(list_left: list, list_right: list):

    list_left.sort()
    list_right.sort()

    diff_dic = {"left": [], "right": []}

    l = 0
    r = 0

    while l < len(list_left) or r < len(list_right):
        if l >= len(list_left):
            diff_dic["right"] += list_right[r:]
            break
        if r >= len(list_right):
            diff_dic["left"] += list_left[l:]
            break
        if list_left[l] == list_right[r]:
            print(f"SAME: {list_left[l]}  <-->  {list_right[r]}")
            l += 1
            r += 1
        elif list_left[l] < list_right[r]:
            print(f"ONLY LEFT: {list_left[l]}")
            diff_dic["left"].append(list_left[l])
            l += 1
        elif list_left[l] > list_right[r]:
            print(f"ONLY RIGHT: {list_right[r]}")
            diff_dic["right"].append(list_right[r])
            r += 1

    return diff_dic


def compare_and_copy(path_l: str, path_r: str, target_path: str, c: int):
    list_left = os.listdir(path_l)
    list_right = os.listdir(path_r)

    list_left.sort()
    list_right.sort()

    # diff_dic = {"left": [], "right": []}

    l = 0
    r = 0

    while l < len(list_left) or r < len(list_right):
        if l >= len(list_left):
            # diff_dic["right"] += list_right[r:]
            break
        if r >= len(list_right):
            # diff_dic["left"] += list_left[l:]
            break
        if list_left[l] == list_right[r]:
            # isdir_print(join(path_l, list_left[l]))
            # print(' '*c*2 + f"SAME: {list_left[l]}  <-->  {list_right[r]}")
            if isdir(join(path_l, list_left[l])):
                tmpath_l = join(path_l, list_left[l])
                tmpath_r = join(path_r, list_right[r])
                tmtarget_path = join(target_path, list_left[l])
                print(' '*(c+1)*2 + f"{list_left[l]}")
                compare_and_copy(tmpath_l, tmpath_r, tmtarget_path, c+1)
            l += 1
            r += 1
        elif list_left[l] < list_right[r]:
            tmpath = join(path_l, list_left[l])
            # isdir_print(tmpath)

            print(' '*c*2 + f"ONLY LEFT: {list_left[l]}")
            target_path
            copy_print(tmpath, target_path, c)
            # diff_dic["left"].append(list_left[l])
            l += 1
        elif list_left[l] > list_right[r]:
            tmpath = join(path_r, list_right[r])
            # isdir_print(tmpath)

            print(' '*c*2 + f"ONLY RIGHT: {list_right[r]}")
            copy_print(tmpath, target_path, c)
            # diff_dic["right"].append(list_right[r])
            r += 1
    print(' '*c*2 + "------------------------------------------------")
    return
    # return diff_dic
