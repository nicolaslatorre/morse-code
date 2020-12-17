import typing

english_to_morse_code_dictionary = {
    'A': '.-',
    'B': '-...'
}

class Translator(object):
    def translate(self, character: str) -> str:
        return english_to_morse_code_dictionary[character]