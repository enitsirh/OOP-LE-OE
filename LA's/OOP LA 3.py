class classHero():
    def __init__(self, name, basic_atk):
        self.name = name
        self.basic_atk = basic_atk
    
    def describe(self):
        return f"{self.name} is a {self.basic_atk}"
    
ml = classHero("Hanabi", "Marksman hero")

print (ml.describe())
