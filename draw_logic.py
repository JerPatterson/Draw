import random
from typing import List, Dict

def make_draw(names: List[str]) -> Dict[str, str]:
    draw_results = {}
    number_already_assigned = []

    for i, name in enumerate(names):
        number = 0
        while number == i or number in number_already_assigned:
            number = round(random.randint(0, 1000) % len(names))
        
        draw_results[name] = names[number]
        number_already_assigned.append(number)

    return draw_results


def print_draw(associations: Dict[str, str]):
    for key in associations.keys():
        print(f"{key} -> {associations[key]}\n")