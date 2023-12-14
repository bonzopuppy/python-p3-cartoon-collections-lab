def roll_call_dwarves(dwarves):
    dwarf_list = [f"{i}. {dwarf}" for i, dwarf in enumerate(dwarves, start=1)]
    final_dwarf_list = "\n".join(dwarf_list)
    print(final_dwarf_list)


def summon_captain_planet(planeteer_calls):
    capital_calls = [f"{call.capitalize()}!" for call in planeteer_calls]
    return capital_calls


def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)


def find_the_cheese(items):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheese_types:
            return item

    return None
