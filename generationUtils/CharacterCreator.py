import random
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
            self.name = self.generateName()
        
        if not KEEP_SKILLS_AND_TRAITS:
            self.skills,self.traits = self.generateSkillsAndTraits()

    def generateName(self):
        NAME_LIST = [
            "Alice", "Benjamin", "Chloe", "Daniel", "Emma",
            "Finn", "Grace", "Henry", "Isla", "Jack",
            "Lily", "Mason", "Nora", "Oliver", "Poppy",
            "Quinn", "Ruby", "Samuel", "Tara", "Uma",
            "Violet", "William", "Xavier", "Yara", "Zoe"
        ]

        return NAME_LIST[random.randint(0,len(NAME_LIST)-1)]
        

    def selectSkill(self):
        return ""

    def generateAttributes(skillPoints,maxSkills):
        while skillPoints != 0 and maxSkills > 0:
            pass
   
    def setCustomName(self,name : str):
        self.name = name

    def generateSkills(self):
        return ""

    def generateTraits(self):
        return ""

    def generateSkillsAndTraits(self):
        return self.generateSkills(),self.generateTraits()
    
    def finishCustomisation(self) -> tuple :
        return self.name,self.skills,self.traits

    def __str__(self):
        return f"\n====================\nName: {self.name}\n--------------------\nSkills: {self.skills}\n--------------------\nTraits: {self.traits}\n===================="

if __name__ == "__main__":
    TEST_ITERATION_NUM = 5
    characterCreationInstance = CharacterCreator()

    for i in range(TEST_ITERATION_NUM):
        characterCreationInstance.randomise(False,False)
        print(characterCreationInstance)
