# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0

    for k in range(0, elements):
        if i >= len(arrA):
            merged_arr[k] = arrB[j]
            j += 1
        elif j >= len(arrB):
            merged_arr[k] = arrA[i]
            i += 1
        elif arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr) // 2)
        left = arr[:mid]
        right = arr[mid:]
        print(f'{left} <-- {mid} --> {right}')

        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
