from openmdao.api import ExplicitComponent


class TailWeightComp(ExplicitComponent):
    def initialize(self):
        self.options.declare('rho', types=float)

    def setup(self):
        self.add_input('tail_area')
        self.add_input('tail_tc')
        self.add_input('tail_AR')
        self.add_input('load_factor')
        self.add_input('w_design')
        self.add_input('v_inf')
        self.add_output('w_tail')

        self.declare_partials('w_tail', 'tail_area')
        self.declare_partials('w_tail', 'tail_tc')
        self.declare_partials('w_tail', 'tail_AR')
        self.declare_partials('w_tail', 'load_factor')
        self.declare_partials('w_tail', 'w_design')
        self.declare_partials('w_tail', 'v_inf')

    def compute(self, inputs, outputs):
        rho = self.options['rho']

        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        v_inf = inputs['v_inf']

        outputs['w_tail'] = 0.016* \
                            ((load_factor*w_design)**0.414)* \
                            ((0.5*rho*v_inf*v_inf)**0.168)* \
                            (tail_area**0.896)* \
                            ((100*tail_tc)**-0.12)* \
                            (tail_AR**0.043)

    def compute_partials(self, inputs, partials):
        rho = self.options['rho']

        tail_area = inputs['tail_area']
        tail_tc = inputs['tail_tc']
        tail_AR = inputs['tail_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        v_inf = inputs['v_inf']

        partials['w_tail', 'tail_area'] = 0.016* \
                                               ((load_factor*w_design)**0.414)* \
                                               ((0.5*rho*v_inf*v_inf)**0.168)* \
                                               0.896*(tail_area**(1-0.896))* \
                                               ((100*tail_tc)**-0.12)* \
                                               (tail_AR**0.043)

        partials['w_tail', 'tail_tc'] = 0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             100*(-0.12)*((100*tail_tc)**(-0.12-1))* \
                                             (tail_AR**0.043)

        partials['w_tail', 'tail_AR'] = 0.043*0.016* \
                                             ((load_factor*w_design)**0.414)* \
                                             ((0.5*rho*v_inf*v_inf)**0.168)* \
                                             (tail_area**0.896)* \
                                             ((100*tail_tc)**-0.12)* \
                                             (tail_AR**-0.957)

        partials['w_tail', 'load_factor'] = 0.016* \
                                                 w_design*0.414*((load_factor*w_design)**(1-0.414))* \
                                                 ((0.5*rho*v_inf*v_inf)**0.168)* \
                                                 (tail_area**0.896)* \
                                                 ((100*tail_tc)**-0.12)* \
                                                 (tail_AR**0.043)

        partials['w_tail', 'w_design'] = 0.016* \
                                              load_factor*0.414*((load_factor*w_design)**(1-0.414))* \
                                              ((0.5*rho*v_inf*v_inf)**0.168)* \
                                              (tail_area**0.896)* \
                                              ((100*tail_tc)**-0.12)* \
                                              (tail_AR**0.043)

        partials['w_tail', 'v_inf'] = 0.016* \
                                           ((load_factor*w_design)**0.414)* \
                                           (tail_area**0.896)* \
                                           ((100*tail_tc)**-0.12)* \
                                           (tail_AR**0.043)* \
                                           ((0.5*rho)**0.168)* \
                                           (2*0.168)* \
                                           (v_inf**(2*0.168 - 1))
