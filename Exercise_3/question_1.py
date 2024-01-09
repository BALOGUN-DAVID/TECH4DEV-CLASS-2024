# max = 0
# List = [2,4,7,4,23,5,99,1,4,8,9, 56]
# for x in List:
#     if max == 0:
#         max = x
#     elif x > max:
#         max = x
# print(max)



List = [2,4,7,4,23,5,99,1,4,8,9, 56]
maximum = List[0]
for X in List:
    if X > maximum:
        maximum = X
print(f"The maximum value is {maximum}")

