class Character:
    pass


hero1 = Character()
hero2 = Character()
hero3 = hero1

print(hero1 is hero2)
print(hero1 is hero3)
print(hero1 == hero2)
print(hero2 == hero2)