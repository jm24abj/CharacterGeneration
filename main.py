from generationUtils import CharacterCreator

# Holds GUI for the project

def run():
    finishedGenerating = False
    character = CharacterCreator.CharacterCreator()

    while not finishedGenerating:
        print(character)

        option = -1

        while option < 1 or option > 5: 
            print("Select an option\n1. re-roll all\n2. re-roll name\n3. re-roll character sheet\n4. enter custom name\n5. finish")
            option = int(input("Input: "))

        
            if option == 1:
                character.randomise(False,False)
            elif option == 2:
                character.randomise(False,True)
            elif option == 3:
                character.randomise(True,False)
            elif option == 4:
                newName = input("\nEnter a new name for your character: ")
                character.setCustomName(newName)
            elif option == 5:
                finishedGenerating = True
            else:
                print("\nnot a valid option!")

if __name__ == "__main__":
    run()