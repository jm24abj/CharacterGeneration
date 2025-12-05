import random

def generateName():
    NAME_LIST = [
        "Alice", "Benjamin", "Chloe", "Daniel", "Emma",
        "Finn", "Grace", "Henry", "Isla", "Jack",
        "Lily", "Mason", "Nora", "Oliver", "Poppy",
        "Quinn", "Ruby", "Samuel", "Tara", "Uma",
        "Violet", "William", "Xavier", "Yara", "Zoe"
    ]
    
    return NAME_LIST[random.randint(0,len(NAME_LIST)-1)]
    

def selectSkill():
    return ""

def generateAttributes(skillPoints,maxSkills):
    while skillPoints != 0 and maxSkills > 0:
        pass

if __name__ == "__main__":
    pass