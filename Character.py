class Character:
    
    def __init__(self, name: str, skills : list, traits: list):
        self.name = name
        self.skills = skills
        self.traits = traits
    
    def __str__(self):
        return f'--------------------\nName: {self.name}\n--------------------\nSkills: {self.skills}\nTraits: {self.traits}\n--------------------'