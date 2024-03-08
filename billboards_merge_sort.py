def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def paint_billboards(k, t, lengths):
    sorted_lengths = merge_sort(lengths)
    painters = [0] * k

    for length in sorted_lengths:
        min_index = painters.index(min(painters))


        if min_index > 0 and painters[min_index - 1] == 0:
            min_index -= 1
        elif min_index < k - 1 and painters[min_index + 1] == 0:
            min_index += 1

        painters[min_index] += length

    return max(painters) * t


k = 10
t = 5
lengths = [10, 5, 10, 15, 10, 5, 10, 15, 20, 20, 15, 20]

print("Результат:", paint_billboards(k, t, lengths), "хвилин")
