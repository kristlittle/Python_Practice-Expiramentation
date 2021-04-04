"""
GENERATES SUBSETS
"""
#SYS - system specific parameters & functions
import sys


def is_Sol(k,n):
    return k == n

"""
def construction():
    return[0, 1]

def process_sol(working_Pair):
    global solution

    s = {k for k in working_Pair if working_Pair[k] == 1}
    solution.append(s)

def backtracking(working_Pair, k, n):

    if is_Sol(k,n):
        process_sol(working_Pair)
    else:
        k += 1
        numbers = construct_Nums()
        for i in numbers:
            working_Pair[k] = i
            backtracking(working_Pair, k, n)
"""

def backtrack_compact(working_set, k, n):
    global solutions

    if k == n:
        s = {k for k in working_set if working_set[k] == 1}
        solutions.append(s)
    else:
        k += 1
        for i in [0, 1]:
            working_set[k] = i
            backtrack_compact(working_set, k, n)

def main():
    if 0 < 1 < len(sys.argv):
        n = int(sys.argv[1])
    else:
        exit('Usage: subsets.py number')

    global solutions
    solutions = []

    # backtrack({}, 0, n)
    # print(solutions)

    backtrack_compact({}, 0, n)
    print(solutions)
    print('Number of subsets: {}'.format(len(solutions)))


if __name__ == '__main__':
    main()


