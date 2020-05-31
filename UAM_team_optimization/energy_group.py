from openmdao.api import Group, IndepVarComp,ExecComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp


class EnergyGroup(Group):
    
    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        from openmdao.api import Group, IndepVarComp,ExecComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp, LinearPowerCombinationComp


class EnergyGroup(Group):
    
    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'total_avail_energy',
            coeff = 3600.,
            powers_dict=dict(
                battery_mass = 1.,
                batter_energy_density = 1.,
            )
        )
        self.add_subsystem('total_avail_energy_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'average_prop_efficiency',
            terms_list=[
                (1/6, dict(
                    tail_right_eff = 1.,
                )),
                (1/6, dict(
                    tail_left_eff = 1.,
                )),
                (1/6, dict(
                    wing_right_outer_eff = 1.,
                )),
                (1/6, dict(
                    wing_right_inner_eff = 1.,
                )),
                (1/6, dict(
                    wing_left_outer_eff = 1.,
                )),
                (1/6, dict(
                    wing_left_inner_eff = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('average_prop_efficiency_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'total_power',
            terms_list=[
                (1, dict(
                    tail_right_power = 1.,
                )),
                (1, dict(
                    tail_left_power = 1.,
                )),
                (1, dict(
                    wing_right_outer_power = 1.,
                )),
                (1, dict(
                    wing_right_inner_power = 1.,
                )),
                (1, dict(
                    wing_left_outer_power = 1.,
                )),
                (1, dict(
                    wing_left_inner_power = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('total_power_comp', comp, promotes = ['*']) 

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'cruise_time',
            coeff = 1.,
            powers_dict = dict(
                trip_length = 1.,
                v_inf = -1.,
            )
        )
        self.add_subsystem('cruise_time', comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'cruise_energy_expenditure',
            coeff = 1.,
            powers_dict=dict(
                cruise_time = 1.,
                total_power = 1.,
            )
        )
        self.add_subsystem('cruise_energy_expenditure_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'energy_remaining',
            constant = 0.,
            coeffs_dict=dict(
                total_avail_energy =1.,
                cruise_energy_expenditure = -1.,
            )
        )
        self.add_subsystem('energy_remaining_comp', comp, promotes=['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'design_range_energy_expenditure',
            coeff = 1.,
            powers_dict=dict(
                trip_length = 1.,
                GrossWeight = 1.,
                average_prop_efficiency = -1.,
                lift_drag_ratio = -1.,
            )
        )
        self.add_subsystem('design_range_energy_expenditure_comp', comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'energy_remaining_1',
            constant = 0.,
            coeffs_dict=dict(
                total_avail_energy =1.,
                design_range_energy_expenditure = -1.,
            )
        )
        self.add_subsystem('energy_remaining_1_comp', comp, promotes=['*'])

        # comp = PowerCombinationComp(
        #     shape = shape,
        #     out_name = 'Range',
        #     coeff = 1.,
        #     powers_dict=dict(
        #         average_prop_efficiency = 1.,
        #         batter_energy_density = 1.,
        #         lift_drag_ratio = 1.,
        #         battery_mass = 1.,
        #         GrossWeight = -1.,
        #     )
        # )
        # self.add_subsystem('Range_comp', comp, promotes = ['*'])

