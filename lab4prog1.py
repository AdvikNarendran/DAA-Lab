def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratio for each item
    for item in items:
        item.append(item[0] / item[1])

    # Sort items based on value-to-weight ratio in non-increasing order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item[1]:
            # If the item fits entirely into the knapsack, take the whole item
            knapsack.append((item[0], item[1]))
            total_value += item[0]
            capacity -= item[1]
        else:
            # If only a fraction of the item fits into the knapsack, take that fraction
            fraction = capacity / item[1]
            knapsack.append((item[0] * fraction, item[1] * fraction))
            total_value += item[0] * fraction
            break

    return total_value, knapsack

# Example usage
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50

optimal_value, optimal_knapsack = fractional_knapsack(items, capacity)

print("Optimal value:", optimal_value)
print("Optimal knapsack:", optimal_knapsack)
