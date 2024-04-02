def sort_array(arr):
    first_swap = None
    second_swap = None
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if first_swap is None:
                first_swap = i
            else:
                second_swap = i + 1
                break
            
    arr[first_swap], arr[second_swap] = arr[second_swap], arr[first_swap]

# Example usage:
arr = [1, 5, 3, 4, 2, 6]
sort_array(arr)
print("Sorted array:", arr)
