'''В этой миссии вам необходимо будет создать класс Warrior, у экземпляров которого будет 2 параметра — здоровье
(равное 50) и атака (равная 5), а также свойство is_alive, которое может быть True (если здоровье воина > 0) или False
(в ином случае). Кроме этого вам необходимо создать класс для второго типа солдат — Knight, который будет наследником
Warrior, но с увеличенной атакой — 7. Также вам необходимо будет создать функцию fight(), которая будет проводить дуэли
между 2 воинами и определять сильнейшего из них. Бои происходят по следующему принципу:
• каждый ход первый воин наносит второму урон в размере своей атаки, в следствие чего здоровье второго воина уменьшается
• аналогично поступает и второй воин по отношению к первому.
Если в конце очередного хода у первого воина здоровье > 0, а у другого — нет, выживший объявляется победителем и функция
 возвращает True, или False в ином случае.'''


class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
