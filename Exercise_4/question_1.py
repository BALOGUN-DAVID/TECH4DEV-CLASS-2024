for x in range(8):
    if x == 0 or x == 7:
        print("+----+")
    elif x%2 == 1:
        print("\    /")
    else:
        print("/    \\")