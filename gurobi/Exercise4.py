from gurobipy import *

n = 7
p = [6, 5, 8, 9, 6, 7, 3]
w = [2, 3, 6, 7, 5, 9, 4]
c = 9

m = Model()

x = m.addVars(n, vtype=GRB.BINARY, name='x')

m.setObjective(quicksum(x[i]*p[i] for i in range(n)), GRB.MAXIMIZE)
m.addConstr(quicksum(x[i]*w[i] for i in range(n))<=c, name='knapsack')
m.optimize()

if m.SolCount > 0:
    m.printAttr('x')

m.write('knapsack.lp')