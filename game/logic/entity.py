from random import random

class Weapon:   # Временно не используется
    def __init__(self, weapon_name,
                 true_dmg,
                 psy_breach, elemental_breach,
                 punch_dmg, penetrated_dmg, cut_dmg,
                 fire_dmg, ice_dmg, acid_dmg, dark_dmg, light_dmg, magick_dmg, electro_dmg):

        self.weapon_name = weapon_name                  # Название оружия

        self.true_dmg = true_dmg                        # Чистый физический

        self.psy_breach = psy_breach * 0.01             # Физическое пробивание %
        self.elemental_breach = elemental_breach * 0.01 # Элементарное пробивание %

        self.punch_dmg = punch_dmg                      # Ударный урон
        self.penetrated_dmg = penetrated_dmg            # Колющий урон
        self.cut_dmg = cut_dmg                          # Урон разрезом

        self.fire_dmg = fire_dmg                        # Урон огнём
        self.ice_dmg = ice_dmg                          # Урон холодом
        self.acid_dmg = acid_dmg                        # Урон ядом
        self.dark_dmg = dark_dmg                        # Урон тьмой
        self.light_dmg = light_dmg                      # Урон светом
        self.magick_dmg = magick_dmg                    # Урон магией
        self.electro_dmg = electro_dmg                  # Урон электричеством

    def get_weapon_name(self): return self.weapon_name

    def set_weapon_name(self, weapon_name): self.weapon_name = weapon_name

    def get_true_dmg(self): return self.true_dmg

    def set_true_dmg(self, true_dmg): self.true_dmg = true_dmg

    def get_psy_breach(self): return self.psy_breach

    def set_psy_breach(self, psy_breach): self.psy_breach = psy_breach * 0.01

    def get_elemental_breach(self): return self.elemental_breach

    def set_elemental_breach(self, elemental_breach): self.elemental_breach = elemental_breach * 0.01

    def get_punch_dmg(self): return self.punch_dmg

    def set_punch_dmg(self, punch_dmg): self.punch_dmg = punch_dmg

    def get_penetrated_dmg(self): return self.penetrated_dmg

    def set_penetrated_dmg(self, penetrated_dmg): self.penetrated_dmg = penetrated_dmg

    def get_cut_dmg(self): return self.cut_dmg

    def set_cut_dmg(self, cut_dmg): self.cut_dmg = cut_dmg

    def get_fire_dmg(self): return self.fire_dmg

    def set_fire_dmg(self, fire_dmg): self.fire_dmg = fire_dmg

    def get_ice_dmg(self): return self.ice_dmg

    def set_ice_dmg(self, ice_dmg): self.ice_dmg = ice_dmg

    def get_acid_dmg(self): return self.acid_dmg

    def set_acid_dmg(self, acid_dmg): self.acid_dmg = acid_dmg

    def get_dark_dmg(self): return self.dark_dmg

    def set_dark_dmg(self, dark_dmg): self.dark_dmg = dark_dmg

    def get_light_dmg(self): return self.light_dmg

    def set_light_dmg(self, light_dmg): self.light_dmg = light_dmg

    def get_magick_dmg(self): return self.magick_dmg

    def set_magick_dmg(self, magick_dmg): self.magick_dmg = magick_dmg

    def get_electro_dmg(self): return self.electro_dmg

    def set_electro_dmg(self, electro_dmg): self.electro_dmg = electro_dmg


class Armor:    # Временно не используется
    def __init__(self, armor_name,
                 psy_def, elem_def,
                 punch_res, penetrated_res, cut_res,
                 fire_res, ice_res, acid_res, dark_res, light_res, magick_res, electro_res):

        self.armor_name = armor_name                    # Название брони

        self.psy_def = psy_def                          # Физ защита
        self.elem_def = elem_def                        # Элем защита

        self.punch_res = punch_res * 0.01               # Сопротивление удару %
        self.penetrated_res = penetrated_res * 0.01     # Сопротивление пронзанию %
        self.cut_res = cut_res * 0.01                   # Сопротивление разрезу %

        self.fire_res = fire_res * 0.01                 # Сопротивление огню %
        self.ice_res = ice_res * 0.01                   # Сопротивление холоду %
        self.acid_res = acid_res * 0.01                 # Сопротивление токсину %
        self.dark_res = dark_res * 0.01                 # Сопротивление тьме %
        self.light_res = light_res * 0.01               # Сопротивление свету %
        self.magick_res = magick_res * 0.01             # Сопротивление магическому воздействию %
        self.electro_res = electro_res * 0.01           # Сопротивление электричеству %

    def get_armor_name(self): return self.armor_name

    def get_psy_def(self): return self.psy_def

    def get_elem_def(self): return self.elem_def

    def get_cut_res(self): return self.cut_res

    def get_punch_res(self): return self.punch_res

    def get_penetrated_res(self): return self.penetrated_res

    def get_fire_res(self): return self.fire_res

    def get_ice_res(self): return self.ice_res

    def get_acid_res(self): return self.acid_res

    def get_dark_res(self): return self.dark_res

    def get_light_res(self): return self.light_res

    def get_magick_res(self): return self.magick_res

    def get_electro_res(self): return self.electro_res


class Entity:
    def __init__(self, name,
                 lvl, max_xp, xp,
                 strength, physique, agility, intelligence,
                 luck,
                 def_stack, eve_stack,
                 weapon: Weapon | None = None,
                 armor: Armor | None = None):

        self.weapon = weapon
        self.armor = armor

        self.name = name  # Ник игрока или имя противника

        self.lvl = lvl  # Общий показатель силы персонажа
        self.max_xp = max_xp  # Для игрока - количество опыта до поднятия уровня, для монстра - максимальный дроп опыта
        self.xp = xp  # Для игрока - текущее количество опыта, для монстра - минимальный дроп опыта

        self.strength = strength  # Модификатор урона оружия
        self.physique = physique  # Модификатор телосложения, от которого зависит оз
        self.agility = agility  # Шанс уклонения, шанс попадания, очерёдность хода
        self.intelligence = intelligence  # Для маны и заклинаний в будущем

        self.luck = luck  # Увеличение награды, криты, шанс попадания, шанс уклонения

        self.def_stack = def_stack  # Модификатор для усиления защиты
        self.eve_stack = eve_stack  # Количество ударов, от которых можно увернуться

        # Максимальный запас здоровья
        self.max_hp = max(5 * self.lvl +  # Базовое значение хп за уровень
                          int(round(
                              self.physique * 1.75 +  # Модификатор здоровья массы тела
                              self.strength * 1.25 -  # Модификатор здоровья от массы мышц
                              self.agility * 1.25 -  # Отрицательный модификатор здоровья за облегчение массы тела
                              self.intelligence * 1.5,  # Отрицательный модификатор здоровья за счёт тренировки мозга
                              0)), 20)  # Минимальное значение здоровья на первом уровне
        self.hp = self.max_hp  # Текущий запас здоровья

        # Очередность хода, право предвидения первого действия хода
        self.spd = max(int(round(
            self.agility * 1.5 +  # Модификатор скорости за рефлексы
            self.intelligence * 1.25 -  # Модификатор скорости за скорость реакции мозга
            self.strength * 1.25 -  # Отрицательный модификатор скорости за неконтролируемую силу
            self.physique * 1.5, 0)),  # Отрицательный модификатор скорости за массу тела
            int(1 + round(self.lvl * 0.5, 0)))  # Минимальное значение скорости за уровень

        # Сила замаха оружием, чистый физический урон с руки
        self.atk = max(1 * self.lvl +  # Базовая сила замаха за уровень
                       int(round(  # Превосходство уровня над прочими равными
                           self.strength * 1.75 +  # Модификатор замаха от силы тела
                           self.physique * 1.5 +  # Модификатор замаха от массы тела
                           self.agility * 1.25 -  # Модификатор замаха за скорость удара
                           self.intelligence * 1.5,  # Отрицательный модификатор экономии сил
                           0)), 1)  # Минимальное сила замаха

        self.crit_chance = (self.luck * 0.25) ** 0.75 * 0.1  # Шанс крита

    def dynamic_stats(self):  # Запускаем для корректировки характеристик
        # Максимальный запас здоровья
        self.max_hp = max(5 * self.lvl +  # Базовое значение хп за уровень
                          int(round(
                              self.physique * 1.75 +  # Модификатор здоровья массы тела
                              self.strength * 1.25 -  # Модификатор здоровья от массы мышц
                              self.agility * 1.25 -  # Отрицательный модификатор здоровья за облегчение массы тела
                              self.intelligence * 1.5),  # Отрицательный модификатор здоровья за счёт тренировки мозга
                              0), 20)  # Минимальное значение здоровья на первом уровне

        # Очередность хода, право предвидения первого действия хода
        self.spd = max(int(round(
            self.agility * 1.5 +  # Модификатор скорости за рефлексы
            self.intelligence * 1.25 -  # Модификатор скорости за скорость реакции мозга
            self.strength * 1.25 -  # Отрицательный модификатор скорости за неконтролируемую силу
            self.physique * 1.5),  # Отрицательный модификатор скорости за массу тела
            0), int(1 + round(self.lvl * 0.5, 0)))  # Минимальное значение скорости за уровень

        # Сила замаха оружием, чистый физический урон с руки
        self.atk = max(1 * self.lvl +  # Базовая сила замаха за уровень
                       int(round(  # Превосходство уровня над прочими равными
                           self.strength * 1.75 +  # Модификатор замаха от силы тела
                           self.physique * 1.5 -  # Модификатор замаха от массы тела
                           self.agility * 1.25 -  # Модификатор замаха за скорость удара
                           self.intelligence * 1.5),  # Отрицательный модификатор экономии сил
                           0), 1)  # Минимальное сила замаха

        # Шанс критического попадания
        self.crit_chance = (self.luck * 0.25) ** 0.75 * 0.1

    def get_name(self): return self.name

    def set_name(self, name): self.name = name

    def get_lvl(self): return self.lvl

    def set_lvl(self, lvl): self.lvl = lvl

    def get_strength(self): return self.strength

    def set_strength(self, strength): self.strength = strength

    def get_physique(self): return self.physique

    def set_physique(self, physique): self.physique = physique

    def get_agility(self): return self.agility

    def set_agility(self, agility): self.agility = agility

    def get_intelligence(self): return self.intelligence

    def set_intelligence(self, intelligence): self.intelligence = intelligence

    def get_luck(self): return self.luck

    def set_luck(self, luck): self.luck = luck

    def get_max_hp(self): return self.max_hp

    def get_hp(self): return self.hp

    def set_hp(self, hp): self.hp = hp

    def get_spd(self): return self.spd

    def get_atk(self): return self.atk

    def get_def_stack(self): return self.def_stack

    def set_def_stack(self, def_stack): self.def_stack = def_stack

    def get_eve_stack(self): return self.eve_stack

    def set_eve_stack(self, eve_stack): self.eve_stack = eve_stack

    def equip_weapon(self, weapon: Weapon): self.weapon = weapon

    def equip_armor(self, armor: Armor): self.armor = armor

    def end_turn_effects(self):  # Прок эффектов конца хода - усиления, ослабления, доты
        if self.eve_stack > 0:
            self.eve_stack -= 1
        elif self.eve_stack < 0:
            self.eve_stack += 1

        if self.def_stack > 0:
            self.def_stack -= 1
        elif self.def_stack < 0:
            self.def_stack += 1

        return None

    def crit_logic(self):  # Используется atk_logic для получения множителя крита
        roll = random()  # Рандом прока крита
        crit_level = int(self.crit_chance)  # Получаем уровень крита
        upgrade_change = self.crit_chance - crit_level  # Получаем шанс на крит следующего уровня

        if roll <= upgrade_change:  # Получили крит следующего уровня
            crit_level += 1

        if crit_level >= 4:  # Красный крит x3
            return 3
        elif crit_level == 3:  # Оранжевый крит x2.5
            return 2.5
        elif crit_level == 2:  # Жёлтый крит x2
            return 2
        elif crit_level == 1:  # Обычный белый крит x1.5
            return 1.5
        else:  # Нет крита, нет множителя x1
            return 1

    def no_over_heal(self):  # Дополнительная проверка на излишнее лечение
        if self.hp > self.max_hp:  # Предотвращаем переполнение здоровья от эффекта вампиризм
            self.hp = self.max_hp

    @staticmethod
    def base_action(move):  # Сущность посылает ключ, а метод возвращать действие
        action = {1: 'atk', 2: 'def', 3: 'eve', 4: 'rest'}

        return action[move]

    def def_action(self, move):  # Общие защитные действия
        if move == "eve":  # Базовое действие уклонения
            self.eve_stack += 1
        elif move == "def":  # Базовое действие защиты
            self.def_stack += 1

        return None

    def atk_action(self, move):  # Атака игрока
        if move == "atk":  # Если существо выбрало действие атаки
            return True

        else:  # Сущность выбрала отдых или некорректное действие
            self.no_over_heal()
            return False  # Неудачное действие не нанесло урона
