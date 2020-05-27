from openmdao.api import ExplicitComponent
import numpy as np

class XCGComp(ExplicitComponent):

    def setup(self):
        self.add_input('w_wing')
        self.add_input('w_tail')
        self.add_input('w_else')
        self.add_input('w_pax')
        self.add_input('x_wingc4')
        self.add_input('x_tailc4')
        self.add_input('x_else')
        self.add_input('x_pax')
        self.add_input('GrossWeight')
        self.add_output('xcg')

        self.declare_partials('xcg', 'w_wing')
        self.declare_partials('xcg', 'w_tail')
        self.declare_partials('xcg', 'w_else')
        self.declare_partials('xcg', 'w_pax')
        self.declare_partials('xcg', 'x_wingc4')
        self.declare_partials('xcg', 'x_tailc4')
        self.declare_partials('xcg', 'x_else')
        self.declare_partials('xcg', 'x_pax')
        self.declare_partials('xcg', 'GrossWeight')

    def compute(self, inputs, outputs):

        w_wing = inputs['w_wing']
        w_tail = inputs['w_tail']
        w_else = inputs['w_else']
        w_pax = inputs['w_pax']
        x_wingc4 = inputs['x_wingc4']
        x_tailc4 = inputs['x_tailc4']
        x_else = inputs['x_else']
        x_pax = inputs['x_pax']
        GrossWeight = inputs['GrossWeight']

        outputs['xcg'] = (1. / GrossWeight) * (w_wing * x_wingc4 + \
                                               w_tail * x_tailc4 + \
                                               w_else * x_else + \
                                               w_pax * x_pax)

    def compute_partials(self, inputs, partials):

        w_wing = inputs['w_wing']
        w_tail = inputs['w_tail']
        w_else = inputs['w_else']
        w_pax = inputs['w_pax']
        x_wingc4 = inputs['x_wingc4']
        x_tailc4 = inputs['x_tailc4']
        x_else = inputs['x_else']
        x_pax = inputs['x_pax']
        GrossWeight = inputs['GrossWeight']

        partials['xcg', 'w_wing'] = x_wingc4 / GrossWeight
        partials['xcg', 'w_tail'] =  x_tailc4 / GrossWeight
        partials['xcg', 'w_else'] = x_else / GrossWeight
        partials['xcg', 'w_pax'] =  x_pax / GrossWeight
        partials['xcg', 'x_wingc4'] = w_wing / GrossWeight
        partials['xcg', 'x_tailc4'] = w_tail / GrossWeight
        partials['xcg', 'x_pax'] = w_pax / GrossWeight
        partials['xcg', 'x_else'] = w_else / GrossWeight
        partials['xcg', 'GrossWeight'] = -1. * (GrossWeight**-2.) * \
                                               (w_wing * x_wingc4 + \
                                               w_tail * x_tailc4 + \
                                               w_else * x_else + \
                                               w_pax * x_pax)
