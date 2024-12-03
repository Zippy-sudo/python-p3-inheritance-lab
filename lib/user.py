#!/usr/bin/env python

import ipdb

class User:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"first name = \"{self.first_name}\", last name = \"{self.last_name}\""
    
    # @property
    # def first_name(self):
    #     return self._first_name
    
    # @first_name.setter
    # def first_name(self, first_name):
    #     self._first_name = first_name

    # @property
    # def last_name(self):
    #     return self._last_name
    
    # @last_name.setter
    # def last_name(self, last_name):
    #     self._last_name = last_name

