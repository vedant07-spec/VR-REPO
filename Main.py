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
        import json
from datetime import datetime

def is_valid_age(age):
    return age.isdigit() and 0 < int(age) < 120

def create_profile():
    name = input("What's your name? ")
    
    # Age validation
    while True:
        age = input("How old are you? ")
        if is_valid_age(age):
            break
        else:
            print("Please enter a valid age (number between 1 and 120).")
    
    language = input("What's your favorite programming language? ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    profile = {
        "name": name,
        "age": int(age),
        "language": language,
        "created_at": timestamp
    }

    print("\n--- Your Profile ---")
    print(json.dumps(profile, indent=4))

    save = input("\nWould you like to save this profile to JSON? (yes/no): ").strip().lower()
    if save == "yes":
        try:
            with open("user_profiles.json", "r") as file:
                profiles = json.load(file)
        except FileNotFoundError:
            profiles = []

        profiles.append(profile)

        with open("user_profiles.json", "w") as file:
            json.dump(profiles, file, indent=4)

        print("Profile saved to user_profiles.json!\n")

while True:
    create_profile()
    another = input("Do you want to enter another profile? (yes/no): ").strip().lower()
    if another != "yes":
        print("Thanks for using the profile creator!")
        break