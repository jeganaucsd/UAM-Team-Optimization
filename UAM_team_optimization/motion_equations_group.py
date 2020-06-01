from openmdao.api import Group, IndepVarComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp, LinearPowerCombinationComp
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
                hover_total_thrust = 1.,
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
        self.add_subsystem('vertical_cruise_equilibrium_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape =shape,
            out_name = 'horizontal_cruise_equilibrium',
            constant = 0.,
            coeffs_dict = dict(
                cruise_total_thrust = 1.,
                total_drag = -1.,
            )
        )
        self.add_subsystem('horizontal_cruise_equilibrium_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'cruise_rolling_moment_equilibrium',
            terms_list=[
                (0.2, dict(
                    cruise_wing_right_inner_thrust = 1.,
                    wing_span = 1.,
                )),
                (0.5, dict(
                    cruise_wing_right_outer_thrust = 1.,
                    wing_span = 1.,
                )),
                (0.5, dict(
                    cruise_tail_right_thrust = 1.,
                    tail_span = 1.,
                )),
                (-0.2, dict(
                    cruise_wing_left_inner_thrust = 1.,
                    wing_span = 1.,
                )),
                (-0.5, dict(
                    cruise_wing_left_outer_thrust = 1.,
                    wing_span = 1.,
                )),
                (-0.5, dict(
                    cruise_tail_left_thrust = 1.,
                    tail_span = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('cruise_rolling_moment_equilibrium_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape =shape,
            out_name = 'wing_lift_moment_arm',
            constant = 0.,
            coeffs_dict = dict(
                xcg = 1.,
                nose_wing_c4 = -1.,
            )
        )
        self.add_subsystem('wing_lift_moment_arm_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape =shape,
            out_name = 'tail_lift_moment_arm',
            constant = 0.,
            coeffs_dict = dict(
                nose_tail_c4= 1.,
                xcg = -1.,
            )
        )
        self.add_subsystem('tail_lift_moment_arm_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'pitching_moment_equilibrium',
            terms_list=[
                (1, dict(
                    wing_lift_moment_arm = 1.,
                    wing_lift = 1.,
                )),
                (-1, dict(
                    tail_lift_moment_arm = 1.,
                    tail_lift = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('pitching_moment_equilibrium_comp', comp, promotes = ['*'])