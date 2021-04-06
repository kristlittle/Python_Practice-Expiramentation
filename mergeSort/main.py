from merge_Sort import MergeSort


def isSorted(numbers):
    last_Number = float("-inf")
    in_Order = True

    for n in numbers:
        if n < last_Number:
            in_Order = False
            break
        last_Number

    return in_Order

def contain_match_ints(arr1, arr2):
    for i in arr1:
        found = False
        for j in arr2:
            if i == j:
                found = True
                break
        if not found:
            return False

    return True


def main():
    #original array
    original = [123, 6, 4, 41, 324143, -12345, -98, 123, 5234, 789,-134, 42363,
    342, 2414, 4121, 12, 13451, 123, 41, 4, 6]

    numbers = original[:]

    mergeSort = MergeSort(numbers)

    output = mergeSort.sort()

    if isSorted(output):
        print("**Awesome JOB!!**")
    else:
        print("**Uh oh - not sorted, try again!!**")

    if contain_match_ints(original, numbers):
        print("** Contains MATCHING ELEMENTS!!**")
    else:
        print("** Uh - OH - Something is MISSING!!**")

    print(output)

if __name__ == "__main__":
    main()