import attributeGenerator
import characterSheetGenerator

'''  ============================ INFO ============================

character creator is a seperate class than the character class
reasoning for this is as to not clutter the character object with code
that is only needed at beggining of character creation.

     ============================ INFO ============================  '''

class CharacterCreator:
    

    def __init__(self):
        self.name, self.skills , self.traits = None , None , None
        self.randomise(False,False) # generates default values
    
    def randomise(self,KEEP_NAME: bool, KEEP_SKILLS_AND_TRAITS: bool):

        if not KEEP_NAME:
            self.name = attributeGenerator.generateName()
        
        if not KEEP_SKILLS_AND_TRAITS:
            self.skills,self.traits = characterSheetGenerator.generateSkillsAndTraits()
    
    def __str__(self):
        return f"\n====================\nName: {self.name}\nSkills: {self.skills}\nTraits: {self.traits}\n===================="

if __name__ == "__main__":
    TEST_ITERATION_NUM = 5
    characterCreationInstance = CharacterCreator()

    for i in range(TEST_ITERATION_NUM):
        characterCreationInstance.randomise(False,False)
        print(characterCreationInstance)
