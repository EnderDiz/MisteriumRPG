from random import randint
from enemy import enemy
from player import player
from math import e

class Battle:
    def __init__(self):
        super().__init__()
        self.first, self.second = None, None

    def battle_cycle(self):
        # Первый этап - определение очередности хода
        self.first, self.second = self.speed_check(player, enemy)
        first_dmg, second_dmg = 0, 0 # Не забываем обнулять урон

        # Второй этап - определение действий
        blind_move = self.first.base_action()  # Совершает слепое действие
        reaction_move = self.reaction(blind_move)  # Получает действие первого и на этой основе выбирает своё действие

        # Третий этап - предварительные действия
        self.second.def_action(reaction_move)    # В первую очередь используется действие быстрого
        self.first.def_action(blind_move)    # Вторым ходит более медленный

        # Четвёртый этап - атакующие действия
        first_dmg = self.atk_logic(self.first, self.second, reaction_move) # Первый атакует второго реакцией
        self.second.set_hp(self.second.hp - first_dmg) # Отнимаем из здоровья медленного урон быстрого
        if self.battle_end(): # Проверка на необходимость продолжать цикл
            return True # Бой кончился раньше конца круга

        second_dmg = self.atk_logic(self.second, self.first, blind_move) # Второй атакует первого слепым действием
        self.first.set_hp(self.first.hp - second_dmg)
        # Вторую проверку не проводим. Сразу переходим на пятый этап

        # Пятый этап - эффекты конца хода
        self.second.end_turn_effects()   # Чем ты быстрее, тем раньше для тебя сработают эффекты конца хода
        self.first.end_turn_effects()   # Более медленный соперник может избежать смерти за счёт запоздалого лечения

        # Шестой этап - финальная проверка
        return self.battle_end()   # Возвращаем результат раунда

    def battle_end(self):   # Бой кончился?
        if (self.first.get_hp() <= 0) or (self.second.get_hp() <= 0):   # У одного из соперников кончились жизни
            return True # Да
        return False    # Нет

    # Вернуть extra turn от скорости > 100
    @staticmethod
    def speed_check(entity_one, entity_two):    # Сравниваем скорости двух сущностей
        if entity_one.get_spd() > entity_two.get_spd(): # Если первый быстрее, то первый быстрее
            return entity_one, entity_two

        elif entity_one.get_spd() == entity_two.get_spd(): # Если скорости равны, то кидаем монетку
            if randint(1, 2) < 2:   # Если выпало 1 - первый быстрее
                return entity_one, entity_two
            else:   # Если выпало 2 - второй быстрее
                return entity_two, entity_one

        else:   # Если первый не быстрее и скорости не равны, то быстрее второй
            return entity_two, entity_one

    def reaction(self, blind_move):
        if self.first is player:
            if blind_move == "atk":
                return "eve"
            elif blind_move == "def":
                return "atk"
            elif blind_move == "rest":
                return "atk"
            else:
                return "rest"
        else:
            print("Враг делает " + blind_move)
            return self.second.base_action()

    @staticmethod
    def get_eve_chance(attacker, defender):  # Проверка на удачное уклонение
        chance = int(1 / (1 + e ** (min(-0.75 + 0.015 *
                                          (defender.get_luck() - attacker.get_luck()), -0.25) * # Проверка на везучего мальчика
                                          (defender.get_agility() - attacker.get_agility() +    # Разница времени реакции
                                           defender.get_intelligence() * 0.25 -           # Грамотный расчёт времени
                                           defender.get_physique() * 0.25))) * 100)       # Неконтролируемая сила

        return min(max(0, chance), 100)

    def eve_logic(self, attacker, defender):
        if randint(1, 100) <= self.get_eve_chance(attacker, defender):
            return True  # Удалось уклониться
        else:  # Дополнительная атака от противника за неудачное уклонение
            print('Доп атака')
            return False  # Дополнительная атака всегда проходит перед основным атакующим действием

    def atk_logic(self, attacker, defender, move):
        aw, da = attacker.weapon, defender.armor
        if attacker.atk_action(move): # Действие атака? Если нет - отдых
            bonus_dmg = 0   # Не забываем обнулять бонусный урон

            if (defender.get_eve_stack() > 0) and (self.eve_logic(attacker, defender)):
                return 0 + bonus_dmg # Возвращаем нулевой урон

            else:
                # Наказание за провал уклонения
                bonus_dmg = max(1, # Бонусный урон не может быть меньше 1 чистого урона
                                int(defender.get_hp() * # Часть текущего хп
                                    max(0.01, # Не меньше 1% текущего здоровья
                                        (0.25 - defender.get_luck() * 0.001)) # Можно немного снизить урон удачей
                                    ))

            true_dmg = max(0, aw.get_true_dmg() + bonus_dmg) # Чистый урон не подвержен изменениям

            # Защитная стойка или атакующая
            if defender.get_def_stack() > 0: # Конверсия брони с учётом защитной стойки
                defensive_stand = min(0.75 + defender.get_def_stack() * 0.5, 2)
            elif defender.get_def_stack() < 0: # Конверсия брони с учётом уязвимости
                defensive_stand = max(0.75 + defender.get_def_stack() * 0.5, 0)
            else:
                defensive_stand = 0.75 # Базовая конверсия брони

            # Урон на % сопротивления физ.
            cut_dmg = aw.get_cut_dmg() * (1 - da.get_cut_res())
            penetrated_dmg = aw.get_penetrated_dmg() * (1 - da.get_penetrated_res())
            punch_dmg = aw.get_punch_dmg() * (1 - da.get_punch_res())
            # Вычитаем из урона общую физическую защиту, делённую на процентное пробивание
            psy_res = da.get_psy_def() * defensive_stand # Учитываем защитные стеки
            breached_psy_res = psy_res * (1 - aw.get_psy_breach())

            # Физические типы урона
            crit = attacker.crit_logic() # Криты работают только на физ урон
            total_psy_dmg = max(1, # Защита от отрицательного урона
                                (attacker.get_atk() + cut_dmg + penetrated_dmg + punch_dmg - breached_psy_res) *
                                crit) # Берём урон с руки, он тоже физический

            # Урон на % сопротивления элем.
            fire = aw.get_fire_dmg() * (1 - da.get_fire_res())
            ice = aw.get_ice_dmg() * (1 - da.get_ice_res())
            acid = aw.get_acid_dmg() * (1 - da.get_acid_res())
            dark = aw.get_dark_dmg() * (1 - da.get_dark_res())
            light = aw.get_light_dmg() * (1 - da.get_light_res())
            magick = aw.get_magick_dmg() * (1 - da.get_magick_res())
            electro = aw.get_electro_dmg() * (1 - da.get_electro_res())
            # Вычитаем из урона общую элементную защиту, делённую на процентное пробивание
            elem_res = da.get_elem_def() * defensive_stand
            breached_elem_res = elem_res * (1 - aw.get_elemental_breach())

            # Элементные типы урона
            total_elem_dmg = max(0, fire + ice + acid + dark + light + magick + electro - breached_elem_res) # Защита от отрицательного урона

            # Основное атакующее действие после провала/отсутствия уклонения
            return int(true_dmg + total_psy_dmg + total_elem_dmg)
