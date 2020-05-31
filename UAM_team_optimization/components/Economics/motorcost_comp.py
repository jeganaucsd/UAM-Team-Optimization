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

<<<<<<< HEAD
        outputs['MotorCost'] = 40000 * num_motor * quantity
=======
        outputs['MotorCost'] = 10000 * num_motor * q
>>>>>>> 8623324c1963ab7102a64cdcd29b94deb399d44a

    def compute_partials(self, inputs, partials):
       
        num_motor = inputs['num_motor']
        quantity = inputs['quantity']

<<<<<<< HEAD
        partials['MotorCost', 'quantity'] = 40000 * num_motor
=======
        partials['MotorCost', 'q'] = 10000 * num_motor
>>>>>>> 8623324c1963ab7102a64cdcd29b94deb399d44a
