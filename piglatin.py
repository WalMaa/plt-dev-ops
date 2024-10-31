class PigLatin:

    __phrase: str

    def __init__(self, phrase: str):
        self.__phrase = phrase

    def get_phrase(self) -> str:
        return self.__phrase

    def translate(self) -> str:
        pass

    class PigLatinTranslator:

        def __init__(self, phrase: str):
            self.__phrase = phrase

        def get_phrase(self) -> str:
            return self.__phrase