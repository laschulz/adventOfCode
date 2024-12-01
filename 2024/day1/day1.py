from collections import Counter

def read_input():
    f=open("day1.txt","r")
    lines=f.readlines()
    left=[]
    right= []
    for x in lines:
        l, r = x.strip().split()
        left.append(int(l))
        right.append(int(r))
    f.close()
    assert(len(left)==len(right))
    return left, right

def part1():
    left, right = read_input()
    left.sort()
    right.sort()

    total_diff = 0
    for i in range(len(left)):
        total_diff += abs(left[i] - right[i])
    print(total_diff)

def part2():
    left, right = read_input()
    c = Counter(right)
    r_mult = dict(c.most_common())
    
    sim_score = 0
    for i in range(len(left)):
        l = left[i]
        if l in r_mult:
            sim_score += l * r_mult[l]
    print(sim_score)

part2()