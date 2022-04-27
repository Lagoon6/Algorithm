from gurobipy import *
model = read("C:\gurobi911\win64\examples\data\coins.lp")

model.optimize()

model.objval
model.printAttr('x')