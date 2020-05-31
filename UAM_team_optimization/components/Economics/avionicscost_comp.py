import numpy as np
from openmdao.api import ExplicitComponent


class AvionicsCostComp(ExplicitComponent):

    def setup(self):

        self.add_input('quantity')
        self.add_output('AvionicsCost')

        self.declare_partials('AvionicsCost', 'quantity')


        
    def compute(self, inputs, outputs):
        
        quantity = inputs['quantity']

<<<<<<< HEAD
        outputs['AvionicsCost'] = 120000 * quantity
=======
        outputs['AvionicsCost'] = 60000 * q
>>>>>>> 8623324c1963ab7102a64cdcd29b94deb399d44a

    def compute_partials(self, inputs, partials):
       
        quantity = inputs['quantity']

<<<<<<< HEAD
        partials['AvionicsCost', 'quantity'] = 120000
=======
        partials['AvionicsCost', 'q'] = 60000 
>>>>>>> 8623324c1963ab7102a64cdcd29b94deb399d44a
