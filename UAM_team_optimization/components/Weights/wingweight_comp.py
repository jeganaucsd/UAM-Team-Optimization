from openmdao.api import ExplicitComponent


class WingWeightComp(ExplicitComponent):
    def initialize(self):
        self.options.declare('rho', types=float)

    def setup(self):
        self.add_input('wing_area')
        self.add_input('wing_tc')
        self.add_input('wing_AR')
        self.add_input('load_factor')
        self.add_input('w_design')
        self.add_input('v_inf')
        self.add_output('w_wing')

        self.declare_partials('w_wing', 'wing_area')
        self.declare_partials('w_wing', 'wing_tc')
        self.declare_partials('w_wing', 'wing_AR')
        self.declare_partials('w_wing', 'load_factor')
        self.declare_partials('w_wing', 'w_design')
        self.declare_partials('w_wing', 'v_inf')

    def compute(self, inputs, outputs):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        v_inf = inputs['v_inf']

        outputs['w_wing'] = 0.036* \
                            (wing_area**0.758)* \
                            (wing_AR**0.6)* \
                            ((0.5*rho*v_inf*v_inf)**0.006)* \
                            ((100*wing_tc)**-0.3)* \
                            ((load_factor*w_design)**0.49)

    def compute_partials(self, inputs, partials):
        rho = self.options['rho']

        wing_area = inputs['wing_area']
        wing_tc = inputs['wing_tc']
        wing_AR = inputs['wing_AR']
        w_design = inputs['w_design']
        load_factor = inputs['load_factor']
        v_inf = inputs['v_inf']

        partials['w_wing', 'wing_area'] = 0.036* \
                                               0.758*(wing_area**(1-0.758))* \
                                               (wing_AR**0.6)* \
                                               ((0.5*rho*v_inf*v_inf)**0.006)* \
                                               ((100*wing_tc)**-0.3)* \
                                               ((load_factor*w_design)**0.49)

        partials['w_wing', 'wing_tc'] = 0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**0.6)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             100*(-0.3)*((100*wing_tc)**(-0.3-1))* \
                                             ((load_factor*w_design)**0.49)

        partials['w_wing', 'wing_AR'] = 0.6*0.036* \
                                             (wing_area**0.758)* \
                                             (wing_AR**-0.4)* \
                                             ((0.5*rho*v_inf*v_inf)**0.006)* \
                                             ((100*wing_tc)**-0.3)* \
                                             ((load_factor*w_design)**0.49)

        partials['w_wing', 'load_factor'] = 0.036* \
                                                 (wing_area**0.758)* \
                                                 (wing_AR**0.6)* \
                                                 ((0.5*rho*v_inf*v_inf)**0.006)* \
                                                 ((100*wing_tc)**-0.3)* \
                                                 w_design*0.49*((load_factor*w_design)**(1-0.49))

        partials['w_wing', 'w_design'] = 0.036* \
                                              (wing_area**0.758)* \
                                              (wing_AR**0.6)* \
                                              ((0.5*rho*v_inf*v_inf)**0.006)* \
                                              ((100*wing_tc)**-0.3)* \
                                              load_factor*0.49*((load_factor*w_design)**(1-0.49))

        partials['w_wing', 'v_inf'] = 0.036* \
                                           (wing_area**0.758)* \
                                           (wing_AR**0.6)* \
                                           ((100*wing_tc)**-0.3)* \
                                           ((load_factor*w_design)**0.49)* \
                                           ((0.5*rho)**0.006)* \
                                           (0.012)* \
                                           (v_inf**(0.012 - 1))
