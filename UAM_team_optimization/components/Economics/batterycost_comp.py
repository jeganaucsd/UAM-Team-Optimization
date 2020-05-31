import numpy as np
from openmdao.api import ExplicitComponent


class BatteryCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('kwh')
        self.add_input('kwhcost')
        self.add_input('quantity')
        self.add_output('BatteryCost')

        self.declare_partials('BatteryCost', 'quantity')


        
    def compute(self, inputs, outputs):
        
        kwh = inputs['kwh']
        kwhcost = inputs['kwhcost']
        quantity = inputs['quantity']

        outputs['BatteryCost'] = kwh * kwhcost * q

    def compute_partials(self, inputs, partials):
       
        kwh = inputs['kwh']
        kwhcost = inputs['kwhcost']
        quantity = inputs['quantity']

        partials['BatteryCost', 'quantity'] = kwh * kwhcost