from openmdao.api import ExplicitComponent


class QComp(ExplicitComponent):
    def initialize(self):
        self.options.declare('rho', types=float)

    def setup(self):
        self.add_input('v_inf')
        self.add_output('q')

        self.declare_partials('q', 'v_inf')

    def compute(self, inputs, outputs):
        rho = self.options['rho']
        v_inf = inputs['v_inf']

        outputs['q'] = 0.5 * rho * v_inf**2.

    def compute_partials(self, inputs, partials):
        rho = self.options['rho']
        v_inf = inputs['v_inf']

        partials['q', 'v_inf'] = rho * v_inf
