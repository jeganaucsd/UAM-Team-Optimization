import numpy as np 
from openmdao.api import Problem, Group, IndepVarComp, ExecComp, ScipyOptimizeDriver
from econ_optimization.components.enghr_comp import EngHrComp
from econ_optimization.components.mfghr_comp import MfgHrComp
from econ_optimization.components.toolhr_comp import ToolHrComp
from econ_optimization.components.qchr_comp import QcHrComp
from econ_optimization.components.laborcost_comp import LaborCostComp
from econ_optimization.components.develcost_comp import DevelCostComp
from econ_optimization.components.fltcost_comp import FltCostComp
from econ_optimization.components.mfgcost_comp import MfgCostComp
from econ_optimization.components.batterycost_comp import BatteryCostComp
from econ_optimization.components.motorcost_comp import MotorCostComp
from econ_optimization.components.avionicscost_comp import AvionicsCostComp
from econ_optimization.components.structcost_comp import StructCostComp
from econ_optimization.components.ac_comp import AcComp

prob = Problem()

model = Group()

comp = IndepVarComp()
comp.add_output('EmptyWeight', val=6000)
comp.add_output('v_inf' , val= 240)
comp.add_output('q' , val= 250)
comp.add_output('EngRt' , val= 40)
comp.add_output('MfgRt' , val= 30)
comp.add_output('ToolRt' , val= 21)
comp.add_output('QcRt' , val= 37)
comp.add_output('kwh' , val= 133)
comp.add_output('kwhcost' , val= 137)
comp.add_output('num_motor' , val= 12)
model.add_subsystem('inputs_comp', comp, promotes=['*'])

comp=EngHrComp()
model.add_subsystem('enghr_comp', comp, promotes=['*'])

comp=MfgHrComp()
model.add_subsystem('mfghr_comp', comp, promotes=['*'])

comp=ToolHrComp()
model.add_subsystem('toolhr_comp', comp, promotes=['*'])

comp=QcHrComp()
model.add_subsystem('qchr_comp', comp, promotes=['*'])

comp=LaborCostComp()
model.add_subsystem('laborcost_comp', comp, promotes=['*'])

comp=DevelCostComp()
model.add_subsystem('develcost_comp', comp, promotes=['*'])

comp=FltCostComp(fta=6)
model.add_subsystem('fltcost_comp', comp, promotes=['*'])

comp=MfgCostComp()
model.add_subsystem('mfgcost_comp', comp, promotes=['*'])

comp=BatteryCostComp()
model.add_subsystem('batterycost_comp', comp, promotes=['*'])

comp=MotorCostComp()
model.add_subsystem('motorcost_comp', comp, promotes=['*'])

comp=AvionicsCostComp()
model.add_subsystem('avionicscost_comp', comp, promotes=['*'])

comp=StructCostComp()
model.add_subsystem('structcost_comp', comp, promotes=['*'])

comp=AcComp()
model.add_subsystem('ac_comp', comp, promotes=['*'])

prob.model = model
prob.setup()
prob.run_model()

prob.check_partials(compact_print=True)

print('EngHr', prob['EngHr'])
print('MfgHr', prob['MfgHr'])
print('ToolHr', prob['ToolHr'])
print('QcHr', prob['QcHr'])
print('LaborCost', prob['LaborCost'])
print('DevelCost', prob['DevelCost'])
print('FltCost', prob['FltCost'])
print('MfgCost', prob['MfgCost'])
print('BatteryCost', prob['BatteryCost'])
print('MotorCost', prob['MotorCost'])
print('AvionicsCost', prob['AvionicsCost'])
print('StructCost', prob['StructCost'])
print('Ac', prob['Ac'])