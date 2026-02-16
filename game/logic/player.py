from typing import override
from entity import Entity, Armor, Weapon, random


class Player(Entity):
    def __init__(self, name,
                 lvl, max_xp, xp, skill_point,
                 strength, physique, agility, intelligence,
                 luck,
                 def_stack, eve_stack):

        Entity.__init__(self, name,
                 lvl, max_xp, xp,
                 strength, physique, agility, intelligence,
                 luck,
                 def_stack, eve_stack)

        self.skill_point = skill_point

        # Максимальный запас выносливости
        self.max_stamina = max(2 * self.lvl +  # Базовое значение выносливости за уровень
                               int(round(
                                   self.physique * 1.5 +  # Модификатор выносливости тела
                                   self.strength * 1.25 -  # Модификатор выносливости от силы
                                   self.agility * 1.25,  # Отрицательный модификатор выносливости за повышение скорости
                                   0)), 10)  # Минимальное значение выносливости на первом уровне
        self.stamina = self.max_stamina

        # Модификатор траты энергии за действие
        self.stamina_cost_modifier = max(
            int(round(
                self.max_stamina * 0.15 +  # Налог на выносливость
                self.strength * 0.75 +  # Модификатор траты выносливости на силу удара
                self.physique * 0.5 -  # Модификатор траты выносливости на движение тела
                self.agility * 0.25 -  # Модификатор экономии выносливости на движение тела
                self.intelligence * 0.5,  # Модификатор экономии выносливости за грамотное разделение нагрузки
                0)), 1)

        # Максимальный запас энергии для магии
        self.max_mana = max(2 * self.lvl +  # Базовое значение магии за уровень
                            int(round(
                                self.intelligence * 1.5 +  # Модификатор чувствительности к магии
                                self.physique * 0.5 +  # Модификатор внутреннего запаса магии
                                (self.physique - self.intelligence * 3),  # Штраф за сдерживание магии в теле
                                0)), 5)  # Минимальное значение магии на первом уровне
        self.mana = self.max_mana

        self.atk_cost = 3 * self.stamina_cost_modifier  # Расход выносливости на атаку
        self.def_cost = 2 * self.stamina_cost_modifier  # Расход выносливости на защиту
        self.eve_cost = 1 * self.stamina_cost_modifier  # Расход выносливости на попытку уклонения

        self.rest_charge = max(int(self.max_stamina * 0.25) - self.stamina_cost_modifier, 1)  # Восстановление энергии за перерыв
        self.rest_heal = int(self.max_stamina * 0.05)  # Восстановление здоровья за перерыв

    @override
    def dynamic_stats(self):    # Запускаем для корректировки характеристик
        super().dynamic_stats()

        # Максимальный запас выносливости
        self.max_stamina = max(2 * self.lvl +       # Базовое значение выносливости за уровень
                        int(round(
                           self.physique * 1.5 +    # Модификатор выносливости тела
                           self.strength * 1.25 -   # Модификатор выносливости от силы
                           self.agility *  1.25,    # Отрицательный модификатор выносливости за повышение скорости
                            0)), 10)                # Минимальное значение выносливости на первом уровне

        # Модификатор траты энергии за действие
        self.stamina_cost_modifier = max(
                        int(round(
                            self.max_stamina * 0.15 + # Налог на выносливость
                            self.strength * 0.75 +    # Модификатор траты выносливости на силу удара
                            self.physique * 0.5 -     # Модификатор траты выносливости на движение тела
                            self.agility * 0.25 -     # Модификатор экономии выносливости на движение тела
                            self.intelligence * 0.5,  # Модификатор экономии выносливости за грамотное разделение нагрузки
                            0)), 1)

        self.atk_cost = 3 * self.stamina_cost_modifier  # Расход выносливости на атаку
        self.def_cost = 2 * self.stamina_cost_modifier  # Расход выносливости на защиту
        self.eve_cost = 1 * self.stamina_cost_modifier  # Расход выносливости на попытку уклонения

        self.rest_charge = max(int(self.max_stamina * 0.25) - self.stamina_cost_modifier, 1)  # Восстановление энергии за перерыв
        self.rest_heal = int(self.max_stamina * 0.05)  # Восстановление здоровья за перерыв

        # Максимальный запас энергии для магии
        self.max_mana = max(2 * self.lvl +                            # Базовое значение магии за уровень
                        int(round(
                            self.intelligence * 1.5 +                 # Модификатор чувствительности к магии
                            self.physique * 0.5 +                     # Модификатор внутреннего запаса магии
                            (self.physique - self.intelligence * 3),  # Штраф за сдерживание магии в теле
                            0)), 5)                                   # Минимальное значение магии на первом уровне

    def get_skill_points(self): return self.skill_point

    def set_skill_points(self, skill_points): self.skill_point = skill_points

    def get_max_stamina(self): return self.max_stamina

    def get_stamina(self): return self.stamina

    def set_stamina(self, stamina): self.stamina = stamina

    def get_stamina_cost_modifier(self): return self.stamina_cost_modifier

    def get_max_mana(self): return self.max_mana

    def get_mana(self): return self.mana

    def set_mana(self, mana): self.mana = mana

    def get_atk_cost(self): return self.atk_cost

    def get_def_cost(self): return self.def_cost

    def get_eve_cost(self): return self.eve_cost

    def get_rest_charge(self): return self.rest_charge

    def get_rest_heal(self): return self.rest_heal

    @override
    def no_over_heal(self): # Дополнительная проверка на излишнее лечение, выносливость и ману
        super().no_over_heal()

        if self.stamina > self.max_stamina:  # Не даём случиться переполнению выносливости
            self.stamina = self.max_stamina

        if self.mana > self.max_mana:  # Не даём случиться переполнению маны
            self.mana = self.max_mana

    def forced_rest(self):
        self.stamina += self.rest_charge  # Проводим принудительный отдых
        self.hp += self.rest_heal  # Восстанавливаем часть ресурсов

        self.no_over_heal()

        return None

    @override
    def base_action(self):
        action = int(input('Выбери действие:\n'
              '1: atk\n'
              '2: def\n'
              '3: eve\n'
              '4: rest\n'))

        return super().base_action(action)

    @override
    def def_action(self, move):  # Переопределённый защитный метод
        if (move == "eve") and (self.stamina >= self.eve_cost):
            self.stamina -= self.eve_cost  # Действует как общий метод, но тратит выносливость игрока
            self.eve_stack += 1

        elif (move == "def") and (self.stamina >= self.def_cost):
            self.stamina -= self.def_cost  # У НПС нелюдей выносливость не предусмотрена
            self.def_stack += 1

        return None

    @override
    def atk_action(self, move): # Атака игрока
        if (move == "atk") and (self.stamina >= self.atk_cost):  # Если игрок выбрал действие атаки
            self.stamina -= self.atk_cost  # Снимаем плату выносливости независимо от попадания
            return True

        else:  # У игрока не хватило энергии или он выбрал некорректное действие
            self.forced_rest()
            return False  # Мы не нанесли урон

    def lvl_up_logic(self): # Поднятие уровня
        while self.xp >= self.max_xp: # Прогоняем круг поднятия уровня
            self.xp -= self.max_xp  # Вычитаем лишний опыт
            self.lvl += 1   # Повышаем уровень
            self.max_xp += self.max_xp * self.lvl  # Опыта до следующего уровня

            # Дополнительная залётная характеристика от поднятия уровня
            chance = random() # Делаем невозможным одинаковое распределение характеристик за забег
            if chance <= 0.05: self.luck += 1
            elif chance <= 0.25: self.physique += 1
            elif chance <= 0.45: self.strength += 1
            elif chance <= 0.65: self.intelligence += 1
            elif chance <= 0.85: self.agility += 1
            else: pass
            # Если не попал в диапазон, то не получил случайную характеристику

            self.skill_point += 3 + self.lvl // 5 # Добавляем несколько очков для выборочного повышения
            self.dynamic_stats() # Динамически корректируем характеристики

            # Небольшое усиление за уровень
            self.max_hp += 2 * (self.lvl - 1)
            self.max_mana += self.lvl - 1

            self.long_time_rest() # Восстанавливаем все ресурсы, как за длительный отдых

        return None

    def long_time_rest(self): # Восстанавливаем все ресурсы после длинного отдыха
        self.hp = self.max_hp
        self.stamina = self.max_stamina
        self.mana = self.max_mana

    def use_skill_point(self, stat): # Распределение очков за уровень
        if self.skill_point > 0:    # Если очки есть, раскидываем их
            self.skill_point -= 1

            if stat == "str": self.strength += 1
            elif stat == "agi": self.agility += 1
            elif stat == "phy": self.physique += 1
            elif stat == "int": self.intelligence += 1
            else: self.skill_point += 1 # Если очко вкинуто не туда, то возвращаем

        return None


player = Player("Игрок",
                 1, 10, 0, 0,
                 1, 1, 2, 1,
                 15,
                 0, 0)

player.equip_weapon(Weapon("Примитивный магический меч",
                           2, 5, 5,
                           1, 1, 3,
                           0, 0, 0, 0, 0, 1, 0))

player.equip_armor(Armor("Примитивный магический доспех",
                         5, 5,
                         5, 5, 5,
                         1, 1, 1, 1, 1, 1, 1))
