wizard = "Wizard"
elf = "Elf"     
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

print("1)Wizard ")
print("2)Elf")
print("3)Human")

character_choice = input("Choose your character (1, 2, or 3): ")

print(f"You chose: {character_choice}")

while True:
    
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")

    
    character_choice = input("Choose your character: ")

    
    if character_choice == '1':
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break  

    elif character_choice == '2':
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break

    elif character_choice == '3':
        character = "Human"
        my_hp = human_hp
        my_damage = human_damage
        break


while True:  
    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!")

    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break  

    
    my_hp = my_hp - dragon_damage
    print(f"The Dragon damaged the {character}!")

   
    if my_hp <= 0:
        print(f"The {character} has lost the battle!")
        break  

