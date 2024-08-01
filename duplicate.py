def find_duplicates(arr):
    duplicates = []
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element has already been identified as a duplicate
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            duplicates.append(abs(arr[i]))
    
    return duplicates

# Example usage:
arr = [1, 2, 3, 4, 5, 2, 7, 8, 4, 10, 5]
duplicates = find_duplicates(arr)
print("Duplicates in the array:", duplicates)
