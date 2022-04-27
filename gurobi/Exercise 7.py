from gurobipy import *

ONHAND_INV = 5
FINAL_INV = 5
DEMAND = [10, 15, 30, 35, 25, 10]
PCOST = [1250, 1255, 1270, 1280, 1285, 1295]
ICOST = [60, 60, 60, 60, 60, 60]
PCAPA = [30, 30, 30, 30, 30, 30]
ICAPA = [10, 10, 10, 10, 10, 10]

n_months = 6

m = Model('Production Planning')

x = m.addVars(n_months, vtype= GRB.CONTINUOUS, name='x')
y = m.addVars(n_months, vtype = GRB.CONTINUOUS, name= 'y')

m.setObjective(quicksum(PCOST[i]*x[i]+ ICOST[i]*y[i] for i in range(n_months)),GRB.MINIMIZE)
m.addConstr(ONHAND_INV + x[0] == DEMAND[0] +y[0])
m.addConstrs(y[i-1] + x[i] == DEMAND[i] + y[i] for i in range(1,n_months))
m.addConstrs(x[i] <= PCAPA[i] for i in range(n_months))
m.addConstrs(y[i] <= ICAPA[i] for i in range(n_months))
m.addConstr(y[5] == FINAL_INV)

m.write('production.lp')
m.optimize()
if m.SolCOunt > 0:
    m.printAttr('x')
