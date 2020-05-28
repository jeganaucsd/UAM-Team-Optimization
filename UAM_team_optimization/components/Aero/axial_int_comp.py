from openmdao.api import ExplicitComponent
from UAM_team_optimization.Propulsion_group import PropulsionGroup
import numpy as np

class AxialIntComp(ExplicitComponent):
# cl for section of the tail that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('tail_right_thrust_coeff')
        self.add_input('tail_left_thrust_coeff')
        self.add_input('wing_right_outer_thrust_coeff')
        self.add_input('wing_right_inner_thrust_coeff')
        self.add_input('wing_left_outer_thrust_coeff')
        self.add_input('wing_left_inner_thrust_coeff')
        
        self.add_output('tail_right_axial_int_fac')
        self.add_output('tail_left_axial_int_fac')
        self.add_output('wing_right_outer_axial_int_fac')
        self.add_output('wing_right_inner_axial_int_fac')
        self.add_output('wing_left_outer_axial_int_fac')
        self.add_output('wing_left_inner_axial_int_fac')
        # self.add_output('average_wing_axial_int_fac')
        # self.add_output('average_tail_axial_int_fac')

        self.declare_partials('tail_right_axial_int_fac','tail_right_thrust_coeff')
        self.declare_partials('tail_left_axial_int_fac','tail_left_thrust_coeff')
        self.declare_partials('wing_right_outer_axial_int_fac','wing_right_outer_thrust_coeff')
        self.declare_partials('wing_right_inner_axial_int_fac','wing_right_inner_thrust_coeff')
        self.declare_partials('wing_left_outer_axial_int_fac','wing_left_outer_thrust_coeff')
        self.declare_partials('wing_left_inner_axial_int_fac','wing_left_inner_thrust_coeff')

    def compute(self, inputs, outputs):
        tail_right_thrust_coeff = inputs['tail_right_thrust_coeff']
        tail_left_thrust_coeff = inputs['tail_left_thrust_coeff']
        wing_right_outer_thrust_coeff = inputs['wing_right_outer_thrust_coeff']
        wing_right_inner_thrust_coeff = inputs['wing_right_inner_thrust_coeff']
        wing_left_outer_thrust_coeff = inputs['wing_left_outer_thrust_coeff']
        wing_left_inner_thrust_coeff = inputs['wing_left_inner_thrust_coeff']

        # average_wing_axial_int_fac = inputs[['wing_right_outer_thrust_coeff'],['wing_right_inner_thrust_coeff'],['wing_left_outer_thrust_coeff'],['wing_left_inner_thrust_coeff']]
        # average_tail_axial_int_fac = inputs['tail_right_axial_int_fac','tail_left_axial_int_fac']

        outputs['tail_right_axial_int_fac'] = (-1 + np.sqrt(1 + tail_right_thrust_coeff**2))/2
        outputs['tail_left_axial_int_fac'] = (-1 + np.sqrt(1 + tail_left_thrust_coeff**2))/2
        outputs['wing_right_outer_axial_int_fac'] = (-1 + np.sqrt(1 + wing_right_outer_thrust_coeff**2))/2
        outputs['wing_right_inner_axial_int_fac'] = (-1 + np.sqrt(1 + wing_right_inner_thrust_coeff**2))/2
        outputs['wing_left_outer_axial_int_fac'] = (-1 + np.sqrt(1 + wing_left_outer_thrust_coeff**2))/2
        outputs['wing_left_inner_axial_int_fac'] = (-1 + np.sqrt(1 + wing_left_inner_thrust_coeff**2))/2
        
        # outputs['average_wing_axial_int_fac'] = ((-1 + np.sqrt(1 + wing_right_outer_thrust_coeff**2))/2 + (-1 + np.sqrt(1 + wing_right_inner_thrust_coeff**2))/2 + (-1 + np.sqrt(1 + wing_left_outer_thrust_coeff**2))/2 + (-1 + np.sqrt(1 + wing_left_inner_thrust_coeff**2))/2)/4

    def compute_partials(self, inputs, partials):
        tail_right_thrust_coeff = inputs['tail_right_thrust_coeff']
        tail_left_thrust_coeff = inputs['tail_left_thrust_coeff']
        wing_right_outer_thrust_coeff = inputs['wing_right_outer_thrust_coeff']
        wing_right_inner_thrust_coeff = inputs['wing_right_inner_thrust_coeff']
        wing_left_outer_thrust_coeff = inputs['wing_left_outer_thrust_coeff']
        wing_left_inner_thrust_coeff = inputs['wing_left_inner_thrust_coeff']

        partials['tail_right_axial_int_fac', 'tail_right_thrust_coeff'] = tail_right_thrust_coeff/(2*np.sqrt(1 + tail_right_thrust_coeff**2))
        partials['tail_left_axial_int_fac', 'tail_left_thrust_coeff'] = tail_left_thrust_coeff/(2*np.sqrt(1 + tail_left_thrust_coeff**2))
        partials['wing_right_outer_axial_int_fac', 'wing_right_outer_thrust_coeff'] = wing_right_outer_thrust_coeff/(2*np.sqrt(1 + wing_right_outer_thrust_coeff**2))
        partials['wing_right_inner_axial_int_fac', 'wing_right_inner_thrust_coeff'] = wing_right_inner_thrust_coeff/(2*np.sqrt(1 + wing_right_inner_thrust_coeff**2))
        partials['wing_left_outer_axial_int_fac', 'wing_left_outer_thrust_coeff'] = wing_left_outer_thrust_coeff/(2*np.sqrt(1 + wing_left_outer_thrust_coeff**2))
        partials['wing_left_inner_axial_int_fac', 'wing_left_inner_thrust_coeff'] = wing_left_inner_thrust_coeff/(2*np.sqrt(1 + wing_left_inner_thrust_coeff**2))
        
 