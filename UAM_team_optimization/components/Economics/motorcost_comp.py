import numpy as np
from openmdao.api import ExplicitComponent


class MotorCostComp(ExplicitComponent):

    def setup(self):

        self.add_input('num_motor')
        self.add_input('quantity')
        self.add_output('MotorCost')

        self.declare_partials('MotorCost', 'quantity')


        
    def compute(self, inputs, outputs):
        
        num_motor = inputs['num_motor']
        quantity = inputs['quantity']

        outputs['MotorCost'] = 40000 * num_motor * quantity

    def compute_partials(self, inputs, partials):
       
        num_motor = inputs['num_motor']
        quantity = inputs['quantity']

        partials['MotorCost', 'quantity'] = 40000 * num_motor