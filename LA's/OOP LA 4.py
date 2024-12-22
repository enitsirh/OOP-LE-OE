class classHero():
    def __init__(self, name, basic_atk):
        self.name = name
        self.basic_atk = basic_atk
    
    def describe(self):
        return f"{self.name} is a {self.basic_atk}"
    
    def __str__(self):
        return f"{self.name} is a Marksman Hero"

ml_hero = classHero("Hanabi", "Marksman Hero")

print(ml_hero)