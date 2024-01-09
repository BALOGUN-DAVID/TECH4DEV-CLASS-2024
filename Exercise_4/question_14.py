"""
    Write a method named numUnique that takes three integers as parameters 
    and returns the number of unique integers among the three. For example, 
    the call numUnique(18, 3, 4) should return 3 because the parameters 
    have three different values. By contrast, the call numUnique(6, 7, 6) 
    should return 2 because there are only two unique numbers among the 
    three parameters: 6 and 7.
"""

def numUnique(num1,num2,num3):
    List = [num1,num2,num3]
    Unique_values = set(List)
    Number = len(Unique_values)
    print(f"{Number} unique values")
numUnique(6,7,6)

