total = 0

for i in range(10):
    num = eval(input("Enter a number : "))
    if num % 2 != 0:
        total += num

print("The sum of odd number is", total)