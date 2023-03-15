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


