from gurobipy import *

n = 6
c = [2,5,6,8,4,3]
M = 100

m = Model('0-1 Logical')

x = m.addVars(n, vtype= GRB.BINARY, name= 'x')
y = m.addVar(vtype = GRB.BINARY, name= 'y')

m.setObjective(quicksum(x[i]*c[i] for i in range(n)), GRB.MAXIMIZE)

m.addConstr(x.sum() >= 2)
m.addConstr(x.sum() <= 4)
m.addConstr(x[2] + x[4] <= 1)
m.addConstr(x[2] + x[4] <= 1)
m.addConstr(x[3] <= x[0])
m.addConstr(x[0]+x[1] <=1 + M*y)
m.addConstr(x[4]+x[5] >= 1 - M*(1-y))

m.write('0-1.lp')

m.optimize()

if m.SolCount > 0:
    m.printAttr('x')
