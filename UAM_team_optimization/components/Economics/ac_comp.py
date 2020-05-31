import numpy as np
from openmdao.api import ExplicitComponent


class AcComp(ExplicitComponent):

    def setup(self):
        self.add_input('LaborCost')
        self.add_input('StructCost')
        self.add_input('quantity')
               
        self.add_output('Ac')


    def compute(self, inputs, outputs):
        
        LaborCost = inputs['LaborCost']
        StructCost = inputs['StructCost']
        quantity = inputs['quantity']


        outputs['Ac'] = 1.1 * (StructCost + LaborCost) / quantity
