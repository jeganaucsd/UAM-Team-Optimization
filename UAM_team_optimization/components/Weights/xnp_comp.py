from openmdao.api import ExplicitComponent
import numpy as np

class XNPComp(ExplicitComponent):

    def setup(self):
        self.add_input('wing_area')
        self.add_input('tail_area')
        self.add_input('x_wingc4')
        self.add_input('x_tailc4')
        self.add_output('xnp')

        self.declare_partials('xnp', 'wing_area')
        self.declare_partials('xnp', 'tail_area')
        self.declare_partials('xnp', 'x_wingc4')
        self.declare_partials('xnp', 'x_tailc4')

    def compute(self, inputs, outputs):
        wing_area = inputs['wing_area']
        tail_area = inputs['tail_area']
        x_wingc4 = inputs['x_wingc4']
        x_tailc4 = inputs['x_tailc4']

        outputs['xnp'] = (wing_area*x_wingc4 + tail_area*x_tailc4) / (wing_area + tail_area)

    def compute_partials(self, inputs, partials):
        wing_area = inputs['wing_area']
        tail_area = inputs['tail_area']
        x_wingc4 = inputs['x_wingc4']
        x_tailc4 = inputs['x_tailc4']

        partials['xnp', 'x_wingc4'] =
        partials['xnp', 'x_tailc4'] =
        partials['xnp', 'wing_area'] =
        partials['xnp', 'tail_area'] = 
