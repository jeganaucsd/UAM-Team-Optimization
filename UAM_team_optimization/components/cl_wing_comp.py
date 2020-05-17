from openmdao.api import ExplicitComponent


class CLWingComp(ExplicitComponent):
# cl for section of the wing that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('wing_alpha')
        self.add_input('wing_CLa')
        self.add_input('wing_CL0')
        self.add_output('wing_CL')

        self.declare_partials('wing_CL','wing_alpha')
        self.declare_partials('wing_CL','wing_CLa')
        self.declare_partials('wing_CL','wing_CL0')

    def compute(self, inputs, outputs):
        wing_alpha = inputs['wing_alpha']
        wing_CLa = inputs['wing_CLa']
        wing_CL0 = inputs['wing_CL0']

        outputs['wing_CL'] = wing_CLa * wing_alpha + wing_CL0

    def compute_partials(self, inputs, partials):
        wing_alpha = inputs['wing_alpha']
        wing_CLa = inputs['wing_CLa']
        wing_CL0 = inputs['wing_CL0']

        partials['wing_CL', 'wing_alpha'] = wing_CLa
        partials['wing_CL', 'wing_CLa'] = wing_alpha
        partials['wing_CL', 'wing_CL0'] = 1.
 