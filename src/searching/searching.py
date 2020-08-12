# TO-DO: Implement a recursive implementation of binary search

def binary_search(arr, target, start, end):
    # if starting index is less than ending index, return -1, exit out
    if start > end:
        return -1
    else:
        # This finds midpoint
        mid = (start + end) // 2
        # if target is equal to midpoint, return midpoint
        if target == arr[mid]:
            return mid
        # if target is less than midpoint, move left
        elif target < arr[mid]:
            # return binary search with midpoint - 1
            return binary_search(arr, target, start, mid-1)
        else:
            # else, move right, increase midpoint + 1
            return binary_search(arr, target, mid+1, end)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    pass
