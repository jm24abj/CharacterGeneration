from generationUtils import attributeGenerator
from generationUtils import skillsGenerator

'''  ============================ INFO ============================

character creator is a seperate class than the character class
reasoning for this is as to not clutter the character object with code
that is only needed at beggining of character creation.

     ============================ INFO ============================  '''

class CharacterCreator:
    

    def __init__(self):
        self.name,self.skills,self.traits = self.randomise(False,False)
    
    def randomise(KEEP_NAME: bool, KEEP_SKILLS_AND_TRAITS: bool):

        if KEEP_NAME and KEEP_SKILLS_AND_TRAITS:
            return
        elif not KEEP_NAME and KEEP_SKILLS_AND_TRAITS:
            newName = attributeGenerator.generateName()
            print(newName)
        if not KEEP_SKILLS_AND_TRAITS and KEEP_NAME:
            pass
        else:
            pass

if __name__ == "__main__":
    print(attributeGenerator.selectSkill())