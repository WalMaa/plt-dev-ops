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

        def get_phrase(self) -> str:
            return self.__phrase

        def translate(self) -> str:
            if self.__phrase == "":
                return "nil"

            if self.__phrase[0] not in self.vowels:
                return self.__phrase[1:] + self.__phrase[0] + "ay"

            if self.__phrase[-1] == 'y':
                return self.__phrase + "nay"

            if self.__phrase[-1] in self.vowels:
                return self.__phrase + "yay"

            if self.__phrase[-1] not in self.vowels:
                return self.__phrase + "ay"

            return self.__phrase
