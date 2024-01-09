sum = 0
while True:
    # Prompt user to enter number
    Number = int(input("Enter a number: "))
    if Number != -1:
        # Add the entered number to the sum
        sum += Number
        continue
    else: 
        # Exits program if -1 is entered
        break
print(f"The sum of the numbers is: {sum}")