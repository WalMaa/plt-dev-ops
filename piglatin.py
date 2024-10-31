class PigLatin:



    def __init__(self, phrase: str):
        pass

    def get_phrase(self) -> str:
        pass

    def translate(self) -> str:
        pass

    class PigLatinTranslator:

        __phrase: str

        def __init__(self, phrase: str):
            self.__phrase = phrase

        def get_phrase(self) -> str:
            return self.__phrase

        def translate(self) -> str:
            if ( self.__phrase == ""):
                return "nil"

            return self.__phrase