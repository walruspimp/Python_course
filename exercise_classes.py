from test_runner import run_tests

# CLASSES
#
# Implement the following classes describing some of the actors in an elementary
# video game. All actors have a property "strength", which is a number that can be
# increased by x, by calling the method "increase_strength(x)", resp. decreased
# by x by calling the method "decrease_strength(x)". If the strength drops below
# zero, it should remain zero.
#
# The property "is_alive" should start out True, and become False once strength
# reaches zero. Contrary to popular opinion, Zombies and Vampires should
# start out as alive.
#
# Two actors x and y can fight eachother by calling "x.fight(y)". The one with the
# highest strength wins, the other dies. The winner is damaged however, and gets
# its strength decreased by the strength of the opponent.
# The winner gets its "kills" property increased by one.


class Actor:
    pass


class Hero(Actor):
    pass


class Enemy(Actor):
    pass


class Zombie(Enemy):
    pass


class Vampire(Enemy):
    pass


def test_hero_strength():
    hero = Hero()
    assert hero.strength == 100
    assert hero.is_alive

    hero.increase_strength(50)
    assert hero.strength == 150
    assert hero.is_alive

    hero.decrease_strength(149)
    assert hero.strength == 1
    assert hero.is_alive

    hero.decrease_strength(5)
    assert hero.strength == 0
    assert not hero.is_alive


def test_hero_fights_and_wins():
    hero = Hero()
    assert hero.strength == 100
    assert hero.kills == 0

    first_vampire = Vampire()
    assert first_vampire.strength == 25
    assert first_vampire.is_alive

    hero.fight(first_vampire)
    assert hero.strength == 75
    assert hero.is_alive
    assert hero.kills == 1
    assert not first_vampire.is_alive

    second_vampire = Vampire()
    hero.fight(second_vampire)

    assert hero.strength == 50
    assert hero.is_alive
    assert hero.kills == 2
    assert not second_vampire.is_alive


def test_hero_fights_and_loses():
    hero = Hero()
    zombie = Zombie()
    assert zombie.strength == 150

    hero.fight(zombie)
    assert not hero.is_alive
    assert hero.kills == 0
    assert zombie.is_alive
    assert zombie.kills == 1


if __name__ == '__main__':
    run_tests()
