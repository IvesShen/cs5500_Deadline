from datetime import datetime
from collections import defaultdict


class Pet():

    """Docstring for Pet. """

    def __init__(self, kind, place, cuteness_level, hungry_level,
                 owner, color):
        """Constructor for Pet class

        :kind: TODO
        :gender: TODO
        :places: TODO
        :cuteness_level: TODO
        :hungry_level: TODO
        :owner: TODO
        :color: TODO

        """
        self._kind = kind
        self._place = place
        self._places = defaultdict(list)
        self._places[place].append(datetime.now())
        self._cuteness_level = cuteness_level
        self._hungry_level = hungry_level
        self._owner = owner
        self._color = color

    @property
    def kind(self):
        return self._kind

    @property
    def cuteness_level(self):
        return self._cuteness_level

    @cuteness_level.setter
    def cuteness_level(self, value):
        self._cuteness_level = value

    @cuteness_level.deleter
    def cuteness_level(self):
        del self._cuteness_level

    @property
    def hungry_level(self):
        return self._hungry_level

    @hungry_level.setter
    def hungry_level(self, value):
        self._hungry_level = value

    @hungry_level.deleter
    def hungry_level(self):
        del self._hungry_level

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @owner.deleter
    def owner(self):
        del self._owner

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value
        current_time = str(datetime.now())
        self._places[value].append(current_time)


class Dog(Pet):

    """Docstring for Dog. """

    def __init__(self, gender, breed, height, weight, name):
        """TODO: to be defined1.

        :gender: TODO
        :breed: TODO
        :height: TODO
        :weight: TODO
        :name: TODO

        """
        Pet.__init__(self)

        self._gender = gender
        self._breed = breed
        self._weight = weight
        self._height = height
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
