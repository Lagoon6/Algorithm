from gurobipy import *

SOURCE = 'A'
TERMINAL = 'F'
nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
arcs, cost = multidict({
    ('A','B'):2,
    ('A','C'):4,
    ('B','C'):1,
    ('B','D'):4,
    ('B','E'):2,
    ('C','E'):3,
    ('D','F'):2,
    ('E','D'):3,
    ('E','F'):2,
})
m = Model('sp')

x = m.addVars(nodes, nodes, vtype= GRB.CONTINUOUS, name= 'x')

m.setObjective(quicksum(cost[(i,j)]* x[i,j] for i in nodes for j in nodes if (i,j) in arcs), GRB.MINIMIZE)

for i in nodes:
    if i == SOURCE:
        m.addConstr(quicksum(x[i,j] for j in nodes if (i,j) in arcs) - quicksum(x[j,i] for j in nodes if (j,i) in arcs) ==1)
    elif i == TERMINAL:
        m.addConstr(quicksum(x[i, j] for j in nodes if (i, j) in arcs) - quicksum(x[j, i] for j in nodes if (j, i) in arcs) == -1)
    else:
        m.addConstr(quicksum(x[i, j] for j in nodes if (i, j) in arcs) - quicksum(x[j, i] for j in nodes if (j, i) in arcs) == 0)

m.write('sp.lp')
m.optimize()
print(m.objVal)

if m.SolCount > 0:
    m.printAttr('x')
