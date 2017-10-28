from datetime import datetime
from collections import defaultdict
from sqlalchemy import Column, Integer, String
from database import Base
from json import dumps, loads


class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    _kind = Column(String(50), nullable=False)
    _place = Column(String(100))
    _history = Column(String(1000))
    _owner = Column(String(100))
    _cuteness_level = Column(Integer)
    _hungry_level = Column(Integer)
    _color = Column(String(100))
    _gender = Column(String(40))
    _breed = Column(String(100))
    _weight = Column(Integer)
    _height = Column(Integer)
    _name = Column(String(100))

    def __init__(self,
                 kind="unknown",
                 place="unknown",
                 cuteness_level=10,
                 hungry_level=10,
                 owner="unknown",
                 color="unknown",
                 gender="unknown",
                 breed="unknown",
                 weight=1,
                 height=1,
                 name="unknown"):
        """Constructor for Pet class for default arguments

        :_kind: TODO
        :_gender: TODO
        :_cuteness_level: TODO
        :_hungry_level: TODO
        :_owner: TODO
        :_color: TODO
        :_gender: TODO
        :_breed: TODO
        :_weight: TODO
        :_height: TODO
        :_name: TODO

        """
        self._kind = kind
        self._cuteness_level = cuteness_level
        self._hungry_level = hungry_level
        self._owner = owner
        self._color = color
        self._gender = gender
        self._breed = breed
        self._weight = weight
        self._height = height
        self._name = name
        self.update_place(place)

    def update_place(self, place):
        self._place = place
        try:
            places = defaultdict(list, loads(self._history))
        except TypeError:
            places = defaultdict(list)
        places[place].append(datetime.utcnow().timestamp())
        self._history = dumps(places)

    def __repr__(self):
        return "Pet({0._kind!r}, {0._place!r}, {0._owner!r}, {0._cuteness_level!r}, {0._hungry_level!r}, {0._color!r}, {0._gender!r}, {0._breed!r}, {0._weight!r}, {0._height!r}, {0._name!r})".format(
            self)

    # def __str__(self):
    #     return "{0._kind!r}, {0._place!r}, {0._owner!r}, {0._cuteness_level!r}, {0._hungry_level!r}, {0._color!r}, {0._gender!r}, {0._breed!r}, {0._weight!r}, {0._height!r}, {0._name!r}".format(
    #         self)

    # def __unicode__(self):
    #     return self.__str__()
