from openmdao.api import IndepVarComp, Group

from openmdao.utils.options_dictionary import OptionsDictionary
from lsdo_aircraft.api import Preprocess, Atmosphere, Powertrain, PowertrainGroup, AtmosphereGroup
from lsdo_aircraft.api import SimpleRotor, SimpleMotor
from UAM_team_optimization.Aero import Aero
from UAM_team_optimization.Aero_group import AeroGroup
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp

#from lsdo_aircraft.preprocess.preprocess_group import PreprocessGroup
# from lsdo_aircraft.api import SimpleRotorGroup
from openmdao.api import ExplicitComponent

import numpy as np

n = 1
shape = (n, n)

powertrain = Powertrain()

preprocess_name = 'preprocess'
atmosphere_name = 'atmosphere'
simple_motor_name = 'motor'
simple_rotor_name = 'rotor'



powertrain.add_module(Preprocess(
    name=preprocess_name,
))
powertrain.add_module(Atmosphere(
    name=atmosphere_name,
))
powertrain.add_module(SimpleMotor(
    name=simple_motor_name,
))
powertrain.add_module(SimpleRotor(
    name=simple_rotor_name,
))

powertrain.add_link(
    preprocess_name, 'altitude',
    atmosphere_name, 'altitude',
)
powertrain.add_link(
    preprocess_name, 'speed',
    atmosphere_name, 'speed',
)
powertrain.add_link(
    preprocess_name, 'speed',
    simple_rotor_name, 'speed',
)
powertrain.add_link(
    atmosphere_name, ['density', 'sonic_speed'],
    simple_rotor_name, ['density', 'sonic_speed'],
)
powertrain.add_link(
    simple_motor_name, ['angular_speed', 'shaft_power'],
    simple_rotor_name, ['angular_speed', 'shaft_power'],
)

class PropulsionGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']

        # ---- ---- ---- ---- CRUISE PROP GROUPS ---- ---- ---- ---- #
        wing_left_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_left_outer_prop_group', wing_left_outer_prop_group, promotes=['*'])

        wing_left_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_left_inner_prop_group', wing_left_inner_prop_group)

        tail_left_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('tail_left_prop_group', tail_left_prop_group)

        wing_right_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_right_outer_prop_group', wing_right_outer_prop_group)

        wing_right_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('wing_right_inner_prop_group', wing_right_inner_prop_group)

        tail_right_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('tail_right_prop_group', tail_right_prop_group)


        # ---- ---- ---- ---- HOVER PROP GROUPS ---- ---- ---- ---- #
        hover_wing_left_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_wing_left_outer_prop_group', hover_wing_left_outer_prop_group)

        hover_wing_left_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_wing_left_inner_prop_group', hover_wing_left_inner_prop_group)

        hover_tail_left_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_tail_left_prop_group', hover_tail_left_prop_group)

        hover_wing_right_outer_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_wing_right_outer_prop_group', hover_wing_right_outer_prop_group)

        hover_wing_right_inner_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_wing_right_inner_prop_group', hover_wing_right_inner_prop_group)

        hover_tail_right_prop_group = PowertrainGroup(
            shape=shape,
            powertrain=powertrain,
        )
        self.add_subsystem('hover_tail_right_prop_group', hover_tail_right_prop_group)


        # ---- ---- ---- ---- CRUISE THRUST ---- ---- ---- ---- #
        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'cruise_total_thrust',
            constant = 0.,
            coeffs_dict=dict(
                cruise_tail_right_thrust =1.,
                cruise_tail_left_thrust =1.,
                cruise_wing_left_inner_thrust = 1.,
                cruise_wing_left_outer_thrust = 1.,
                cruise_wing_right_inner_thrust = 1.,
                cruise_wing_right_outer_thrust = 1.,
            )
        )
        self.add_subsystem('cruise_total_thrust_comp',comp,promotes=['*'])

        # ---- ---- ---- ---- HOVER THRUST ---- ---- ---- ---- #
        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'hover_total_thrust',
            constant = 0.,
            coeffs_dict=dict(
                hover_tail_right_thrust =1.,
                hover_tail_left_thrust =1.,
                hover_wing_left_inner_thrust = 1.,
                hover_wing_left_outer_thrust = 1.,
                hover_wing_right_inner_thrust = 1.,
                hover_wing_right_outer_thrust = 1.,
            )
        )
        self.add_subsystem('hover_total_thrust_comp',comp,promotes=['*'])



        # comp = TestCLWingComp()
        # comp = GeometryComp()
        # self.add_subsystem('geometry_comp', comp, promotes = ['*'])
