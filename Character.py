class Character:
    
    def __init__(self, name: str, skills : list, traits: list):
        self.name = name
        self.skills = skills
        self.traits = traits
    
    def __str__(self):
        return f'--------------------\nName: {self.name}\n--------------------\nSkills: {self.skills}\nTraits: {self.traits}\n--------------------'
    
if __name__ == "__main__":
    
    didSucceed = []
    testChar = None
    testNum = 0

    try:
        testChar = Character("Jack",["Construction: +2","Science: +9"], ["Artist: This character can play guitar"])
        didSucceed.append(("can create obj",True))
        print(testChar)
        didSucceed.append(("can __str__",True))
    except:
        print("Not all tests succeeded")
        
    print("\n\n\n============== CHARACTER UNIT TEST ============== ")
    print("=================================================")
        
    for i in range(len(didSucceed)):
        print(f"TEST {i} ({didSucceed[i][0]}) RESULT ==> {"Success" if didSucceed[i][1] else "Faliure"}")
    
    print("=================================================")