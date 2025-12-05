print("Adding Data to Dictionary")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

isContinue = True

empty_dictionary = {}

def print_anime():
    for i, a in empty_dictionary.items():
        print(f"{i} title -- {a}")

def pang_search(key):
    print("Searching... Please wait\n")
    print(f"seach shows {empty_dictionary[key].upper()} in our database")

while isContinue == True:
    key = input("Enter key for this anime : ")

    value = input("Enter anime title : ")

    empty_dictionary[key] = value

    choice = input("Would you like to continue? (y/n) : ").lower()

    if choice == "y":
        print("Continuing program...")
        continue
    elif choice == "n":
        print("Program stopped.")
        break
    elif choice == "p":
        print_anime()
        continue
    elif choice == "s":
        search = input("Enter the code name for the anime : ")
        pang_search(search)
        continue
    else:
        print("Invalid")
        continue