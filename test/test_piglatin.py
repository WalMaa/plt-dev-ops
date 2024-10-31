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
        self.assertEquals("phrase", translator.get_phrase())

    def test_translate_empty_string(self):
        translator = PigLatin.PigLatinTranslator("")
        self.assertEquals("nil", translator.translate())

    def test_word_ends_with_y_append_nay(self):
        translator = PigLatin.PigLatinTranslator("easy")
        self.assertEquals("easnay", translator.translate())

