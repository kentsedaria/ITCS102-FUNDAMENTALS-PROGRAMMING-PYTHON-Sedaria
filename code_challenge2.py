amount = eval(input("Enter amount to Deposit - ->"))

print("\nHere is a breakdown, using PH denomination:")

n1 = 100000
n2 = 10000
n3 = 1000
n4 = 500
n5 = 200
n6 = 100
n7 = 50
n8 = 20
n9 = 10
n10 =5
n11 =1

denominations = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11]

for denom in denominations:
    count = amount // denom
    amount %= denom
    print(f"{count} = ₱{denom}")