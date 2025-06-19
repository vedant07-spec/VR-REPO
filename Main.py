# Simple Python script to greet the user

name = input("What's your name? ")
print(f"Hello, {name}! Nice to meet you.")
# Extended user profile script with file saving and loop

def create_profile():
    name = input("What's your name? ")
    age = input("How old are you? ")
    language = input("What's your favorite programming language? ")

    print("\n--- Your Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Favorite Language: {language}")
    print(f"\nNice to meet you, {name}! At {age} years old, diving into {language} is a great choice!")

    save = input("\nWould you like to save this profile? (yes/no): ").strip().lower()
    if save == "yes":
        with open("user_profiles.txt", "a") as file:
            file.write(f"{name}, {age}, {language}\n")
        print("Profile saved successfully!\n")

while True:
    create_profile()
    another = input("Do you want to enter another profile? (yes/no): ").strip().lower()
    if another != "yes":
        print("Thanks for using the profile creator!")
        break