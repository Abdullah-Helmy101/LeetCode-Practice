def binary_search(arr: list, target: int):

    low = 0
    high = len(arr) - 1

    while low <= high:

        # Calc the middle index
        mid = low + (high - low) // 2

        # Check if the middle value is the target
        if arr[mid] == target:
            return mid

        # Check if middle value is smaller than the target. If met we split the lower half.
        elif arr[mid] < target:
            low = mid + 1

        # Check if middle value is larger than the target. If met we split the upper half.
        elif arr[mid] > target:
            high = mid - 1

    return -1


if __name__ == '__main__':

    arr = [2, 3, 4, 10, 40]
    x = 4

    result = binary_search(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")