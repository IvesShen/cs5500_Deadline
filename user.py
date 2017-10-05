class User():

    """Docstring for User. """

    def __init__(self, name="unknown", email="unknown", password="unknown",
                 information="unknown"):
        """TODO: to be defined1.

        :name: TODO
        :email: TODO
        :password: TODO
        :information: TODO

        """

        self._name = name
        self._email = email
        self._password = password
        self._information = information

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("name has to be a string")

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str):
            self._email = value
        else:
            raise TypeError("email has to be a string")

    @email.deleter
    def email(self):
        raise AttributeError("Can't delete attribute")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            self._password = value
        else:
            raise TypeError("password has to be a string")

    @password.deleter
    def password(self):
        raise AttributeError("Can't delete attribute")

    @property
    def information(self):
        return self._information

    @information.setter
    def information(self, value):
        if isinstance(value, str):
            self._information = value
        else:
            raise TypeError("information has to be a string")

    @information.deleter
    def information(self):
        raise AttributeError("Can't delete attribute")
