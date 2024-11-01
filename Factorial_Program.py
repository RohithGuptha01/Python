n = int(input("Enter Any Number : "))

fact = 1

if n < 0:
    print("Enter any Positive Number")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print(f"factorial of {n} is {fact}")
