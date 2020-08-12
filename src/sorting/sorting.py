# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # holds current index, start at 0 cos smallest ends of both lists will be at the beginning since both lists are in sorted order
    i = 0
    j = 0

    # Store length of the two inputs in new variable to avoid repetition
    len1 = len(arrA)
    len2 = len(arrB)

    # This will be final output list
    arr = []

    # While loop will continue iterating until all elements are done
    while (i < len1) and (j < len2):
        # Compare elements at top of each list and append whichever is smaller to merged list
        if(arrA[i] < arrB[j]):
            arr.append(arrA[i])
            # Increment the index from list we pulled from to prevent writing the same element onto the merge list again
            i += 1
        else:
            arr.append(arrB[j])
            j += 1

    # Extend merged list with whichever of the two lists that wasn't used up inside while loop
    if i == len1:
        arr.extend(arrB[j:])
    else:
        arr.extend(arrA[i:])
    return arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # List with only 1 element or less, is already sorted.
    if len(arr) <= 1:
        return arr

    # this variable is to avoid repetition
    # Takes length of our input and divides it by 2
    l = len(arr)//2

    # List is now divided in 2, we can call merge_sort recursively on each half
    arrA = merge_sort(arr[:l])  # :l passes in the first half of the list
    # :l passes in the second half of the list
    arrB = merge_sort(arr[l:])

    # use merge function to merge the two lists
    arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
