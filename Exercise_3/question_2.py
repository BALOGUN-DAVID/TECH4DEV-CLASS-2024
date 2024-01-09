# 2. Write a program that calculates the average value of the given list.
# Try your program with the following list
# 4 7 1 5 11 53 12 46 84 23

List = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]
Sum = 0
count = 0
for avg in List:
    count += 1
    Sum += avg
    average = Sum / count
print(f"The average value {average}")

