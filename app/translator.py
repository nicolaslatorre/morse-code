import typing

english_to_morse_code_dictionary: dict[str, str] = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---'
}

class Translator(object):
    def translate(self, character: str) -> str:
        return english_to_morse_code_dictionary[character]