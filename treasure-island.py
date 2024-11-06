"""
Here we import random, for some methods where we are going to use random
"""

import random

"""
Here we made a global variable of name, age and BMI. Where we are going to used it for various things in the game
"""
name = ""
age = 0
BMI = 0.0

"""
Function for calculating BMI
"""


def calculate_bmi(weight, height):
    return weight / (height**2)


"""
This is where the game starts, asking the username their name, age and BMI
"""


def intro():
    global name, age, BMI
    print(
        "Hello, how are you? Welcome to The Treasure Island. Where you will go through a lot of difficulties, in the water, earth, air, caves, all you can imagine."
    )
    print(
        "You will need to find the treasure where the Captain Flint has died with it in his hands, so first..."
    )

    name = input("What's your name? ")
    name = name.capitalize().strip()
    age = input("What about your age? ").strip()
    age = int(age)
    weight = float(input("Put your weight in kilograms: ").strip())
    height = float(input("Put your heigh in meters: ").strip()) / 100
    BMI = calculate_bmi(weight, height)
    print(f"Your BMI is {BMI:.2f}")
    if age < 18:
        print(f"Well young {name}, let's start this journey, your story...")
    else:
        print(f"Well {name}, let's start this journey, your story...")

    choose_path()


"""
This is where the username will choose their path, between swim or walk
"""


def choose_path():
    question = input(
        "You prefer to swim or walk to explore the island? (Just put swim / walk): "
    )
    question = question.lower().strip()
    if question == "swim":
        swim_path()
    elif question == "walk":
        walk_path()
    else:
        print("Invalid input, try again")
        choose_path()


"""
Here if they choose swim path and the different options that they will encounter different obstacules
"""


def swim_path():
    swim_encounters = ["shark", "piranhas", "anaconda", "shipwrecks"]
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
        print("But you see a mountain and a cave...")
        question = (
            input(
                "Do you prefer to go to the mountain or cave? (Answer cave/mountain): "
            )
            .strip()
            .lower()
        )
        if question == "cave":
            cave_path()
        elif question == "mountain":
            mountain_path()
        else:
            print("invalid input, try again")
            swim_path()
    else:
        print("A hurricane interrupt and you die trying to find a shelter")


"""
Here if they choose walk path, where they will encounter different obstacules
"""


def walk_path():
    walk_encounters = ["mountain", "cave", "snake", "spider", "mosquitos"]
    first_encounter = random.choice(walk_encounters)
    if first_encounter == "snake":
        print(
            "When you were goign through the jungle, a snake appears from nowhere and bite you, it was a poisonous viper!"
        )
        print("Game over!")
    elif first_encounter == "mosquitos":
        print("A mosquito just bite you, later you feeling dizzed and died from an ill")
        print("Game over!")
    elif first_encounter == "spider":
        print(
            "When you were walking beside the river, you see a spider that land on your hand and bite you. Minutes later, you feel dizzed and die!"
        )
        print("Game over")
    elif first_encounter == "mountain":
        mountain_path()
    elif first_encounter == "cave":
        cave_path()
    else:
        print("Unknown input, try again")
        walk_path()


"""
Here we see the mountain path, where the BMI plays a huge role and where the function get_torch_materials_mountain is in
"""


def mountain_path():
    print(
        "Hours later from walkin, you see a gigantic mountain. You may think that there is the treasure"
    )
    print("You must escalate the mountain but let's see if your physique is capable")
    if BMI <= 24.9 and age <= 18:
        print(
            f"Well your BMI is {BMI} and your age is {age}. You are more than capable to escalete the mountain."
        )
        print("Now you must search for a torch! Let's make one!")
        get_torch_materials_mountain()
    elif BMI <= 24.9 and age > 18:
        print(
            "You are small, you try to escalate the mountain, but in the trying you fall to your death."
        )
        print("Game over")
    elif BMI <= 18.5 and age > 18:
        print(
            "You are small. You try to reach a rock and you failed in the trying. You fall to your death"
        )
        print("Game over")
    elif BMI <= 18.5 and age <= 18:
        print(
            f"Well your BMI is {BMI} and your age is {age}. You try to escalate the mountain and fall trying."
        )
        print("Game over")
    elif BMI <= 29.9 and age > 18:
        print(
            "You are small. You try to jump from a rock to another but you slept and fall to your death."
        )
        print("Game over")
    elif BMI <= 29.9 and age <= 18:
        print(
            f"Well your BMI is {BMI} and your age is {age}. You try to escalate the mountain, in the middle. You were tired and a mountain lion kill you."
        )
        print("Game over!")
    else:
        print(
            "You try to escalate, but you get tired at the try. So you walk through the jungle and you die in the darkness"
        )
        print("Game over")


"""
Here we see the cave path, where the BMI plays a huge role and where the function get_torch_materials_mountain is in
"""


def cave_path():
    print("So you are brave enough to enter the cave...")
    if BMI <= 24.9 and age <= 18:
        print(f"Well your BMI is {BMI} and your age is {age}. You fit in the cave.")
        print(
            "Now, it's very dark. You need a torch. Let's make one with the help of the moon with it light"
        )
        get_torch_materials_cave()
    elif BMI <= 24.9 and age > 18:
        print(
            "You are small, you try to reach a rock, but in the trying you fall and break your neck."
        )
        print("Game over")
    elif BMI <= 18.5 and age > 18:
        print(
            "You are small. You try to reach a stick, but in the trying you fall and break your neck."
        )
        print("Game over")
    elif BMI <= 18.5 and age <= 18:
        print(
            f"Well your BMI is {BMI} and your age is {age}. You try to fit in the entrance of the cave but you cut in the process and then you die of an ill."
        )
        print("Game over")
    elif BMI <= 29.9 and age > 18:
        print(
            "You are small. You try to jump from a rock to another but you slept and fall to your death."
        )
        print("Game over")
    elif BMI <= 29.9 and age <= 18:
        print(
            f"Well your BMI is {BMI} and your age is {age}. You try to relax in the cave but when you sit, you fall into a lake and you drown."
        )
        print("Game over!")
    else:
        print(
            "You try to fit in the entrance of the cave, but a rock fall to your head and you die."
        )
        print("Game over")


"""
Here is the materials for the torch in the cave
"""


def get_torch_materials_cave():
    cave_items = [
        "stalactites",
        "stalagmites",
        "bats",
        "limestone",
        "calcite",
        "underground pools",
        "crystals",
        "fossils",
        "moss",
        "fungi",
        "unique microorganisms",
        # Torch-specific items
        "sticks",  # Sometimes found near cave entrances
        "dry moss",  # Can be found in caves
        "bat guano",  # Highly flammable and could be used as fuel
        "flint",  # Useful for creating sparks
    ]
    require_items = {"sticks", "dry moss", "bat guano", "flint"}
    inventory = set()
    while True:
        item = random.choice(cave_items)
        response = (
            (f"Do you want to keep this {item}? (Answer yes/no): ").strip().lower()
        )

        if response == "yes":
            inventory.add(item)

        if require_items.issubset(inventory):
            print("Perfect, you grab all the neccesary items for make a torch.")
            turn_on_torch()


"""
Here is the materials for the torch in the mountain
"""


def get_torch_materials_mountain():
    mountain_items = [
        "rocks",
        "boulders",
        "trees",
        "shrubs",
        "wildlife",
        "streams",
        "snow",
        "ice",
        "minerals",
        "crystals",
        "cliffs",
        "moss",
        "fungi",
        # Torch-specific items
        "sticks",  # From trees or shrubs
        "dry moss",  # For kindling
        "resin",  # Found in some tree bark as a flammable material
        "flint",  # For striking to create sparks
    ]

    require_items = {"sticks", "dry moss", " resin", "flint"}
    inventory = set()
    """
    If the player gets the neccesary items, he can make the torch. Where he will tur on the torch
    """
    while True:
        item = random.choice(mountain_items)
        response = (
            input(f"Do you want to grab this {item}? (Answer yes/no): ").strip().lower()
        )
        if response == "yes":
            inventory.add(item)

        if require_items.issubset(inventory):
            print("Perfect, you have all the items require for making a torch")
            turn_on_torch()


"""
Here is how the user can turn on the torch, if it will work or not
"""


def turn_on_torch():
    hit_the_rocks = random.randint(1, 6)
    print("Hit the rocks so it can turn on!")
    while True:
        hit = input("Write 'hit'")
        hit = hit.lower().strip()
        if hit_the_rocks == 3 or hit_the_rocks == 5:
            print("Very good, you did it! You have a torch in fire!")
            print(
                "Now when you walk through, you see a riddle in the wall. You lean the torch and read..."
            )
            riddle_in_wall()
        else:
            print("You failed and die in the darkness")
            break

    """
    Here the player, must answer the riddle if not. He will die
    """


def riddle_in_wall():
    riddle = {
        "What has keys but cant open locks?": "piano",
        "What has to be broken before you can use it?": "egg",
        "I'm tall when I'm young and short when I'm old. What am I?": "candle",
        "What comes once in a minute, twice in a moment, but never in a thousand years?": "m",
        "What can you catch but not throw?": "cold",
        "I have branches, but no fruit, trunk, or leaves. What am I?": "bank",
        "What goes up but never comes down?": "age",
        "I'm light as a feather, yet the strongest man can't hold me for much longer than a minute. What am I?": "breath",
        "The more of this there is, the less you see. What is it?": "darkness",
        "I have many teeth, but I can't bite. What am I?": "comb",
    }
    # Here the random_riddle, will chose a key and a value of the dictionary riddle
    random_riddle, answer = random.choice(list(riddle.items()))
    question = input(f"{random_riddle}: ").strip().lower()
    if question == answer:
        print("Yes! You made it!")
        finish_game()
    else:
        print("Game over, you made a mistake.")


"""
Here is where the player finished the game and wins it
"""


def finish_game():
    print(
        f"Finally {name}, you made it and at the age of {age}. You cross the obstaclues and finally you made it. You finished this game!"
    )


intro()
