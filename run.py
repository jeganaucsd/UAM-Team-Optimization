<<<<<<< HEAD
# Maximize Profit w.r.t:
# Describe optimization problem
# 
# Model Inputs: ...
# Model Outputs: ...

# Models:
    # Model Inputs:
        # input_comp :   Model inputs (not limited to desgin variables 
                        # --> Not all model inputs are design variables)
    # Aerodynamics
        # aero_comp_1 : Equation
        # aero_comp_2 : Equation
        # ...
    # Propulsion 
        # prop_comp_1 : Equation
        # prop_copm_2 : Equation
        # ...
    # Weights and Stability
        # weight_comp_1 : Equation 
        # weight_comp_2 : Equation
        # ...
    # Economics 
        # econ_comp_1 : Equation
        # econ_comp_2 : Equation
        # ...
    # Performance 
        # perf_comp_1 : Equation
        # perf_comp_2 : Equation 
    # Model Outpu:
        # output_comp : Model Outputs = Profit



from openmdao.api import Problem, Group, IndepVarComp, ExecComp
import numpy as np
=======
# OBJECTIVE FUNCTION: MINIMIZE (negative) Profit

# DESIGN VARIABLES (w.r.t) :
#       wing_alpha - WING AOA
#       wing_ar - WING ASPECT RATIO
#       wing_s - WING SURFACE AREA
#       tail_alpha - TAIL AOA
#       tail_ar - TAIL ASPECT RATIO
#       tail_span - TAIL SURFACE AREA
#       h - ALTITUDE
#       v_inf - SPEED
#       cp - POWER COEFFICIENT
#       j - ADVANCE RATIO
#       r - ROTOR RADIUS
#       rpm - ROTATIONAL SPEED
#       mb - BATTERY MASS
#       numflts - NUMBER OF FLIGHTS

# CONSTRAINTS (subj. to):
#       L - W = 0 -- LEVEL FLIGHT CONDITION (VERTICAL)
#       T - D = 0 -- LEVEL FLIGHT CONDITION (HORIZONTAL)
#       R >= 100e3 m -- MINIMUM RANGE
#       Cm = 0 -- LEVEL FLIGHT CONDITION (MOMENT)
#       SM: [0.06, 0.20] -- STATIC MARGIN

# MODEL INPUTS: wing_alpha, wing_ar, wing_span, tail_alpha, tail_ar, tail_span,
#               h, v_inf, cp, j, r, rpm, mb, numflts
# MODEL OUTPUTS: L, W, T, D, R, M, SM

import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, ExecComp, ScipyOptimizeDriver
>>>>>>> e6008428a13a8e1745b2ec8847787c280f01a7b8
from UAM_team_optimization.components.cl_wing_comp import CLWingComp
from UAM_team_optimization.components.cl_tail_comp import CLTailComp
from UAM_team_optimization.components.cdi_wing_comp import CDiWingComp
from UAM_team_optimization.components.cdi_tail_comp import CDiTailComp
from UAM_team_optimization.components.geometry_comp import GeometryComp
from UAM_team_optimization.components.propulsion_comp import wing_outer_prop_thrust_coeff, wing_inner_prop_thrust_coeff,tail_prop_thrust_coeff
from UAM_team_optimization.components.axial_int_comp import AxialIntComp
from UAM_team_optimization.components.percent_blown_comp import PercentBlownComp
<<<<<<< HEAD
=======
from UAM_team_optimization.components.geometry_comp import GeometryComp
from UAM_team_optimization.components.grossweight_comp import GrossWeightComp
from UAM_team_optimization.components.xcg_comp import XCGComp
from UAM_team_optimization.components.xnp_comp import XNPComp
>>>>>>> e6008428a13a8e1745b2ec8847787c280f01a7b8

prob = Problem()
model = Group()

comp = IndepVarComp()

#Adding Input variables which are the outputs of input_comp
# Wing 
comp.add_output('wing_alpha', val = 0.1)
comp.add_output('wing_CLa', val = 2*np.pi)
comp.add_output('wing_CL0', val = 0.2)
comp.add_output('wing_CD0', val = 0.015)
comp.add_output('wing_e', val = 0.85)
comp.add_output('wing_AR', val = 8 )
comp.add_output('wing_area', val = 25 )
# Tail
comp.add_output('tail_alpha', val = 0)
comp.add_output('tail_CLa', val = 2*np.pi)
comp.add_output('tail_CL0', val = 0.2)
comp.add_output('tail_CD0', val = 0.015)
comp.add_output('tail_e', val = 0.85)
comp.add_output('tail_AR', val = 8 )
comp.add_output('tail_area', val = 4 )
# Propeller 
comp.add_output('wing_prop_inner_rad',val = 0.8)
comp.add_output('wing_prop_outer_rad',val = 0.8)
comp.add_output('tail_prop_rad',val = 0.8)
comp.add_output('wing_inner_thrust_coeff', val = wing_inner_prop_thrust_coeff)
comp.add_output('wing_outer_thrust_coeff', val = wing_outer_prop_thrust_coeff)
comp.add_output('tail_thrust_coeff', val = tail_prop_thrust_coeff)

<<<<<<< HEAD
model.add_subsystem('inputs_comp', comp, promotes = ['*'])


comp = GeometryComp()
model.add_subsystem('geometry_comp', comp, promotes = ['*'])
comp = ExecComp('wing_chord = wing_area / wing_span')
model.add_subsystem('wing_chord_comp', comp, promotes = ['*'])
comp = ExecComp('tail_chord = tail_area / tail_span')
model.add_subsystem('tail_chord_comp', comp, promotes = ['*'])
comp = AxialIntComp()
model.add_subsystem('axial_int_comp', comp, promotes = ['*'])
comp = PercentBlownComp()
model.add_subsystem('percent_blown_comp', comp, promotes = ['*'])
comp = CLWingComp()
model.add_subsystem('cl_wing_comp', comp, promotes = ['*'])
comp = CLTailComp()
model.add_subsystem('cl_tail_comp', comp, promotes = ['*'])
comp = CDiWingComp()
model.add_subsystem('cdi_wing_comp', comp, promotes = ['*'])
comp = CDiTailComp()
model.add_subsystem('cdi_tail_comp', comp, promotes = ['*'])
comp = ExecComp('wing_CD = wing_CD0 + wing_CDi')
model.add_subsystem('wing_CD_comp', comp, promotes = ['*'])
comp = ExecComp('tail_CD = tail_CD0 + tail_CDi')
model.add_subsystem('tail_CD_comp', comp, promotes = ['*'])
comp = ExecComp('wing_LD = wing_CL/wing_CD')
model.add_subsystem('wing_ld_comp', comp, promotes = ['*'])
comp = ExecComp('tail_LD = tail_CL/tail_CD')
model.add_subsystem('tail_ld_comp', comp, promotes = ['*'])





prob.model = model 
prob.setup(check = True)
prob.run_model()
prob.check_partials(compact_print=True)

print('wing_CL',prob['wing_CL'])
print('tail_CL',prob['tail_CL'])
print('wing_span',prob['wing_span'])
print('tail_span',prob['tail_span'])
print('thrust_coeff',prob['thrust_coeff'])
print('axial_int_fac',prob['axial_int_fac'])
print('wing_blown_percent', prob['wing_blown_percent'])

prob.model.list_outputs()
=======
comp.add_output('h', val=0.)
comp.add_output('v_inf', val=58.)
comp.add_output('cp', val=0.)
comp.add_output('j', val=0.)
comp.add_output('r', val=0.)
comp.add_output('rpm', val=1900)
comp.add_output('mb', val=500.)
comp.add_output('nmflts', val=0.)

comp.add_design_var('wing_alpha')
comp.add_design_var('wing_ar')
comp.add_design_var('wing_span')
comp.add_design_var('tail_alpha')
comp.add_design_var('tail_ar')
comp.add_design_var('tail_span')
comp.add_design_var('h')
comp.add_design_var('v_inf')
comp.add_design_var('cp')
comp.add_design_var('j')
comp.add_design_var('r')
comp.add_design_var('rpm')
comp.add_design_var('mb')
comp.add_design_var('nmflts')

model.add_subsystem('inputs_comp', comp, promotes = ['*'])


comp = GeometryComp()
model.add_subsystem('geometry_comp', comp, promotes = ['*'])
comp = ExecComp('wing_chord = wing_area / wing_span')
model.add_subsystem('wing_chord_comp', comp, promotes = ['*'])
comp = ExecComp('tail_chord = tail_area / tail_span')
model.add_subsystem('tail_chord_comp', comp, promotes = ['*'])
comp = AxialIntComp()
model.add_subsystem('axial_int_comp', comp, promotes = ['*'])
comp = PercentBlownComp()
model.add_subsystem('percent_blown_comp', comp, promotes = ['*'])
comp = CLWingComp()
model.add_subsystem('cl_wing_comp', comp, promotes = ['*'])
comp = CLTailComp()
model.add_subsystem('cl_tail_comp', comp, promotes = ['*'])
comp = CDiWingComp()
model.add_subsystem('cdi_wing_comp', comp, promotes = ['*'])
comp = CDiTailComp()
model.add_subsystem('cdi_tail_comp', comp, promotes = ['*'])
comp = ExecComp('wing_CD = wing_CD0 + wing_CDi')
model.add_subsystem('wing_CD_comp', comp, promotes = ['*'])
comp = ExecComp('tail_CD = tail_CD0 + tail_CDi')
model.add_subsystem('tail_CD_comp', comp, promotes = ['*'])
comp = ExecComp('wing_LD = wing_CL/wing_CD')
model.add_subsystem('wing_ld_comp', comp, promotes = ['*'])
comp = ExecComp('tail_LD = tail_CL/tail_CD')
model.add_subsystem('tail_ld_comp', comp, promotes = ['*'])




# WEIGHTS/STABILITY COMPONENTS
comp = GrossWeightComp()
model.add_subsystem('grossweight_comp', comp, promotes=['*'])

comp = XCGComp()
model.add_subsystem('xcg_comp', comp, promotes=['*'])

comp = XNPComp()
model.add_subsystem('xnp_comp', comp, promotes=['*'])

comp = ExecComp('SM = (XNP - XAC) / MAC')
comp.add_constraint('SM', lower=0.06, upper=0.20)
model.add_subsystem('sm_comp', comp, promotes=['*'])

comp = ExecComp('M = (wing_lift * XCG) - tail_lift * (tail_arm - XCG)')
comp.add_constraint('M', equals=0.)
model.add_subsystem('m_comp', comp, promotes=['*'])







prob.model = model
prob.setup()
prob.run_model()
prob.check_partials(compact_print=True)
prob.model.list_outputs()
# prob.driver = ScipyOptimizeDriver()
# prob.driver.options['optimizer'] = 'SLSQP'
# prob.driver.options['tol'] = 1e-15
# prob.driver.options['disp'] = True


# prob.run_driver()

>>>>>>> e6008428a13a8e1745b2ec8847787c280f01a7b8
