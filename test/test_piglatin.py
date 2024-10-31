import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_creator(self):
        translator = PigLatin("phrase")

    def test_get_phrase(self):
        translator = PigLatin("phrase")
        self.assertEquals("phrase", translator.get_phrase())

