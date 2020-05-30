from openmdao.api import Group, IndepVarComp
from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp

# from lsdo_utils.api import PowerCombinationComp, LinearCombinationComp
from UAM_team_optimization.components.Geometry.geometry_comp import GeometryComp
from UAM_team_optimization.components.Geometry.test_geometry_comp import TestGeometryComp 


class GeometryGroup(Group):

    def initialize(self):
        self.options.declare('shape', types=tuple)

    def setup(self):
        shape = self.options['shape']
        
        # 
        comp = GeometryComp()
        self.add_subsystem('geometry_comp', comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'wing_chord',
            coeff = 1.,
            powers_dict=dict(
                wing_area = 1.,
                wing_span = -1.,
            )
        )
        self.add_subsystem('wing_chord_comp',comp, promotes = ['*'])

        comp = PowerCombinationComp(
            shape = shape,
            out_name = 'tail_chord',
            coeff = 1.,
            powers_dict=dict(
                tail_area = 1.,
                tail_span = -1.,
            )
        )
        self.add_subsystem('tail_chord_comp', comp, promotes=['*'])