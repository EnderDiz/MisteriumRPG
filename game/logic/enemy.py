from typing import override

from entity import Entity, Armor, Weapon
from random import randint

class Enemy(Entity):
    def __init__(self, name,
                 lvl, max_xp, xp,
                 strength, physique, agility, intelligence,
                 luck,
                 def_stack, eve_stack):

        Entity.__init__(self, name,
                 lvl, max_xp, xp,
                 strength, physique, agility, intelligence,
                 luck,
                 def_stack, eve_stack)

    @override
    def base_action(self): return super().base_action(randint(1, 4))

    def loot_reward(self, player):
        # В случае монстров max_xp - это максимальное количество бонусного опыта
        # Монстры не умеют усиливаться, только игроки и нпс люди имеют в max_xp опыт до следующего уровня
        # xp - средний показатель выпавшего опыта
        xp_drop = int(self.xp * (self.lvl / player.get_lvl()) + randint(0, self.max_xp))

        return xp_drop


enemy = Enemy("Гоблин-тестировщик",
                 1, 10, 1,
                 1, 1, 3, 1,
                 15,
                 0, 0)

enemy_armor = Armor("Шкура тестового монстра", 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1)
enemy_weapon = Weapon("Когти тестового монстра", 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1)