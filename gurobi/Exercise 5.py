from gurobipy import *

m = Model('RAP')

R = ['Carlos', 'Joe', 'Monika']
J = ['Tester', 'JavaDeveloper', 'Architect']

combinations, ms=multidict({
    ('Carlos','Tester'):53,
    ('Carlos','JavaDeveloper'):27,
    ('Carlos','Architect'):13,
    ('Joe','Tester'):80,
    ('Joe','JavaDeveloper'):47,
    ('Joe', 'Architect'): 67,
    ('Monika', 'Tester'): 53,
    ('Monika', 'JavaDeveloper'): 73,
    ('Monika', 'Architect'): 47,
})

x = m.addVars(combinations, vtype= GRB.BINARY, name ="assign")
jobs = m.addConstrs((x.sum('*',j) == 1 for j in J), 'job')
resources = m.addConstrs((x.sum(r, '*') <=1 for r in R), 'resource')

m.setObjective(x.prod(ms), GRB.MAXIMIZE)

m.write('RAP.lp')
m.optimize()

if m.solcount >0:
    m.printAttr('x')

print('total matching scores', m.objval)
