# lab2.py
import random

weapons= ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    rollDice= random.randint(1,6)
    weaponRoll= rollDice
    heroCombat=10
    CombatStrength= heroCombat+weaponRoll
    selectedWeapon=weapons[weaponRoll-1]

    print(f"You rolled {weaponRoll}, so your weapon is {selectedWeapon}")
    print(f"You have {CombatStrength} points of combat strength")

    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend!")

    if selectedWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist....")

except Exception as e:
    print(f"Something went wrong: {e}")

