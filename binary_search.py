def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        quess = list[mid]
        if quess == item:
            return mid
        if quess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

binary_search(my_list, 3)
binary_search(my_list, -1)
