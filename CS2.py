class Player:
    def __init__(self, name, hp: int = 100, armor: int = 50, damage: int = 20):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def attack(self, enemy: Player, headshot=False):
        if headshot:
            print(f"{self.name} стреляет в {enemy.name}! 💥HEADSHOT!")
        else:
            print(f"{self.name} стреляет в {enemy.name}!")
        base_damage = self.damage * 2 if headshot == True else self.damage
        reduced_damage = base_damage - enemy.armor // 2

        if reduced_damage < 1:
            reduced_damage = 1

        enemy.hp = max(0, enemy.hp - reduced_damage)

        print(f"У {enemy.name} осталось ❤ {enemy.hp} hp")


t_name, t_hp, t_armor, t_damage = "Террорист 120 15 30".split()
ct_name, ct_hp, ct_armor, ct_damage = "Контр-террорист 100 22 20".split()

player1 = Player(t_name, int(t_hp), int(t_armor), int(t_damage))
player2 = Player(ct_name, int(ct_hp), int(ct_armor), int(ct_damage))

attacker = player1
defender = player2

attacker.shots = 1
defender.shots = 1

while True:
    if attacker.shots % 2 == 0:
        attacker.attack(defender, headshot=True)
        # print("💥HEADSHOT!")
    else:
        attacker.attack(defender, headshot=False)
    if defender.hp <= 0:
        print(f"Победил {attacker.name}")
        break
    else:
        attacker.shots += 1

    if defender.shots % 2 == 0:
        defender.attack(attacker, headshot=True)
        # print("💥HEADSHOT!")
    else:
        defender.attack(attacker, headshot=False)
    if attacker.hp <= 0:
        print(f"Победил {defender.name}")
        break
    else:
        defender.shots +=   1






    # if defender.shots % 2 == 0:
    #     defender.attack(attacker, headshot=True)
    #     print(f"{defender.name} стреляет в {attacker.name}! 💥HEADSHOT!")
    # else:
    #     defender.attack(attacker)
    #     print(f" {defender.name} стреляет в {attacker.name}!")
    # defender.shots += 1
    # if attacker.hp <= 0:
    #     break