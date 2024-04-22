class Character():
    def __init__(self, Name, DoB, IntelliJ, Speed):
        self.__CharacterName = Name # string
        self.__DateOfBirth = DoB # date
        self.__Intelligence = IntelliJ # real
        self.__Speed = Speed # integer

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewIntellegence):
        self.__Intelligence = NewIntellegence

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - int(self.__DateOfBirth[-4:])
    
FirstCharacter = Character("Royal", "1 January 2019", 70, 30)
FirstCharacter.Learn()
print(f"Name: {FirstCharacter.GetName()} \nAge: {FirstCharacter.ReturnAge()} \nIntellegence: {FirstCharacter.GetIntelligence()}")

class MagicCharacter(Character):
    def __init__(self, Name, DoB, IntelliJ, Speed, Element):
        super().__init__(Name, DoB, IntelliJ, Speed)
        self.__Element = Element

    def Learn(self):
        Element = self.__Element
        if Element in ["fire", "water"]:
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)

FirstMagic = MagicCharacter("Light", "3 March 2018", 75, 22, "fire")
FirstMagic.Learn()
print(f"Name: {FirstMagic.GetName()} \nAge: {FirstMagic.ReturnAge()} \nIntellegence: {FirstMagic.GetIntelligence()}")