name = input("Hi! What is your name --> ")
print("++++++++++++++++++++++++++++++++++")
print("ODD number compiler, type '0' to terminate")

sum = 0
odd = ""
ge = True

while ge == True:
    num = eval(input("Please input a number --> "))

    if num % 2 == 1:
        print("ODD number detectted")
        odd += str(num) + ","
        sum += num
    elif num == 0:
        print("Loop Terminated")
        break
    else:
        if num % 2 == 0:
            print("EVEN number detected, skipping...")
        else:
            print("invalid number ")
            continue

print(f"Hi {name}, The sum of all ODD number is {sum}")
print(f"ALL the ODD numbers you inputted are {odd}")