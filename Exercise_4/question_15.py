import random

number_of_tries = 0
while True:
    first = random.randint(1,6)
    second = random.randint(1,6)
    sum = first + second
    print(f"{first} + {second} = {sum}") 
    if sum == 7:
        break
    number_of_tries += 1
print(f"You won after {number_of_tries} tries")
