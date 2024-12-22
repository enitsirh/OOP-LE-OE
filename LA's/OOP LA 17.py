class Player:
    def __init__(self, name, health, atk_pwr):
        self.name = name
        self.health = health
        self.atk_pwr = atk_pwr

    def attack(self, target):
        target.health -= self.atk_pwr
        if target.health < 0:
            target.health = 0

    def heal(self, amount):
        self.health += amount

wolverine = Player("Wolverine", 1000, 155)
hulk = Player("Hulk", 5000, 320)

while wolverine.health > 0 and hulk.health > 0:
    wolverine.attack(hulk)
    print(hulk.name, hulk.health, "HP", hulk.atk_pwr, "dmg")
   
    if hulk.health <= 0:
        break
    
    if wolverine.health < 500:
        wolverine.heal(300)
        print(f"{wolverine.name} heals to {wolverine.health} HP")

    hulk.attack(wolverine)
    print(wolverine.name, wolverine.health, "HP", wolverine.atk_pwr, "dmg")

if wolverine.health <= 0:
    print(f"{hulk.name} wins!")
else:
    print(f"{wolverine.name} wins!")