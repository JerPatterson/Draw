import random
from typing import Set


def random_character() -> str:
    return chr((random.randint(1, 1270)) % 127)


def get_smallest_length(names: Set[str]) -> int:
    """
    Return the length of the smallest word of a given set
    """
    smallest_length = len(list(names)[0])
    for name in names:
        if len(name) < smallest_length:
            smallest_length = len(name)

    return smallest_length


def get_first_difference_length(names: Set[str]) -> int:
    """
    Return the minimum length from which all the string are different
    """
    characters_list = ["" for _ in range(len(names))]
    first_difference_length = 1

    iterations = 1
    while iterations != len(names):
        for i, name in enumerate(names):
            # This way we don't try to access a character undefined (Ex: Simon & Simone)
            if len(name) >= iterations:
                characters_list[i] = name[:iterations]
        
        unique_characters = set(characters_list)
        if len(unique_characters) == len(characters_list):
            return first_difference_length
        else:
            first_difference_length += 1

        iterations += 1


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