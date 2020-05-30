from openmdao.api import Group, IndepVarComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp
from UAM_team_optimization.components.Weights.grossweight_comp import GrossWeightComp

class MotionEquationsGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)
        self.options.declare('options_dictionary')

        self.promotes = None
    def setup(self):
        shape = self.options['shape']
        # module = self.options['options_dictionary']
        # 
        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'vertical_hover_equilibrium',
            constant = 0.,
            coeffs_dict = dict(
                total_thrust = 1.,
                GrossWeight = -1.,
            )
        )
        self.add_subsystem('vertical_hover_equilibrium_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape =shape,
            out_name = 'vertical_cruise_equilibrium',
            constant = 0.,
            coeffs_dict = dict(
                total_lift = 1.,
                GrossWeight = -1.,
            )
        )
        self.add_subsystem('vertical_cruise_equilibrium', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape =shape,
            out_name = 'horizontal_cruise_equilibrium',
            constant = 0.,
            coeffs_dict = dict(
                total_thrust = 1.,
                total_drag = -1.,
            )
        )
        self.add_subsystem('horizontal_cruise_equilibrium', comp, promotes = ['*'])