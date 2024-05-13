def QuickSort(array, start, end):
    if start >= end:
        return

    pivot = array[start]
    left = start + 1
    right = end

    print("Pivot:", pivot)
    print("Array before partitioning:", array[start:end + 1])

    while True:
        while left <= right and array[right] >= pivot:
            right -= 1
        while left <= right and array[left] <= pivot:
            left += 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            break

    array[start], array[right] = array[right], array[start]

    print("Array after partitioning:", array[start:end + 1])
    print("Pivot position:", right)
    print()

    QuickSort(array, start, right - 1)
    QuickSort(array, right + 1, end)


array = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Original array:")
print(array)
print()

QuickSort(array, 0, len(array) - 1)

print("Sorted array:")
print(array)
