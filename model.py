from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Pet(db.Model):

    """Docstring for Pet. """

    # def __init__(self, kind="unknown", place="unknown", cuteness_level=10,
    #              hungry_level=10, owner="unknown", color="unknown"):
        """Constructor for Pet class

        :kind: TODO
        :gender: TODO
        :places: TODO
        :cuteness_level: TODO
        :hungry_level: TODO
        :owner: TODO
        :color: TODO

        """
        id = db.Column(db.Integer, primary_key=True)
        kind = db.Column(db.String(50), nullable=False)
        place = db.Column(db.String(100))
        places = db.Column(db.Column(JSON))
        owner = db.Column(db.String(100))
        cuteness_level = db.Column(db.Integer, nullable=False)
        hungery_level = db.Column(db.Integer, nullable=False)
        color = db.Column(db.String(100), nullable=False)
        kind = db.Column(db.String(50))
        kind = db.Column(db.String(50))
        kind = db.Column(db.String(50))
        kind = db.Column(db.String(50))
        kind = db.Column(db.String(50))

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if isinstance(value, str):
            self._kind = value
        else:
            raise TypeError("kind has to be a string")

    @kind.deleter
    def kind(self):
        raise AttributeError("Can't delete attribute")

    @property
    def cuteness_level(self):
        return self._cuteness_level

    @cuteness_level.setter
    def cuteness_level(self, value):
        if isinstance(value, int) and 0 < value < 10:
            self._cuteness_level = value
        else:
            raise ValueError("cuteness_level Needs to be 0 and 10 and int")

    @cuteness_level.deleter
    def cuteness_level(self):
        raise AttributeError("Can't delete attribute")

    @property
    def hungry_level(self):
        return self._hungry_level

    @hungry_level.setter
    def hungry_level(self, value):
        if isinstance(value, int) and 0 < value < 10:
            self._hungry_level = value
        else:
            raise ValueError("hungry_level Needs to be 0 and 10 and int")

    @hungry_level.deleter
    def hungry_level(self):
        raise AttributeError("Can't delete attribute")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, str):
            self._owner = value
        else:
            raise TypeError("Owner needs to be a string")

    @owner.deleter
    def owner(self):
        raise AttributeError("Can't delete attribute")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError("color needs to be a string")

    @color.deleter
    def color(self):
        raise AttributeError("Can't delete attribute")

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if isinstance(value, str):
            self._place = value
            current_time = str(datetime.now())
            self._places[value].append(current_time)
        else:
            raise TypeError("place needs to be a string")

    def __repr__(self):
        return "Pet({0.color!r}, {0.kind!r}, {0.cuteness_level!r}, {0.owner!r},\
    {0.hungry_level!r},{0.place!r})".format(self)

    def __str__(self):
        return "({0.color!r}, {0.kind!r}, {0.cuteness_level!r}, {0.owner!r},\
    {0.hungry_level!r},{0.place!r})".format(self)

    def __unicode__(self):
        self.__str__()


class Dog(Pet):

    """Docstring for Dog. """

    def __init__(self, gender="unknown", breed="unknown", height=-1, weight=-1,
                 name="unknown"):
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
        if isinstance(value, str) and value in ["male", "female",
                                                "unknown"]:
            self._gender = value
        else:
            raise ValueError("gender needs to be a string and can be male, \
                             female, or unknown")

    @gender.deleter
    def gender(self):
        raise AttributeError("Can't delete attribute")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if isinstance(value, str):
            self._breed = value
        else:
            raise TypeError("breed needs to be a string")

    @breed.deleter
    def breed(self):
        raise AttributeError("Can't delete attribute")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self._height = value
        else:
            raise TypeError("height needs to be an int")

    @height.deleter
    def height(self):
        raise AttributeError("Can't delete attribute")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if isinstance(value, int):
            self._weight = value
        else:
            raise TypeError("weight needs to be an int")

    @weight.deleter
    def weight(self):
        raise AttributeError("Can't delete attribute")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("name needs to be a string")

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

    def __repr__(self):
        return "Dog({0.breed!r}, {0.cuteness_level!r}, {0.height!r},\
        {0.kind!r}, {0.owner!r}, {0.weight!r}, {0.color!r}, {0.gender!r},\
        {0.hungry_level!r}, {0.name!r}, {0.place!r})".format(self)

    def __str__(self):
        return "Dog({0.breed!r}, {0.cuteness_level!r}, {0.height!r},\
            {0.kind!r}, {0.owner!r}, {0.weight!r}, {0.color!r}, {0.gender!r},\
            {0.hungry_level!r}, {0.name!r}, {0.place!r})".format(self)

    def __unicode__(self):
        return self.__str__()


chiman = Dog()
