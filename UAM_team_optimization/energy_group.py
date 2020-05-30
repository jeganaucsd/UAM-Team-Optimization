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
