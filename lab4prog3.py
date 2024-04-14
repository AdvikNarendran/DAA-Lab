import itertools

def min_sum_of_products_brute_force(array_one, array_two):
    min_sum = float('inf')
    
    # Generate all permutations of array_one
    permutations = itertools.permutations(array_one)
    
    # Iterate through each permutation
    for perm in permutations:
        current_sum = sum(perm[i] * array_two[i] for i in range(len(array_one)))
        min_sum = min(min_sum, current_sum)
    
    return min_sum

# Example usage
array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
min_sum_brute_force = min_sum_of_products_brute_force(array_one, array_two)
print("Minimum sum of products (brute force):", min_sum_brute_force)



#time complexity nlogn

def min_sum_of_products_optimized(array_one, array_two):
    # Sort both arrays
    array_one.sort()
    array_two.sort(reverse=True)
    
    # Calculate the sum of products
    min_sum = sum(array_one[i] * array_two[i] for i in range(len(array_one)))
    
    return min_sum

# Example usage
array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
min_sum_optimized = min_sum_of_products_optimized(array_one, array_two)
print("Minimum sum of products (optimized):", min_sum_optimized)
