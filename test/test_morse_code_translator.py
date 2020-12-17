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
