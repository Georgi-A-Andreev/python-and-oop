def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort() for the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from both halves and add the smaller one to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add the remaining elements from the unfinished half
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


arr = [int(x) for x in input().split()]

result = merge_sort(arr)
print(' '.join(str(x) for x in result))
