import random

swim_encounters = ["shark", "piranhas", "anaconda", "shipwrecks"]
walk_encounters = ["mountain", "cave", "snake", "spider", "mosquitos"]

print(
    "Hello, how are you? Welcome to The Treasure Island. Where you will go through a lot of difficulties, in the water, earth, air, caves, all you can imagine."
)
print(
    "You will need to find the treasure where the Captain Flint has died with it in his hands, so first..."
)

name = input("What's your name?")
name = name.capitalize().strip()
age = input("What about your age?")
age = int(age)

if age < 18:
    print(f"Well young {name}, let's start this journey, your story...")
else:
    print(f"Well {name}, let's start this journey, your story...")

question = input(
    "You prefer to swim or walk to explore the island? (Just put swim / talk)"
)

question = question.lower().strip()

if question == "swim":
    print("So you prefer to swim... I must say that you are a brave person")
    first_encounter = random.choice(swim_encounters)
    if first_encounter == "shark":
        print("The shark attacks and you lost an arm, later you died by bled")
        print("Game over!")
    elif first_encounter == "piranhas":
        print(
            "While you swim, you didn't notice the fishes around your feet. By the moment that you realised, it was to late. The piranhas already ate you!"
        )
        print("Game over!")
    elif first_encounter == "anaconda":
        print(
            "You encounter a giant anaconda, when you want to back. It was to late, the anaconda slide through your body and destroy it"
        )
        print("Game over!")
    elif first_encounter == "shipwrecks":
        print(
            "Yes! You finally see the shipwrecks, is a good sign. You approach to investigate them"
        )
    else:
        print("A hurricane interrupt and you die in the try to find a shelter")

if question == "walk":
    print("So you choose to walk, that a smart decision. Now go through the jungle")
    first_encounter = random.choice(walk_encounters)
