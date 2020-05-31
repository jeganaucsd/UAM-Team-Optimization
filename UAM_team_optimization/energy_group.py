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
            out_name = 'cruise_average_prop_efficiency',
            terms_list=[
                (1/6, dict(
                    cruise_tail_right_eff = 1.,
                )),
                (1/6, dict(
                    cruise_tail_left_eff = 1.,
                )),
                (1/6, dict(
                    cruise_wing_right_outer_eff = 1.,
                )),
                (1/6, dict(
                    cruise_wing_right_inner_eff = 1.,
                )),
                (1/6, dict(
                    cruise_wing_left_outer_eff = 1.,
                )),
                (1/6, dict(
                    cruise_wing_left_inner_eff = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('cruise_average_prop_efficiency_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'hover_average_prop_efficiency',
            terms_list=[
                (1/6, dict(
                    hover_tail_right_eff = 1.,
                )),
                (1/6, dict(
                    hover_tail_left_eff = 1.,
                )),
                (1/6, dict(
                    hover_wing_right_outer_eff = 1.,
                )),
                (1/6, dict(
                    hover_wing_right_inner_eff = 1.,
                )),
                (1/6, dict(
                    hover_wing_left_outer_eff = 1.,
                )),
                (1/6, dict(
                    hover_wing_left_inner_eff = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('hover_average_prop_efficiency_comp', comp, promotes = ['*'])

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'cruise_total_power',
            terms_list=[
                (1, dict(
                    cruise_tail_right_power = 1.,
                )),
                (1, dict(
                    cruise_tail_left_power = 1.,
                )),
                (1, dict(
                    cruise_wing_right_outer_power = 1.,
                )),
                (1, dict(
                    cruise_wing_right_inner_power = 1.,
                )),
                (1, dict(
                    cruise_wing_left_outer_power = 1.,
                )),
                (1, dict(
                    cruise_wing_left_inner_power = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('cruise_total_power_comp', comp, promotes = ['*']) 

        comp = LinearPowerCombinationComp(
            shape = shape,
            out_name = 'hover_total_power',
            terms_list=[
                (1, dict(
                    hover_tail_right_power = 1.,
                )),
                (1, dict(
                    hover_tail_left_power = 1.,
                )),
                (1, dict(
                    hover_wing_right_outer_power = 1.,
                )),
                (1, dict(
                    hover_wing_right_inner_power = 1.,
                )),
                (1, dict(
                    hover_wing_left_outer_power = 1.,
                )),
                (1, dict(
                    hover_wing_left_inner_power = 1.,
                )),
            ],
            constant = 0.,          
        )
        self.add_subsystem('hover_total_power_comp', comp, promotes = ['*'])

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
                cruise_total_power = 1.,
            )
        )
        self.add_subsystem('cruise_energy_expenditure_comp', comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'hover_energy_expenditure',
            powers_dict=dict(
                hover_time = 1.,
                hover_total_power = 1.,
            )
        )
        self.add_subsystem('hover_energy_expenditure_comp', comp, promotes = ['*'])

        comp =  LinearCombinationComp(
            shape = shape,
            out_name = 'energy_expenditure_per_trip',
            constant = 0.,
            coeffs_dict=dict(
                hover_energy_expenditure = 1.,
                cruise_energy_expenditure = 1.,                    
            )
        )
        self.add_subsystem('energy_expenditure_per_trip_comp',comp, promotes = ['*'])

        comp = LinearCombinationComp(
            shape = shape,
            out_name = 'energy_remaining',
            constant = 0.,
            coeffs_dict=dict(
                total_avail_energy =1.,
                cruise_energy_expenditure = -1.,
                hover_energy_expenditure = -1.,
            )
        )
        self.add_subsystem('energy_remaining_comp', comp, promotes=['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'trips_per_charge',
            powers_dict=dict(
                total_avail_energy = 1.,
                energy_expenditure_per_trip = -1.,
            )
        )
        self.add_subsystem('trips_per_charge_comp', comp, promotes=['*'])
       
        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'aircraft_range',
            coeff = 1/1000,
            powers_dict = dict(
                trip_length = 1.,
                trips_per_charge = 1.,
            )
        )
        self.add_subsystem('aircraft_range_comp', comp, promotes=['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'design_range_energy_expenditure',
            coeff = 1.,
            powers_dict=dict(
                trip_length = 1.,
                GrossWeight = 1.,
                cruise_average_prop_efficiency = -1.,
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

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'Electric_Range_Equation',
            coeff = 1.,
            powers_dict=dict(
                cruise_average_prop_efficiency = 1.,
                batter_energy_density = 1.,
                lift_drag_ratio = 1.,
                battery_mass = 1.,
                GrossWeight = -1.,
            )
        )
        self.add_subsystem('Electric_Range_Equation_comp', comp, promotes = ['*'])

