import unittest
from app.translator import Translator

class TranslatorTests(unittest.TestCase):
    def test_translator_translate_method_should_return_the_morse_equivalent_of_A(self):
        translator = Translator()
        result = translator.translate('A')
        self.assertEqual('.-', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_B(self):
        translator = Translator()
        result = translator.translate('B')
        self.assertEqual('-...', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_C(self):
        translator = Translator()
        result = translator.translate('C')
        self.assertEqual('-.-.', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_D(self):
        translator = Translator()
        result = translator.translate('D')
        self.assertEqual('-..', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_E(self):
        translator = Translator()
        result = translator.translate('E')
        self.assertEqual('.', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_F(self):
        translator = Translator()
        result = translator.translate('F')
        self.assertEqual('..-.', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_G(self):
        translator = Translator()
        result = translator.translate('G')
        self.assertEqual('--.', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_H(self):
        translator = Translator()
        result = translator.translate('H')
        self.assertEqual('....', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_I(self):
        translator = Translator()
        result = translator.translate('I')
        self.assertEqual('..', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_J(self):
        translator = Translator()
        result = translator.translate('J')
        self.assertEqual('.---', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_K(self):
        translator = Translator()
        result = translator.translate('K')
        self.assertEqual('-.-', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_L(self):
        translator = Translator()
        result = translator.translate('L')
        self.assertEqual('.-..', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_M(self):
        translator = Translator()
        result = translator.translate('M')
        self.assertEqual('--', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_N(self):
        translator = Translator()
        result = translator.translate('N')
        self.assertEqual('-.', result)

    def test_translator_translate_method_should_return_the_morse_equivalent_of_O(self):
        translator = Translator()
        result = translator.translate('O')
        self.assertEqual('---', result)
