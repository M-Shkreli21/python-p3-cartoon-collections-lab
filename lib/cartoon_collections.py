def roll_call_dwarves(dwarf_names):
    i = 1
    for name in dwarf_names:
        print(f'{i}. {name}')
        i += 1

roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

def summon_captain_planet(planeteer_calls):
    planeteer_calls = [i.capitalize() + "!" for i in planeteer_calls]
    return planeteer_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False
            
long_planeteer_calls(['puff', 'go', 'two'])
long_planeteer_calls(['two', 'go', 'industrious', 'bop'])

def find_the_cheese(foods):
    for food in foods:
        if food == "cheddar":
            return food
        elif food == 'gouda':
            return food
        elif food == "camembert":
            return food
    return None

find_the_cheese(["banana", "cheddar", "sock"])