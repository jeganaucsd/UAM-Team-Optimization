import numpy as np
from openmdao.api import ExplicitComponent


class AvionicsCostComp(ExplicitComponent):

    def setup(self):

        self.add_input('quantity')
        self.add_output('AvionicsCost')

        self.declare_partials('AvionicsCost', 'quantity')


        
    def compute(self, inputs, outputs):
        
        quantity = inputs['quantity']

        outputs['AvionicsCost'] = 120000 * quantity

    def compute_partials(self, inputs, partials):
       
        quantity = inputs['quantity']

        partials['AvionicsCost', 'quantity'] = 120000