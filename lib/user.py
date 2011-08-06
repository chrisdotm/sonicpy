#!/bin/env python
import md5
import config
import dbo

'''
' Author: Chris McCoy
' ./lib/user.py
' This is the user class
' in order to keep it modular nothing should directly reference storage here
'''


class User:
    def __init__(self, name, email, username, password):
        """Create a new user
        password will never be stored in plain text always pass a hash
        users should be unique on username
        """
        self.name = name
        self.email = email
        self.username = username
        # I don't trust people to always give me hashed passwords
        hash_pass = md5.new(password + config.get('security', 'salt')).digest()
        self.password = hash_pass

    def create(self):
        """Create a new user
        This is a very ugly function but what are you gonna do?
        """
        if User.load(username) is None:
            """This username is not in use"""
            if self.validateEmail(self.email):
                """This email is valid"""
                if len(self.username) > 2:
                    """This is long enough"""
                    self.__store()

    def disable(self):
        """Instead of allowing deletion of users we just disable their usage"""
        self.enabled = False
        self.__store(self)

    def enable(self):
        """Reenable a user"""
        self.enable = True
        self.__store(self)

    def __store(self):
        """Attempts to store a user in whatever database model is used"""
        # connection strings are accessed directly by dbo
        dbo = dbo.connect()
        dbo.save(self.__to_dict())
         # not supre important to call but a nice idea
        dbo.destroy()

    def __to_dict(self):
        """Turn the object into a dictionary"""
        our_dict = {'username': self.username, 'email': self.email,
            'name': self.name, 'enable': self.enable}
        return our_dict

    def load(self, username):
        """Attempts to load a user from whatever database model is used"""
        dbo = dbo.connect()
        # performs the actual query
        result = dbo.get_one('User', 'username=%s' % username)
        # initialize the results using query data
        self.username = result.get('username')
        self.email = result.get('email')
        self.password = result.get('password')
        self.name = result.get('name')
        self.enable = result.get('enable')

        dbo.destroy()  # not super important to call but a nice idea

    @staticmethod
    def authenticate(username, password):
        """attempt to authenticate a user"""
        test = User.load(username)
        test_password = test.password
        input_password = md5.new(
                password + config.get('security', 'salt')).digest()
        if input_password == test_password:
            return True
        else:
            return False

    @staticmethod
    def validateEmail(address):
        pattern = "[\.\w]{2,}[@]\w+[.]\w+"
        if re.match(pattern, address):
            return True
        else:
            return False


# vim: ts=4:sw=4:softtabstop=4:expandtab
