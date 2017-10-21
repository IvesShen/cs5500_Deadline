from datetime import datetime
from collections import defaultdict
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Pet(db.Model):
    """Docstring for Pet. """

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(50), nullable=False)
    place = db.Column(db.String(100))
    places = db.Column(db.Column(JSON))
    owner = db.Column(db.String(100))
    cuteness_level = db.Column(db.Integer, nullable=False)
    hungery_level = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(40))
    breed = db.Column(db.String(100))
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))

    def __init__(self,
                 kind="unknown",
                 place="unknown",
                 cuteness_level=10,
                 hungry_level=10,
                 owner="unknown",
                 color="unknown",
                 gender="unknown",
                 breed="unknown",
                 weight=-1,
                 height=-1,
                 name="unknown"):
        """Constructor for Pet class for default arguments

        :kind: TODO
        :gender: TODO
        :places: TODO
        :cuteness_level: TODO
        :hungry_level: TODO
        :owner: TODO
        :color: TODO
        :gender: TODO
        :breed: TODO
        :weight: TODO
        :height: TODO
        :name: TODO

        """
        self._kind = kind
        self._place = place
        self._places = defaultdict(list)
        self._places[place].append(datetime.now())
        self._cuteness_level = cuteness_level
        self._hungry_level = hungry_level
        self._owner = owner
        self._color = color
        self._gender = gender
        self._breed = breed
        self._weight = weight
        self._height = height
        self._name = name

    def __repr__(self):
        return "Pet({0.id!r}, {0.kind!r}, {0.place!r}, {0.owner!r},\
        {0.cuteness_level!r}, {0.hungry_level!r}, {0.color!r},\
        {0.gender!r}, {0.breed!r}, {0.weight!r}, {0.height!r},\
        {0.name!r})".format(self)

    def __str__(self):
        return "{0.id!r}, {0.kind!r}, {0.place!r}, {0.owner!r},\
        {0.cuteness_level!r}, {0.hungry_level!r}, {0.color!r},\
        {0.gender!r}, {0.breed!r}, {0.weight!r}, {0.height!r},\
        {0.name!r}".format(self)

    def __unicode__(self):
        return self.__str__()


db.create_all()
