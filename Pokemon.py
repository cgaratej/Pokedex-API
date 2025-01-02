class pokemon:
    def __init__(self, name, hp, attack, defence, speed, urlImg, type=None):
        self.__name = name
        self.__hp = hp
        self.__attack = attack
        self.__defence = defence
        self.__speed = speed
        self.__urlImg = urlImg
        self.__type = type

    def GetName(self):
        return self.__name
    
    def Gethp(self):
        return self.__hp
    
    def GetAttack(self):
        return self.__attack
    
    def GetDefence(self):
        return self.__defence
    
    def GetSpeed(self):
        return self.__speed

    def GetUrlImg(self):
        return self.__urlImg
    
    def GetType(self):
        return self.__type

