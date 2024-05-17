def min_square_size(n, w, h):
    min_side = 1
    max_side = max(w, h) * n
    while min_side < max_side:
        mid = (min_side + max_side) // 2
        if check_capacity(w, h, n, mid):
            max_side = mid
        else:
            min_side = mid + 1
    return min_side


def check_capacity(w, h, n, x):
    val = (x // w) * (x // h)
    return val >= n


w = 2
h = 3
n = 10
print(min_square_size(n, w, h))
