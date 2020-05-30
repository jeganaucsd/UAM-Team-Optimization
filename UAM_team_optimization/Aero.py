import numpy as np

from lsdo_utils.api import OptionsDictionary

from UAM_team_optimization.aero_group import AeroGroup

class Aero(OptionsDictionary):

    def initialize(self):
        self.declare('name', types=str)
        self.declare('group_class', default=AeroGroup, values=[AeroGroup])

    def pre_setup(self):
        pass