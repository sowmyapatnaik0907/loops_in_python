
number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
