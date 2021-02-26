
def quick_sort(array):
    if array == []:
        return array
    p = array[-1]
    left = []
    right = []
    pivots = []
    for v in array:
        if v < p:
            left.append(v)
        elif v == p:
            pivots.append(v)
        else:
            right.append(v)
    return quick_sort(left) + pivots + quick_sort(right)

import random
a = [random.randint(0, 99) for i in range(20)]
print(a)
print(quick_sort(a))
