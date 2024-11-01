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
weight_in_kilograms = input("Put your weight in kilograms: ").strip()
height_in_meters = input("Put your heigh in meters: ")

weight_in_kilograms = float(weight_in_kilograms)
height_in_meters = float(height_in_meters) / 100

BMI = weight_in_kilograms / (height_in_meters**2)


if age < 18:
    print(f"Well young {name}, let's start this journey, your story...")
else:
    print(f"Well {name}, let's start this journey, your story...")

question = input(
    "You prefer to swim or walk to explore the island? (Just put swim / walk)"
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
        print("A hurricane interrupt and you die trying to find a shelter")

if question == "walk":
    print("So you choose to walk, that a smart decision. Now go through the jungle")
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
        print(
            "Hours later from walkin, you see a gigantic mountain. You may think that there is the treasure"
        )
        print(
            "You must escalate the mountain but let's see if your physique is capable"
        )
        if BMI <= 24.9 and age <= 18:
            print(
                f"Well your BMI is {BMI} and your age is {age}. You are more than capable to escalete the mountain."
            )
            print("Now you must search for a torch! Let's make one!")
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
    elif first_encounter == "cave":
        print("So you are brave enough to enter the cave")
        if BMI <= 24.9 and age <= 18:
            print(f"Well your BMI is {BMI} and your age is {age}. You fit in the cave.")
            print(
                "Now, it's very dark. You need a torch. Let's make one with the help of the moon with it light"
            )
            get_stick = input(
                "While you are looking around the cave, you saw a stick. Do you grab it?: (answer yes/no)"
            )
            get_stick = get_stick.lower().strip()
            print("You grab the stick")
            get_plant_fiber = input(
                "While you are looking for something flammable, you look at a plant fiber. Do you grab it? (yes/no)"
            )
            get_plant_fiber = get_plant_fiber.lower().strip()
            get_ancient_rope = input(
                "As a mere miracle, you saw an abandon rope. You approach, what will you do? Grab it? (yes/no)"
            )
            get_ancient_rope = get_ancient_rope.lower().strip()
            get_oil = input(
                "You saw a little bottle of oil in the corner. You saw it a little strange. Do you grab it? (yes/no)"
            )
            get_oil = get_oil.lower().strip()
            question_of_wrap = input(
                "As you look confused, do you wrap it with the plant fiber or the rope? (fiber/rope) "
            )
            if question_of_wrap == "fiber":
                print(
                    "Perfect, you make the right decision, you wrap the stick with the fiber and then you tie it with the rope"
                )
                print(
                    "And as is a light of hope, you saw two rocks. You take them and start hitting each other to create fire."
                )

                def turn_on_torch():
                    hit_the_rocks = random.randint(1, 6)
                    print("Hit the rocks so it can turn on!")
                    while True:
                        hit = input("Write 'hit'")
                        hit = hit.lower().strip()
                        if hit_the_rocks == 3 or hit_the_rocks == 5:
                            print("Very good, you did it! You have a torch in fire!")
                        else:
                            print("You failed and die in the darkness")
                        break

                turn_on_torch()
            if question_of_wrap == "rope":
                print(
                    "Well you wrap it in rope, then you tie it with the fiber but it's not that strong. And you lost the fiber, now you are lost in the darkness and cold."
                )
                print("Game over")
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
