def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[:k]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)
    return []

def findKLargest(arr, k):
    if k <= 0 or k > len(arr):
        return "Invalid value of K"
    return quickselect(arr, 0, len(arr) - 1, len(arr) - k)

# Example usage:
arr = [3, 10, 4, 7, 1, 9, 5]
k = 3
print("K largest elements:", findKLargest(arr, k))
