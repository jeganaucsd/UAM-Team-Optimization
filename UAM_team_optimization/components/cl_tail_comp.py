from openmdao.api import ExplicitComponent


class CLTailComp(ExplicitComponent):
# cl for section of the tail that is NOT affected by propeller slip stream
    def setup(self):
        self.add_input('tail_alpha')
        self.add_input('tail_CLa')
        self.add_input('tail_CL0')
        self.add_output('tail_CL')

        self.declare_partials('tail_CL','tail_alpha')
        self.declare_partials('tail_CL','tail_CLa')
        self.declare_partials('tail_CL','tail_CL0')

    def compute(self, inputs, outputs):
        tail_alpha = inputs['tail_alpha']
        tail_CLa = inputs['tail_CLa']
        tail_CL0 = inputs['tail_CL0']

        outputs['tail_CL'] = tail_CLa * tail_alpha + tail_CL0

    def compute_partials(self, inputs, partials):
        tail_alpha = inputs['tail_alpha']
        tail_CLa = inputs['tail_CLa']
        tail_CL0 = inputs['tail_CL0']

        partials['tail_CL', 'tail_alpha'] = tail_CLa
        partials['tail_CL', 'tail_CLa'] = tail_alpha
        partials['tail_CL', 'tail_CL0'] = 1.
 