"""
    Write a method named smallestLargest that asks the user to enter numbers, 
    then prints the smallest and largest of all the numbers typed in by the 
    user. You may assume the user enters a valid number greater than 0 for 
    the number of numbers to read. Here is an example dialogue: 
"""

def smallestLargest():
    List =[]
    Num_of_times = int(input("How many numbers do you want to enter? "))
    for x in range(Num_of_times):
        Number = int(input(f"Number {x+1}: "))
        List.append(Number)
    Smallest = min(List)
    Largest = max(List)
    print(f"Smallest = {Smallest}")
    print(f"Largest = {Largest}")
smallestLargest()