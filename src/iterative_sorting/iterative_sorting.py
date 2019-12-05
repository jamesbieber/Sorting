# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        for j in range(i + 1, len(arr) - 1):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp
        # for j in range(i + 1, len(arr) - 1):
        #     if arr[j] < arr[smallest_index]:
        #         smallest_index = j

        # temp = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = temp
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
