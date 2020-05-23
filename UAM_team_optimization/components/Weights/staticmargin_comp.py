from openmdao.api import ExplicitComponent
import numpy as np

class StaticMarginComp(ExplicitComponent):

    def setup(self):
        self.add_input('xcg')
        self.add_input('xnp')
        self.add_input('MAC')
        self.add_output('staticmargin')

        self.declare_partials('staticmargin','xcg')
        self.declare_partials('staticmargin','xnp')
        self.declare_partials('staticmargin','MAC')

    def compute(self, inputs, outputs):

        xcg = inputs['xcg']
        xnp = inputs['xnp']
        MAC = inputs['MAC']

        outputs['staticmargin'] = (1. / MAC) * (xnp - xcg)

    def compute_partials(self, inputs, partials):

        xcg = inputs['xcg']
        xnp = inputs['xnp']
        MAC = inputs['MAC']

        partials['staticmargin','xcg'] = (1. / MAC) * (-1.)
        partials['staticmargin','xnp'] = (1. / MAC) * (1.)
        partials['staticmargin','MAC'] = (xnp - xcg) * (-1.) * (MAC**-2.)
