import genUtils.attributeGenerator as attributeGenerator
import genUtils.skillsGenerator as skillsGenerator

'''  ============================ INFO ============================

character creator is a seperate class than the character class
reasoning for this is as to not clutter the character object with code
that is only needed at beggining of character creation.

     ============================ INFO ============================  '''

MAX_START_TRAITS = 3
MAX_SKILL_POINTS = 10
NAME_LIST = [
    "Alice", "Benjamin", "Chloe", "Daniel", "Emma",
    "Finn", "Grace", "Henry", "Isla", "Jack",
    "Lily", "Mason", "Nora", "Oliver", "Poppy",
    "Quinn", "Ruby", "Samuel", "Tara", "Uma",
    "Violet", "William", "Xavier", "Yara", "Zoe"
]

class CharacterCreator:
    

    def __init__(self):
        pass
    
    def randomise(KEEP_NAME: bool, KEEP_SKILLS_AND_TRAITS: bool):

        if not KEEP_NAME:
            pass
        if not KEEP_SKILLS_AND_TRAITS:
            pass
