class UNIT:
    pass


class Europe_LongSword_Man(UNIT):
    def __init__(self):

        # 기본 유닛
        self.__unit_name = "롱소드병"
        self.__health = 50
        self.__attack_damage = 10
        self.__quantity = 100
        self.__defensive_power = 5
        self.__speed = 1
        self.__image = None
        self.__range = 2

        

    @property
    def damage(self):

        return self.__attack_damage * self.__quantity

    @property
    def health(self):

        return self.__health * self.__quantity * (1 + self.__defensive_power / 10)

    @property
    def speed(self):

        return self.__speed

    @property
    def name(self):

        return self.__unit_name

    @property
    def image(self):

        return self.__image

    @property
    def range(self):

        return self.__range


class Europe_LongBow_Man(UNIT):
    def __init__(self):

        self.__unit_name = "장궁병"
        self.__health = 25
        self.__attack_damage = 30
        self.__quantity = 50
        self.__defensive_power = 1
        self.__speed = 1
        self.__image = None
        self.__range = 2

    @property
    def damage(self):

        return self.__attack_damage * self.__quantity

    @property
    def health(self):

        return self.__health * self.__quantity * (1 * self.__defensive_power)

    @property
    def speed(self):

        return self.__speed

    @property
    def name(self):

        return self.__unit_name

    @property
    def image(self):

        return self.__image

    @property
    def range(self):

        return self.__range



