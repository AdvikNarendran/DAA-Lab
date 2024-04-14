def candies(n, arr):
    candies = [1] * n
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)

# Example usage
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(candies(n, arr)) # Output: 10
