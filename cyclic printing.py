#cyclic printing
k = int(input())  # Read integer input k
arr = list(map(int, input().split()))  # Read array of integers from input
n = len(arr)  # Length of the array

p = k - n  # Calculate the adjusted index

if k < n:
    print(arr[k])  # If k is within bounds of the array, directly print arr[k]
else:
    print(arr[p])  # If k is greater than or equal to n, print arr[p]
