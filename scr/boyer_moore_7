def boyer_moore(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    if needle_len == 0:
        return []

    shift_table = {}
    for i in range(needle_len - 1):
        shift_table[needle[i]] = needle_len - i - 1
    shift_table[needle[-1]] = needle_len

    found_indexes = []
    i = needle_len - 1
    while i < haystack_len:
        j = needle_len - 1
        k = i
        while j >= 0 and haystack[k] == needle[j]:
            k -= 1
            j -= 1
        if j == -1:
            found_indexes.append(k + 1)
        if haystack[i] in shift_table:
            i += shift_table[haystack[i]]
        else:
            i += needle_len
    return found_indexes


haystack = "abababcababcabcabc"
needle = "abc"
print(boyer_moore(haystack, needle))
