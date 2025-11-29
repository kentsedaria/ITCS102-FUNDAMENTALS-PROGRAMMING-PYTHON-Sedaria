end = 0
for me in range(1,11):
    nb = eval(input("Put number"))
    if nb % 2 == 1:
        end += nb
print(f"The summation of all number is {end}")