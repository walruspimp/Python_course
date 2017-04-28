#!/usr/bin/env python
"""
In this exercise we will create a number of classes and apply some elementary
object-oriented programming.

Implement the following classes describing some of the actors in an elementary
video game.

All actors have a property "strength". Strength is a number that can be
increased by x by calling the method "increase_strength(x)", resp. "strength" is
decreased by x by calling the method "decrease_strength(x)". If the strength drops
below zero, it should remain zero.

The property "is_alive" should start out True, and become False once strength
reaches zero. Contrary to popular opinion, Zombies and Vampires should
start out as alive.

All actors will contain the method "fight()". Actor x can start a fight with
Actor y by calling "x.fight(y)". The one with the highest strength wins,
the other dies. The winner is damaged however, and gets its strength decreased
by the strength of the opponent. If the strengths are equal, both die horribly.

All actors have a "kills" property which increases by one when the actor wins a
fight.

Class Hero has an special property "magic". Hero's "strength" can increase only
if "magic" is above zero. x increase in "strength" causes x decrease in "magic".

Class Vampire will increase its property "strength" after winning a fight, instead
of decreasing it, by half the strength of its enemy.

Class Zombie will increase its "strength" by x at the beginning of every fight
_it starts itself_, where x is a randomly generated number between 1 and 10.
"""


class Actor:
    """
    This is supposed to be the most general class, at the top of the hierarchy:
    everything that shared between all actors can be put here.
    """
    pass


class Hero(Actor):
    """
    Heroes start out with 100 strength and 50 magic.
    """
    pass


class Zombie(Actor):
    """
    Zombies start out with 150 strength.
    Remember that Zombies increase their strength randomly at the beginning
    of each fight. How to generate a random number?
    """
    pass


class Vampire(Actor):
    """
    Vampires start out with 70 strength.
    Remember that when a Vampire wins a fight it starts, it obtains half of the
    strength of the enemy it has beaten.
    """
    pass


"""
From here on unit tests.
Do not modify this code!
"""


def test_hero_strength():
    hero = Hero()
    assert hero.strength == 100, 'Hero strength does not initialize to 100'
    assert hero.magic == 50, 'Hero magic does not initialize to 50'
    assert hero.is_alive, 'Hero aliveness does not intialize to True'

    hero.increase_strength(50)
    assert hero.strength == 150, 'Hero increase_strength does not increase strength'
    assert hero.is_alive, 'Hero increase_strength breaks is_alive'
    assert hero.magic == 0, 'Hero increase_strength does not decrease magic'

    hero.decrease_strength(149)
    assert hero.strength == 1, 'Hero decrease_strength does not decrease strength'
    assert hero.is_alive, 'Hero decrease_strength breaks is_alive'

    hero.decrease_strength(5)
    assert hero.strength == 0, 'Hero decrease_strength breaks when going below 0'
    assert not hero.is_alive, 'Hero decrease strength breaks when going below 0'


def test_hero_fights_vs_vampires():
    hero = Hero()
    assert hero.strength == 100, 'Hero strength does not initialize to 100'
    assert hero.kills == 0, 'Hero kills does not initialize to 0'

    first_vampire = Vampire()
    assert first_vampire.strength == 70, 'Vampire strength does not initialize to 70'
    assert first_vampire.is_alive, 'Vampire is_alive does not initialize to True'

    first_vampire.fight(hero)
    assert hero.strength == 30, 'Vampire fight does not decrease hero strength correctly'
    assert hero.is_alive, 'Vampire fight breaks hero is_alive'
    assert hero.kills == 1, 'Vampire fight does not increase Hero kills'
    assert not first_vampire.is_alive, 'Vampire fight does not kill vampire'

    second_vampire = Vampire()
    second_vampire.fight(hero)

    assert hero.strength == 0, 'Vampire fight does not decrease Hero strength'
    assert not hero.is_alive, 'Vampire fight does not kill Hero'
    assert hero.kills == 1, 'Vampire fight breaks existing Hero kill count'
    assert second_vampire.is_alive, 'Vampire fight breaks Vampire is_alive'
    assert second_vampire.strength == 85, 'Vampire fight does not increase strength after win'
    assert second_vampire.kills == 1, 'Vampire fight deos not increase Vampire kills'


def test_hero_loses_against_zombie():
    hero = Hero()
    zombie = Zombie()
    assert zombie.strength == 150, 'Zombie strength does not initialize properly'

    zombie.fight(hero)
    assert not hero.is_alive, 'Zombie fight does not kill Hero'
    assert hero.kills == 0, 'Zombie fight breaks Hero kills'
    assert zombie.is_alive, 'Zombie fight breaks Zombie is_alive'
    assert zombie.kills == 1, 'Zombie fight breaks Zombie kills'
    assert zombie.strength > 50, 'Zombie fight does not increase strength'
    assert zombie.strength < 61, 'Zombie fight increases strength too much'


if __name__ == '__main__':
    from test_runner import run_tests
    run_tests()
