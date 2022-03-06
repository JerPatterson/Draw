import random
import encryption
from typing import List, Dict

RANDOM_CHARACTERS_TO_COMPLETE_NAME = [encryption.random_character() for _ in range(10)]


def make_draw(names: List[str]) -> Dict[str, str]:
    """
    Return a dict of random associations of a given list of names.\n
    *The user has to make sure the names are different.
    """
    draw_results = {}
    number_already_assigned = []

    for i, name in enumerate(names):
        number = 0
        while number == i or number in number_already_assigned:
            number = round(random.randint(0, 1000) % len(names))
        
        draw_results[name] = names[number]
        number_already_assigned.append(number)

    return draw_results
        

# Make sure to display all the results with the same length.
#   Of course it's easier to decrypt if multiple names are similar...
def encrypt_draw(associations: Dict[str, str], key: str) -> Dict[str, str]:
    """
    Return the draw result encrypted to make it difficult to decode for a participant.
    """
    encryption_result = {}

    names = associations.keys()
    first_difference_length = encryption.get_first_difference_length(names)
    smallest_length = encryption.get_smallest_length(names)

    for name, draw_result in associations.items():
        if first_difference_length < smallest_length:
            draw_result = encryption.encrypt_name(draw_result, key)
            encryption_result[name] = draw_result[:smallest_length]
        
        else:
            i = 0
            while len(draw_result) < first_difference_length:
                draw_result += RANDOM_CHARACTERS_TO_COMPLETE_NAME[i]
                i += 1

            draw_result = encryption.encrypt_name(draw_result, key)
            encryption_result[name] = draw_result[:first_difference_length]
    
    return encryption_result


def print_draw(associations: Dict[str, str]):
    """
    Handle the printing of all the draw results.
    """
    print("The draw results are: ")

    for key in associations.keys():
        print(f"{key} -> {associations[key]}")
    
    print("----------------------------------------\n")