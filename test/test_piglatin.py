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

