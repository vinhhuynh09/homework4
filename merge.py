def merge_list(list1, list2):
    # check if there are any bad inputs in the list (non integer values)
    for lists in [list1, list2]:
        if any(not isinstance(item, int) for item in lists):
            raise TypeError("List contains non-integer element(s).")

    # merge the two lists
    mergedList = list1 + list2

    # use bubble sort to sort the merged list
    n = len(mergedList)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mergedList[j] > mergedList[j + 1]:
                mergedList[j], mergedList[j + 1] = mergedList[j + 1], mergedList[j]
    return mergedList
