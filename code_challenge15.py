animelist = []
isContinue = True
print("Welcome to Anime Lister!\nEnter 'exit' to stop.")

while isContinue == True:
    anime = input("Enter your favorite anime: ")

    if anime.lower() == "exit":
        print("\nHere is your list of favorite anime:")
        break

    animelist.append(anime)
    print(f"{anime} has been added to your anime list.")

for i in animelist:
    print(f"- {i}")