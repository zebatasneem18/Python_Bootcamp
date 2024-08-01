def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing
    total_sum = n * (n + 1) // 2  # sum of first n natural numbers
    
    arr_sum = sum(arr)  # sum of elements in the array
    
    missing_number = total_sum - arr_sum
    
    return missing_number

# Read input and convert to list of integers
arr = list(map(int, input().split()))

missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)