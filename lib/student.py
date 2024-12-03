#!/usr/bin/env python

from user import User

import ipdb

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self._knowledge = []
    
    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, lesson):
        self._knowledge.append(lesson)

    def learn(self, lesson):
        self.knowledge = lesson

