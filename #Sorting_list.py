# List to be sorted
list = [6, 0, 3, 5, 7, 4, 2]

# Bubble sort logic
n = len(list)

# Perform the sort, but print after each full pass
for i in range(n - 1):
    # Flag to detect if a swap happened
    swapped = False

    # Compare adjacent elements
    for j in range(n - 1 - i):
        if list[j] > list[j + 1]:  # Swap if out of order
            list[j], list[j + 1] = list[j + 1], list[j]
            swapped = True

    # Print the list after each full pass
    print(f"Pass {i + 1}: {list}")

    # If no swaps occurred, the list is sorted
    if not swapped:
        break