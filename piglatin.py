import functools


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

        def amount_of_starting_consonants(self) -> int:
            consonants = 0
            for char in self.__phrase:
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

            # Starting consonants

            starting_consonants = self.amount_of_starting_consonants()

            if starting_consonants > 0:
                return self.__phrase[starting_consonants:] + self.__phrase[:starting_consonants] + "ay"


            if self.__phrase[-1] == 'y':
                return self.__phrase + "nay"

            if self.__phrase[-1] in self.vowels:
                return self.__phrase + "yay"

            if self.__phrase[-1] not in self.vowels:
                return self.__phrase + "ay"

            return self.__phrase



