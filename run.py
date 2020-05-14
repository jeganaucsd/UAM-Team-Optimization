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



from openmdao.api import Problem, Group, IndepVarComp
import numpy as np

prob = Problem()

model = Group()

comp = IndepVarComp()
#Adding Input variables which are the outputs of input_comp
comp.add_output('wing_alpha', val = 0)
comp.add_output('tail_alpha', val = 0)
model.add_subsystem('inputs_comp', comp, promotes = ['*'])
#...etc...

prob.model = model 
prob.setup()
prob.run_model()