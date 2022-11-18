def merge(arr, temp, left, mid, right):
    count = 0
    i, j, k = left, mid, left
    while (i<= mid - 1) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            count += (mid - i)
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return count
def mergeSort(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mergeSort(arr, temp, left, mid)
        count += mergeSort(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid + 1, right)
    return count
def countSwaps(arr):
    n = len(arr)
    temp = [0] * n
    return mergeSort(arr, temp, 0, n - 1)
N = int(input())
arr = list(map(int, input().split()))
print(countSwaps(arr))