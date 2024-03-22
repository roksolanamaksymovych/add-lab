def is_monotonic(array):
    n = len(array)
    is_increasing = True
    is_decreasing = True

    for i in range(n - 1):
        if array[i] > array[i + 1]:
            is_increasing = False
        elif array[i] < array[i + 1]:
            is_decreasing = False
        if not is_increasing and not is_decreasing:
            return False

    return is_increasing or is_decreasing


print(is_monotonic([2,2,2,2,2]))
print(is_monotonic([2,2,2,2,3]))
print(is_monotonic([2,2,2,2,1]))