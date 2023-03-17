from os.path import isdir, join

def isdir_print(path):
    if isdir(path):
        print("DIR")
    else:
        print("FILE")

def compare(left_l: list, right_l: list, path_l: str,path_r: str):
    # # Sortowanie folder first
    # list_dir1.sort(key=lambda x: isdir(join(path_dir1, x)), reverse=True)
    # list_dir2.sort(key=lambda x: isdir(join(path_dir2, x)), reverse=True)

    left_l.sort()
    right_l.sort()

    if len(left_l) < len(right_l):
        lenth_max = len(right_l)
        lenth_min = len(left_l)
    else:
        lenth_max = len(left_l)
        lenth_min = len(right_l)

    next_l = 0
    next_r = 0
    print(f"==={lenth_max}===")
    for i in range(lenth_min):

        if left_l[i+next_l] == right_l[i+next_r]:
            isdir_print(join(path_l, left_l[i+next_l]))
            print(f"SAME:       L:{left_l[i+next_l]}  R:{right_l[i+next_r]}")
        elif left_l[i+next_l] < right_l[i+next_r]:
            while left_l[i+next_l] < right_l[i+next_r]:
                isdir_print(join(path_l, left_l[i + next_l]))
                print(f"NEXT L: {left_l[i+next_l]}")
                print(i+next_l)
                print(next_l)
                next_l += 1
                print(i + next_l)
                if i+next_l >= lenth_max:
                    break
            isdir_print(join(path_l, left_l[i + next_l]))
            print(f"SAME l:       L:{left_l[i+next_l]}  R:{right_l[i+next_r]}")

        elif left_l[i+next_l] > right_l[i+next_r]:
            while left_l[i+next_l] > right_l[i+next_r]:
                isdir_print(join(path_r, right_l[i+next_r]))
                print(f"NEXT R: {right_l[i+next_r]}")
                print(i+next_r)
                print(next_r)
                next_r += 1
                print(i + next_r)
                if i+next_r >= lenth_max:
                    break
            isdir_print(join(path_r, right_l[i + next_r]))
            print(f"SAME r:       L:{left_l[i+next_l]}  R:{right_l[i+next_r]}")
        print(f"-----------------------{i}---------------------------")


def compare_two_list(list_1: list, list_2: list):

    list_1.sort()
    list_2.sort()

    min_lenght = min(len(list_1), len(list_2))

    next_r = 0
    next_l = 0

    diff_dic = {"left": [], "right": []}

    if len(list_1) == 0:
        diff_dic["right"] + list_2
    if len(list_2) == 0:
        diff_dic["left"] + list_1

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



def compare_two_list_v2(list_left: list, list_right: list):

    list_left.sort()
    list_right.sort()

    min_lenght = min(len(list_left), len(list_right))

    next_r = 0
    next_l = 0

    diff_dic = {"left": [], "right": []}

    l = 0
    r = 0

    if len(list_left) == 0:
        diff_dic["right"] += list_right
    if len(list_right) == 0:
        diff_dic["left"] += list_left

    while l < len(list_left) and r < len(list_right):
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