"""
    2. Write a method named smallestLargest that asks the user to enter numbers, 
    then prints the smallest and largest of all the numbers typed in by the 
    user. You may assume the user enters a valid number greater than 0 for 
    the number of numbers to read. Here is an example dialogue:   
"""

def printAverage():
    total = 0
    count = 0
    while True:
        Num = float(input("Type a number: "))
        if Num < 0:
            break
        elif Num > 0:
            #Add number if > 0
            total += Num
            count += 1
            continue
        else:
            # Calculate average if number is less than zero
            Average = total/count
            print(f"Average was {Average}")
            break
printAverage()

        
