import unittest
from idlelib.pyparse import trans

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_creator(self):
        translator = PigLatin.PigLatinTranslator("phrase")
        self.assertTrue(isinstance(translator,PigLatin.PigLatinTranslator))

    def test_get_phrase(self):
        translator = PigLatin.PigLatinTranslator("phrase")
        self.assertEqual("phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin.PigLatinTranslator("")
        self.assertEqual("nil", translator.translate())

    def test_word_ends_with_y_append_nay(self):
        translator = PigLatin.PigLatinTranslator("any")
        self.assertEqual("anynay", translator.translate())

    def test_word_ends_with_vowel_append_yay(self):
        translator = PigLatin.PigLatinTranslator("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_word_ends_with_consonant_append_ay(self):
        translator = PigLatin.PigLatinTranslator("ask")
        self.assertEqual("askay", translator.translate())


