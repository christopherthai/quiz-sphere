class User:

    all = {}

    def __init__(self, username, is_admin=0, id=None):
        self.id = id
        self.username = username
        self.is_admin = is_admin
        type(self).all[username] = self

    # Property method that returns the username
    @property
    def username(self):
        return self._username

    # Property method that sets the username
    @username.setter
    def username(self, value):
        if value in self.all:
            raise ValueError("Username already exists")
        self._username = value

    # Property method that returns the is_admin value
    @property
    def is_admin(self):
        return self._is_admin

    # Property method that sets the is_admin value
    @is_admin.setter
    def is_admin(self, value):
        if value not in (0, 1):
            raise ValueError("Invalid value for is_admin")
        self._is_admin = value
