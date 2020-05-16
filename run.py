# OBJECTIVE FUNCTION: MINIMIZE (negative) Profit

# DESIGN VARIABLES (w.r.t) :
#       wing_alpha - WING AOA
#       wing_ar - WING ASPECT RATIO
#       wing_s - WING SURFACE AREA
#       tail_alpha - TAIL AOA
#       tail_ar - TAIL ASPECT RATIO
#       tail_s - TAIL SURFACE AREA
#       h - ALTITUDE
#       v_inf - SPEED
#       cp - POWER COEFFICIENT
#       j - ADVANCE RATIO
#       r - ROTOR RADIUS
#       rpm - ROTATIONAL SPEED
#       mb - BATTERY MASS
#       numflts - NUMBER OF FLIGHTS

# CONSTRAINTS (subj. to):
#       L - W = 0 -- LEVEL FLIGHT CONDITION (CRUISE)
#       T - D = 0 -- LEVEL FLIGHT CONDITION (CRUISE)
#       R >= 100e3 m -- MINIMUM RANGE
#       Cm = 0 -- LEVEL FLIGHT CONDITION (CRUISE)
#       SM: [0.06, 0.20] -- STATIC MARGIN

# MODEL INPUTS: wing_alpha, wing_ar, wing_s, tail_alpha, tail_ar, tail_s,
#               h, v_inf, cp, j, r, rpm, mb, numflts
# MODEL OUTPUTS: L, W, T, D, R, Cm, SM

import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, ExecComp, ScipyOptimizeDriver

prob = Problem()
model = Group()

comp = IndepVarComp()

comp.add_output('wing_alpha', val=0.)
comp.add_output('wing_ar', val=3.)
comp.add_output('wing_s', val=15.)
comp.add_output('tail_alpha', val=0.)
comp.add_output('tail_ar', val=3.)
comp.add_output('tail_s', val=2.)
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
comp.add_design_var('wing_s')
comp.add_design_var('tail_alpha')
comp.add_design_var('tail_ar')
comp.add_design_var('tail_s')
comp.add_design_var('h')
comp.add_design_var('v_inf')
comp.add_design_var('cp')
comp.add_design_var('j')
comp.add_design_var('r')
comp.add_design_var('rpm')
comp.add_design_var('mb')
comp.add_design_var('nmflts')

model.add_subsystem('inputs_comp', comp, promotes = ['*'])

prob.model = model
prob.setup()
prob.run_model()
