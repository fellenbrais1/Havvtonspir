
# Defining the default settings when initialising a new game

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
}

c_1 = {
    'character_number': 1,
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
}

c_2 = {
    'character_number': 2,
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
}

c_3 = {
    'character_number': 3,
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
}

characters_data = [
    c_1,
    c_2,
    c_3,
]

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
