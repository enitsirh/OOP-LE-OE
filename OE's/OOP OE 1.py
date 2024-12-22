class mlbb_hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} is a {self.role} that has {self.damage_type}"

heroes = [
    mlbb_hero("Ling", "Core", "Physical Damage"),
    mlbb_hero("Freya", "Fighter", "Physical Damage"),
    mlbb_hero("Karrie", "Marksman", "True Damage"),
    mlbb_hero("Lou Yi", "Mage", "Magic Damage"),
    mlbb_hero("Angela", "Support", "Magic Damage"),
]

# Printing each hero
for hero in heroes:
    print(hero)
