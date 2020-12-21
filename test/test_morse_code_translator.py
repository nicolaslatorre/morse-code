import unittest
from app.translator import Translator


class TranslatorTests(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_A(self):
        result = self.translator.translate_character('A')
        self.assertEqual('.-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_B(self):
        result = self.translator.translate_character('B')
        self.assertEqual('-...', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_C(self):
        result = self.translator.translate_character('C')
        self.assertEqual('-.-.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_D(self):
        result = self.translator.translate_character('D')
        self.assertEqual('-..', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_E(self):
        result = self.translator.translate_character('E')
        self.assertEqual('.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_F(self):
        result = self.translator.translate_character('F')
        self.assertEqual('..-.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_G(self):
        result = self.translator.translate_character('G')
        self.assertEqual('--.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_H(self):
        result = self.translator.translate_character('H')
        self.assertEqual('....', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_I(self):
        result = self.translator.translate_character('I')
        self.assertEqual('..', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_J(self):
        result = self.translator.translate_character('J')
        self.assertEqual('.---', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_K(self):
        result = self.translator.translate_character('K')
        self.assertEqual('-.-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_L(self):
        result = self.translator.translate_character('L')
        self.assertEqual('.-..', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_M(self):
        result = self.translator.translate_character('M')
        self.assertEqual('--', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_N(self):
        result = self.translator.translate_character('N')
        self.assertEqual('-.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_O(self):
        result = self.translator.translate_character('O')
        self.assertEqual('---', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_P(self):
        result = self.translator.translate_character('P')
        self.assertEqual('.--.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_Q(self):
        result = self.translator.translate_character('Q')
        self.assertEqual('--.-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_R(self):
        result = self.translator.translate_character('R')
        self.assertEqual('.-.', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_S(self):
        result = self.translator.translate_character('S')
        self.assertEqual('...', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_T(self):
        result = self.translator.translate_character('T')
        self.assertEqual('-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_U(self):
        result = self.translator.translate_character('U')
        self.assertEqual('..-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_V(self):
        result = self.translator.translate_character('V')
        self.assertEqual('...-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_W(self):
        result = self.translator.translate_character('W')
        self.assertEqual('.--', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_X(self):
        result = self.translator.translate_character('X')
        self.assertEqual('-..-', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_Y(self):
        result = self.translator.translate_character('Y')
        self.assertEqual('-.--', result)

    def test_translator_translate_character_method_should_return_the_morse_equivalent_of_Z(self):
        result = self.translator.translate_character('Z')
        self.assertEqual('--..', result)

    def test_translator_translate_character_method_should_return_an_empty_string(self):
        result = self.translator.translate_character('è')
        self.assertEqual('', result)

    def test_translator_translate_word_method_should_return_the_morse_equivalent_of_hello(self):
        result = self.translator.translate_word('hello')
        self.assertEqual('.... . .-.. .-.. ---', result)

    def test_translator_translate_word_method_should_return_the_morse_equivalent_of_world(self):
        result = self.translator.translate_word('world')
        self.assertEqual('.-- --- .-. .-.. -..', result)

    def test_translator_translate_word_method_should_return_an_empty_string_for_empty_word(self):
        result = self.translator.translate_word('')
        self.assertEqual('', result)

    def test_translator_translate_method_should_translate_a_phrase(self):
        result = self.translator.translate('Hello world')
        self.assertEqual('.... . .-.. .-.. ---       .-- --- .-. .-.. -..', result)
