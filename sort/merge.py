import random

def merge_arrays(left, right):
    res = []
    i, j  = 0,0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res + left[i:] + right[j:]

def merge_sort(array):
    if len(array) == 1:
        return array
    min_idx = len(array)//2
    left = array[:min_idx]
    right = array[min_idx:]
    return merge_arrays(merge_sort(left), merge_sort(right))
