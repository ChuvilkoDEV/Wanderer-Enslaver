import json


def generateDefaultUser():
    data = {
        "user_name": "Безымянный воин",
        "money": 0,
        "hunger": 150,
        "state_of_life": "Живой",
        "head_bounty": 0,
        "honor": 50,
        "wins": 0,
        "loses": 0,
        "close_combat": 1,
        "close_combat_exp": 0,
        "distante_battle": 1,
        "distante_battle_exp": 0,
        "defense": 1,
        "defense_exp": 0,
        "strength": 1,
        "strength_exp": 0,
        "employment": 1,
        "employment_exp": 0,
        "breaking": 1,
        "breaking_exp": 0,
        "stealth": 1,
        "stealth_exp": 0,
        "main_weapon": "Отсутствует",
        "secondary_weapon": "Отсутствует",
        "head_armor": "Отсутствует",
        "outer_armor": "Отсутствует",
        "additional_armor": "Отсутствует",
        "legs_armor": "Дырявые трусы",
        "shoes_armor": "Отсутствует",
        "burnt_meat": 0,
        "bowl_of_rice": 0,
        "shawarma": 0,
        "tools": 0,
        "steel": 0,
        "shackles": 0,
        "cells": 0,
        "time_for_next_job": '0001-00-00 00:00:00.000000'
    }
    with open('DataBase/defaultUser.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp)
