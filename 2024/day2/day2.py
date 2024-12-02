import numpy as np
def part1():
    f=open("day2.txt","r")
    lines=f.readlines()
    safe = 0
    for x in lines:
        nums = np.array(x.split(), dtype=int)
        diffs = np.diff(nums)
        is_increasing = diffs[0] > 0
        is_safe = all(1 <= abs(d) <= 3 and ((d > 0) == is_increasing) for d in diffs)
        safe += is_safe

    f.close()
    print(safe)

def remove_elem_safe(nums, i):
    nums1 = np.delete(nums, i)
    diffs1 = np.diff(nums1)
    is_increasing = diffs1[0]>0
    is_safe1 = all(1 <= abs(d) <= 3 and ((d > 0) == is_increasing) for d in diffs1)
    return is_safe1

def part2():
    f=open("day2.txt","r")
    lines=f.readlines()
    safe = 0
    for x in lines:
        nums = np.array(x.split(), dtype=int)
        diffs = np.diff(nums)
        is_increasing = diffs[0] > 0
        holds_cond = [1 <= abs(d) <= 3 and ((d > 0) == is_increasing) for d in diffs]
        if all(holds_cond):
            is_safe = 1
        else:
            i = np.argmin(holds_cond)
            is_safe1 = remove_elem_safe(nums, i)
            is_safe2 = remove_elem_safe(nums, 0)
            is_safe3 = remove_elem_safe(nums, i+1)
            is_safe = max(is_safe1, is_safe2, is_safe3)

        safe += is_safe
    f.close()
    print(safe)

#adjust to which part you need
part2()