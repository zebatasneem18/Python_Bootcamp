def find_missing_number(arr):
    n = 50  # Since the sequence is from 1 to 50
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    
    arr_sum = sum(arr)  # Sum of elements in the array
    
    missing_number = total_sum - arr_sum
    return missing_number

# Read input and convert to list of integers
arr = list(map(int, input().split()))

missing_number = find_missing_number(arr)
print("The missing number between 1 and 50 is:", missing_number)
