from gurobipy import *

effort = [2,3,5]
days = [76,69,54]

total = 3

m = Model('Summer Vacation Planning')

x = m.addVars(total, vtype= GRB.CONTINUOUS, name= 'x')

m.setObjective(quicksum(effort[i]*x[i] for i in range(total)),GRB.MAXIMIZE)

m.addConstr(x[0]+x[1]+x[2] <= days[0] )
m.addConstr(x[0]+x[1] <= days[1] )
m.addConstr(x[0]<= days[2] )
m.addConstr(x[2] >= 30)
m.addConstr(x[1] >= 15)
m.addConstr(x[0] >= 10)

m.write('summer vacation.lp')
m.optimize()

if m.Solcount > 0:
    m.printAttr('x')
