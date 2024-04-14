#bruteforce
import itertools

def maximize_sum_brute_force(arr):
    max_sum = float('-inf')
    n = len(arr)
    
    # Generate all permutations of the array elements
    permutations = itertools.permutations(arr)
    
    # Iterate through each permutation and calculate the sum
    for perm in permutations:
        current_sum = sum(perm[i] * i for i in range(n))
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
arr = [3, 5, 6, 1]
maximized_sum_brute_force = maximize_sum_brute_force(arr)
print("Maximized sum (brute force):", maximized_sum_brute_force)



#time complexity nlogn
def max_sum(arr):
    arr.sort()
    # Calculate the sum of arr[i] * i for each element
    total_sum = sum(arr[i] * i for i in range(len(arr)))

    return total_sum

# Example usage
arr = [3, 5, 6, 1]
print("Maximum sum:", max_sum(arr))
