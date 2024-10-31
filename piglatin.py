import functools
from gettext import translation


class PigLatin:



    def __init__(self, phrase: str):
        pass

    def get_phrase(self) -> str:
        pass

    def translate(self) -> str:
        pass

    class PigLatinTranslator:
        vowels = "AaEeIiOoUu"
        __phrase: str

        def __init__(self, phrase: str):
            self.__phrase = phrase

        def amount_of_starting_consonants(self, word) -> int:
            consonants = 0
            for char in word:
                if char not in self.vowels:
                    consonants = consonants + 1
                else:
                    break
            return consonants

        def get_phrase(self) -> str:
            return self.__phrase

        def translate(self) -> str:
            if self.__phrase == "":
                return "nil"

            words = self.__phrase.split()

            translation = ""

            for word in words:
                if translation != "":
                    translation = translation + " "

                if '-' in word:
                    composites = word.split('-')
                    for index, composite in enumerate(composites):
                        composite = self.translate_word(composite)
                        composites[index] = composite
                    translation = translation +  "-".join(composites)
                    continue



                translation = translation + self.translate_word(word)

            return translation

        def translate_word(self, word):

            # Starting consonants
            starting_consonants = self.amount_of_starting_consonants(word)

            # Move starting consonants to the tail and append ay
            if starting_consonants > 0:
                return word[starting_consonants:] + word[:starting_consonants] + "ay"

            if word[-1] == 'y':
                return word + "nay"

            if word[-1] in self.vowels:
                return word + "yay"

            if word[-1] not in self.vowels:
                return word + "ay"

            return word




