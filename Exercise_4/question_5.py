def pay(salary, hours):
    if hours > 8:
       amount_received = (salary * 8) +6*(hours-8)
       print(amount_received)
    else:
        amount_received = salary * hours
        print(amount_received)
pay(4, 11)
