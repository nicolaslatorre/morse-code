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
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

class Translator(object):
    def translate(self, character: str) -> str:
        if character in english_to_morse_code_dictionary:
            return english_to_morse_code_dictionary[character]
        return ''

    def translate_word(self, word: str) -> str:
        translated_word = map(lambda x: self.translate(x), list(word.upper()))
        return ' '.join(translated_word)
