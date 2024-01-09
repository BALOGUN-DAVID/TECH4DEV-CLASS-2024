low = int(input("Enter a low number: "))
high = int(input("Enter a high number: "))
Sum = 0
# Loop through the values
for i in range(low, high):
    # Add each value to the sum
    Sum += i
print("Sum =",Sum)