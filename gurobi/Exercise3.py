from gurobipy import *
m= gurobipy.read("C:\gurobi911\win64\examples\data\Seongwon_VS_Dad.lp")
m.optimize()
m.printAttr("x")
print(m.objVal)
