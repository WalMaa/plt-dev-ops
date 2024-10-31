import unittest

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

    def test_translate_word_with_single_consonant(self):
        translator = PigLatin.PigLatinTranslator("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_translate_word_with_multiple_consonants(self):
        translator = PigLatin.PigLatinTranslator("known")
        self.assertEqual("ownknay", translator.translate())

    def test_translate_multiple_words(self):
        translator = PigLatin.PigLatinTranslator("hello world")
        self.assertEqual("ellohay orldway", translator.translate())

    def test_translate_composite_words(self):
        translator = PigLatin.PigLatinTranslator("well-being")
        self.assertEqual("ellway-eingbay", translator.translate())

    def test_preserve_punctuations(self):
        translator = PigLatin.PigLatinTranslator("hello world!")
        self.assertEqual("ellohay orldway!", translator.translate())








