# Take input for name and marks
name = input("Enter your name: ")
s1, s2, s3, s4, s5 = map(int, input("Enter marks for 5 subjects separated by space: ").split())

# Calculate total marks and average
total_marks = s1 + s2 + s3 + s4 + s5
average_marks = total_marks / 5

# Print the result
print(f"Hello {name}, your total marks are {total_marks} and average is {average_marks:.2f}")
