def is_monotonic(array):
    n = len(array)
    is_increasing = True
    is_decreasing = True

    for i in range(n - 1):
        if array[i] > array[i + 1]:
            is_increasing = False
        elif array[i] < array[i + 1]:
            is_decreasing = False

    return is_increasing or is_decreasing


print(is_monotonic([1, 2, 3, 4, 5]))
print(is_monotonic([5, 4, 3, 2, 1]))
print(is_monotonic([1, 2, 2, 3, 2, 4]))
