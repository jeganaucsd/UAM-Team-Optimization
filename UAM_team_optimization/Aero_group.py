from openmdao.api import Group, IndepVarComp,ExecComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp, LinearPowerCombinationComp

from UAM_team_optimization.components.Aero.cl_wing_comp import CLWingComp
from UAM_team_optimization.components.Aero.cl_tail_comp import CLTailComp
from UAM_team_optimization.components.Aero.cdi_wing_comp import CDiWingComp
from UAM_team_optimization.components.Aero.cdi_tail_comp import CDiTailComp
from UAM_team_optimization.components.Aero.percent_blown_comp import PercentBlownComp
from UAM_team_optimization.components.Aero.axial_int_comp import AxialIntComp
from UAM_team_optimization.components.Aero.average_axial_int_comp import AverageAxialIntComp
# from UAM_team_optimization.components.Aero.test_cl_wing_comp import TestCLWingComp
# from UAM_team_optimization.components.Aero.test_cl_tail_comp import TestCLTailComp
# from UAM_team_optimization.components.Aero.test_cdi_wing_comp import TestCDiWingComp
# from UAM_team_optimization.components.Aero.test_cdi_tail_comp import TestCDiTailComp
# from UAM_team_optimization.components.Aero.test_percent_blown_comp import TestPercentBlownComp
# from UAM_team_optimization.components.Aero.test_axial_int_comp import TestAxialIntComp



class AeroGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)
        self.options.declare('options_dictionary')

        self.promotes = None
    def setup(self):
        shape = self.options['shape']
        # module = self.options['options_dictionary']
        # 
        comp = PercentBlownComp()
        self.add_subsystem('percent_blown_comp', comp, promotes=['*'])
        comp = AxialIntComp()
        self.add_subsystem('axial_int_comp', comp, promotes=['*'])
        comp = AverageAxialIntComp()
        self.add_subsystem('average_axial_int_comp', comp, promotes=['*'])
        comp = CLWingComp()
        self.add_subsystem('cl_wing_comp', comp, promotes=['*'])
        comp = CLTailComp()
        self.add_subsystem('cl_tail_comp', comp, promotes=['*'])
        comp = CDiWingComp()
        self.add_subsystem('cdi_wing_comp', comp, promotes=['*'])
        comp = CDiTailComp()
        self.add_subsystem('cdi_tail_comp', comp, promotes=['*'])
        # comp = ExecComp('wing_lift = wing_CL*q*wing_area')
        # self.add_subsystem('wing_lift_comp', comp, promotes= ['*'])
        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_lift',
            coeff = 0.5,
            powers_dict=dict(
                wing_CL=1.,
                density=1.,
                v_inf=2.,
                wing_area=1.,
            )
        )
        self.add_subsystem('wing_lift_comp', comp, promotes=['*'])
        
        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'tail_lift',
            coeff = 0.5,
            powers_dict=dict(
                tail_CL=1.,
                density = 1.,
                v_inf=2.,
                tail_area=1.,
            )
        )
        self.add_subsystem('tail_lift_comp', comp, promotes=['*'])
        
        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'total_lift',
            constant = 0.,
            coeffs_dict=dict(
                wing_lift =1.,
                tail_lift=1.,
            )
        )
        self.add_subsystem('total_lift_comp', comp, promotes=['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_Re',
            coeff = 1.,
            powers_dict=dict(
                density = 1.,
                v_inf = 1.,
                wing_chord = 1.,
                dynamic_viscosity = -1.,
            )
        )
        self.add_subsystem('wing_Re_comp', comp, promotes = ['*'])


        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'mach_number'
            coeff = 1.,
            powers_dict=dict(
                v_inf = 1.,
                sonic_speed = -1.
            )
        )
        self.add_subsystem('mach_number_comp',comp , promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_skin_friction',
            coeff = 1.328,
            powers_dict=dict(
                wing_Re = -0.5,
            )
        )
        self.add_subsystem('wing_skin_friction', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'wing_form_factor_1',
            terms_list=[
                (100, dict(
                    wing_tc = 4.,
                )),
                (0.6, dict(
                    wing_tc = 1.,
                    x_wingc4 = -1.,
                )),
            ],
            constant = 1.,          
        )
        self.add_subsystem('wing_form_factor_1', comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_form_factor_2',
            coeff = 1.34,
            powers_dict=dict(
                mach_number = 0.18
            )
        )
        self.add_subsystem('wing_form_factor_2', comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_form_factor',
            coeff = 1.,
            powers_dict=dict(
                wing_form_factor_1 = 1.,
                wing_form_factor_2 = 1.,
            )
        )
        self.add_subsystem('wing_form_factor', comp, promotes = ['*'])