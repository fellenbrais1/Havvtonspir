
# Defining the default settings when initialising a new game
import operator
from random import randint

character_base_data = {
    'character_number': 0,
    'name': '',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 0,
}

c_1 = {
    'ref': 'c_1',
    'number': 1,
    'name': 'Johnny Johns',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 7,
}

c_2 = {
    'ref': 'c_2',
    'number': 2,
    'name': 'Bibbs',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 2,
}

c_3 = {
    'ref': 'c_3',
    'number': 3,
    'name': 'Chobby Bobba',
    'class': '',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 10,
}

e_1 = {
    'ref': 'e_1',
    'number': 0,
    'name': 'Mad Hatter',
    'class': 'Hatter',
    'level': 1,
    'max_HP': 100,
    'current_HP': 100,
    'max_MP': 50,
    'current_MP': 50,
    'attack': 10,
    'defence': 10,
    'speed': 10,
    'magic': 10,
    'initiative': 3,
}

characters_data = [
    c_1,
    c_2,
    c_3,
]

battlers = [
    c_1,
    c_2,
    c_3,
    e_1
]

# Need to work out how to sort the initiative values into a list for turns
# COMMENTED OUT FOR NOW
# turn_order = sorted(battlers)

active_turn_list = []
for item in battlers:
    item_initiative = item['ref'], item['name'], item['initiative']
    active_turn_list.append(item_initiative)
print(active_turn_list)

active_turn_list = sorted(active_turn_list, key=operator.itemgetter(2))

print(active_turn_list)

status_effects = [
    'KO',
    'Sleep',
    'Poison',
    'Silence',
    '',
]

game_data = {
    'save_file_name': 'Save File 1',
    'world_position': 0,
    'map_position': 0,
    'story_trigger': 0,
    'time_elapsed': 0,
    'reputation': 0,
    'character_data': character_base_data,


}

character_health = c_1['current_HP']

print(character_health)

damage = randint(1, 25) - c_1['defence']
if damage < 0:
    damage = 0


print('{0} took {1} damage!'.format(c_1['name'], damage))
c_1['current_HP'] = c_1['current_HP'] - damage

print(c_1['name'], 'now has', c_1['current_HP'], 'HP!')
