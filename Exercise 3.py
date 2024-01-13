#1
#Write a program to produce the following output using for loop

for i in range(4):
    if i % 2 == 0:
        print("+----+")
    else:
        print("\\ /")
        print("/ \\")

#2
       # Write a program to produce the following output using for loop
        for i in range(5):
             for j in range(10):
                 print("*", end="")
                 print()

#3
#Complete the code for the following for loop
for i in range(1,7):
    if i == 1:
        print("a) 1 b) 2 c) 4 d) 30 e) -7 f) 97 g) -4")
    elif i == 2:
        print("2 4 19 20 -3 94 14")
    else:
        print(i, end=" ")
        print(i * 2, end=" ")
        print(i * 15 + 4, end=" ")
        print((i - 3) * 10, end=" ")
        print(abs(i - 4), end=" ")
        print(99 - i * 3, end=" ")
        if i % 2 == 0:
            print(i * 7)
        else:
            print(i * 7 + 2)

#4
            class NumberTriangle:
                NUM_LINES = 7  # Class constant to change the number of lines in the figure
    
                def generate_triangle(self):
                    for i in range(1, self.NUM_LINES + 1):
                        for j in range(i):
                            print(i, end='')
                        print()

# Create an instance of the class and generate the triangle
            triangle = NumberTriangle()
            triangle.generate_triangle()

#5
def pay(salary, hours_worked):
    regular_hours = 8  # Define regular working hours
    overtime_multiplier = 1.5  # Overtime pay multiplier

    if hours_worked <= regular_hours:
        total_pay = salary * hours_worked  # Calculate pay for regular hours
    else:
        regular_pay = salary * regular_hours  # Calculate pay for regular hours
        overtime_pay = salary * overtime_multiplier * (hours_worked - regular_hours)  # Calculate overtime pay
        total_pay = regular_pay + overtime_pay  # Calculate total pay including overtime

    return total_pay

#6
import math

def area(radius):
    return math.pi * (radius ** 2)

#7
low = int(input("low? "))  # Prompt user for low value
high = int(input("high? "))  # Prompt user for high value
sum_result = 0

for i in range(low, high):
    sum_result += i

print("sum = ", sum_result)

#8
# Initialize variables
total = 0
num = None

# Continue prompting user for numbers until 0 is entered
while True:
    num = float(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break  # Exit the loop if 0 is entered
    total += num  # Add the entered number to the running total

# Output the sum of the entered numbers
print("The sum of the numbers entered is:", total)

#9
# Initialize variables
total = 0
num = None

# Continue prompting user for numbers until -1 is entered
while num != -1:
    num = float(input("Enter a number (enter -1 to stop): "))
    if num != -1:
        total += num  # Add the entered number to the running total

# Output the sum of the entered numbers (excluding -1)
print("The sum of the numbers entered is:", total)

#10
def repl(s, repetitions):
    if repetitions <= 0:
        return ""  # Return an empty string if repetitions is 0 or less
    else:
        return s * repetitions  # Concatenate the string 's' for 'repetitions' times

#11
    def printRange(start, end):
        if start < end:
             for i in range(start, end + 1):
                 print(i, end=" ")
        elif start > end:
              for i in range(start, end - 1, -1):
                 print(i, end=" ")
        else:
            print(start)

#12
        def smallestLargest():
            num_of_numbers = int(input("How many numbers do you want to enter? "))
    
    # Initialize variables to store smallest and largest numbers
    smallest = float('inf')  # Initialize smallest as positive infinity
    largest = float('-inf')  # Initialize largest as negative infinity
    
    for i in range(1, num_of_numbers + 1):
        num = float(input(f"Number {i}: "))
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print(f"Smallest = {smallest}")
    print(f"Largest = {largest}")

# Call the method to execute the functionality
    smallestLargest()

#13
def printAverage():
    total = 0.0
    count = 0

    while True:
        num = float(input("Type a number: "))
        if num < 0:
            if count > 0:
                average = total / count
                print(f"Average was {average:.1f}")
            else:
                print("No non-negative numbers were entered.")
            break
        else:
            total += num
            count += 1

# Call the method to execute the functionality
printAverage()

#14
def printAverage():
    total = 0.0
    count = 0

    while True:
        num = float(input("Type a number: "))
        if num < 0:
            if count > 0:
                average = total / count
                print(f"Average was {average:.1f}")
            else:
                print("No non-negative numbers were entered.")
            break
        else:
            total += num
            count += 1

# Call the method to execute the functionality
printAverage()

#15
import random

def roll_dice():
    return random.randint(1, 6)  # Simulates rolling a 6-sided die

def main():
    tries = 0
    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        print(f"{dice1} + {dice2} = {total}")
        tries += 1
        if total == 7:
            print(f"You won after {tries} tries!")
            break

if __name__ == "__main__":
    main()

