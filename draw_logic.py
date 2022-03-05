import random
from typing import List, Dict, Set

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


def get_smallest_length(names: Set[str]) -> int:
    """
    Return the length of the smallest word of a given set
    """
    smallest_length = len(list(names)[0])
    for name in names:
        if len(name) < smallest_length:
            smallest_length = len(name)

    return smallest_length


def get_first_difference_length(names: set) -> int:
    """
    Return the minimum length from which all the string are different
    """
    characters_list = ["" for _ in range(len(names))]
    first_difference_length = 1

    iterations = 1
    while iterations != len(names):
        for i, name in enumerate(names):
            # This way we don't try to access a character undefined (Ex: Simon & Simone)
            if len(name) < iterations:
                return first_difference_length + 1
            else:
                characters_list[i] = (name[:iterations])
        
        unique_characters = set(characters_list)
        if len(unique_characters) == len(characters_list):
            return first_difference_length
        else:
            first_difference_length += 1


def encrypt_name(name: str, key: str) -> str:
    index = 0
    encrypted_name = ""
    for letter in name:
        if index == len(key) - 1:
            index = 0
        else:
            index += 1
        
        encrypted_name += chr((ord(letter) + ord(key[index])) % 127)

    return encrypted_name
        

#TODO make it so all the results have the same length.
def encrypt_draw(associations: Dict[str, str], key: str) -> Dict[str, str]:
    """
    Return the draw result encrypted to make it difficult to decode for a participant.
    """
    encryption = {}

    names = associations.keys()
    first_difference_length = get_first_difference_length(names)
    smallest_length = get_smallest_length(names)

    for name, draw_result in associations.items():
        if first_difference_length < smallest_length:
            draw_result = encrypt_name(draw_result, key)
            encryption[name] = draw_result
    
    return encryption


def print_draw(associations: Dict[str, str]):
    """
    Handle the printing of all the draw results.
    """
    print("The draw results are: ")

    for key in associations.keys():
        print(f"{key} -> {associations[key]}")
    
    print("----------------------------------------\n")