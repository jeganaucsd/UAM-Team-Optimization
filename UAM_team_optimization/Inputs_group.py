from openmdao.api import Group, IndepVarComp, Problem
import numpy as np
from UAM_team_optimization.Propulsion_group import PropulsionGroup

# from UAM_team_optimization.components.Propulsion.propulsion_comp import wing_left_outer_prop_thrust_coeff, wing_left_inner_prop_thrust_coeff,tail_left_prop_thrust_coeff
# from UAM_team_optimization.components.Propulsion.propulsion_comp import wing_right_outer_prop_thrust_coeff, wing_right_inner_prop_thrust_coeff,tail_right_prop_thrust_coeff
# from test_run import stuff
# my_shape = (1,)
# inputs_prob = Problem()

# propulsion_group = PropulsionGroup(
#     shape = my_shape
# )
# inputs_prob.model.add_subsystem('propulsion_group', propulsion_group,promotes = ['*'])
# inputs_prob.setup(check=True)
# inputs_prob['motor_group.mass'] = 120.
# inputs_prob['motor_group.angular_speed'] = 120.
# inputs_prob['motor_group.normalized_torque'] = 0.6
# inputs_prob['preprocess_group.speed'] = 67. * 0.25


class InputsGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = IndepVarComp()

# Initial values for optimization:
# Adding Input variables which are the outputs of input_comp

# Atmospheric inital values:
        comp.add_output('v_inf' , val= 60)
        comp.add_output('q' , val= 250)

# Wing inital values:
        comp.add_output('wing_alpha', val = 0.05)
        comp.add_output('wing_CLa', val = 2*np.pi)
        comp.add_output('wing_CL0', val = 0.2)
        comp.add_output('wing_CD0', val = 0.015)
        comp.add_output('wing_e', val = 0.85)
        comp.add_output('wing_AR', val = 8 )
        comp.add_output('wing_area', val = 25 )
        comp.add_output('wing_tc', val = 0.12 )

# Tail inital values:
        comp.add_output('tail_alpha', val = 0)
        comp.add_output('tail_CLa', val = 2*np.pi)
        comp.add_output('tail_CL0', val = 0.2)
        comp.add_output('tail_CD0', val = 0.015)
        comp.add_output('tail_e', val = 0.85)
        comp.add_output('tail_AR', val = 8 )
        comp.add_output('tail_area', val = 4 )
        comp.add_output('tail_tc', val = 0.12)

        comp.add_output('total_area', val = 29)

# Fuselage initial values:
        comp.add_output('fuselage_max_crossec_area', val = 7.22)
        comp.add_output('fuselage_length', val = 6.4)
        comp.add_output('fuselage_f', val = 0.886426)
        comp.add_output('fuselage_form_factor', val = 87)
        comp.add_output('fuselage_wetter_area', val = 52.05)

# Vertical tail initial values:
        comp.add_output('vertical_tail_mac', val = 1.074)
        comp.add_output('vertical_tail_tc', val = 0.188)
        comp.add_output('vertical_tail_area', val = 1.625803)
        
        

# Propeller inital values:
        comp.add_output('wing_prop_inner_rad',val = 0.8)
        comp.add_output('wing_prop_outer_rad',val = 0.8)
        comp.add_output('tail_prop_rad',val = 0.8)
        # comp.add_output('wing_left_inner_thrust_coeff', val = 0)#wing_left_inner_prop_thrust_coeff)
        # comp.add_output('wing_left_outer_thrust_coeff', val = 0)#inputs_prob['rotor_group.thrust_coeff']/7.75)
        # comp.add_output('tail_left_thrust_coeff', val =0)# tail_left_prop_thrust_coeff)
        # comp.add_output('wing_right_inner_thrust_coeff', val = 0)#wing_right_inner_prop_thrust_coeff)
        # comp.add_output('wing_right_outer_thrust_coeff', val =0)# wing_right_outer_prop_thrust_coeff)
        # comp.add_output('tail_right_thrust_coeff', val = 0)#tail_right_prop_group.rotor_group.thrust_coeff )

# Weights initial values:
        comp.add_output('w_design', val=26700.)
        comp.add_output('w_pax', val=900.)
        comp.add_output('w_else', val=18000.) # all empty weight EXCEPT tail, wing, PAX
        comp.add_output('load_factor', val=3.8)
        comp.add_output('x_wingc4', val=1.)
        comp.add_output('x_tailc4', val=2.)
        comp.add_output('x_else', val=3.)
        comp.add_output('x_pax', val=4.)
        comp.add_output('MAC', val=1.)
        comp.add_output('w_tail')

# Economics initial values:
        comp.add_output('EngRt' , val= 40)
        comp.add_output('MfgRt' , val= 30)
        comp.add_output('ToolRt' , val= 21)
        comp.add_output('QcRt' , val= 37)
        comp.add_output('kwh' , val= 133)
        comp.add_output('kwhcost' , val= 137)
        comp.add_output('num_motor' , val= 12)
        self.add_subsystem('inputs_comp', comp, promotes=['*'])



