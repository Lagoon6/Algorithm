from gurobipy import *

#파라미터
mine = 4

year = 5

max_mine =3

royalty = [500,400,400,500]

MaxOutput = [200,250,130,300]

quality = [1, 0.7, 1.5, 0,5]

demand_quality =[0.9, 0.8, 1.2, 0.8, 1.0]

price_year = [10, 9, 8.1, 7.29, 6.561]

sale_rate = 0.1

m = Model('project mine')

#결정변수
x = m.addVars(year,mine, vtype = GRB.BINARY,name = "open")
y = m.addVars(year,mine, vtype = GRB.BINARY, name = "mining")
z = m.addVars(year,mine, name = "output")
w = m.addVars(year, name = "year_output")



#제약조건
c1 = m.addConstrs(x.sum(i,'*') <= max_mine for i in range(year))
c2 = m.addConstrs(y.sum(i,'*') <= max_mine for i in range(year))
c3 = m.addConstrs(z.sum(i,'*') == w[i] for i in range(year))

for i in range(year):
    for j in range(mine):
        c4 = m.addConstr(z[i,j] <= MaxOutput[j]*y[i,j])


c5 = m.addConstrs(quicksum(quality[j]*z[i,j]for j in range(mine)) == demand_quality[i]*w[i] for i in range(year))

for i in range(year):
    for j in range(mine):
        c6 = m.addConstr(x[i,j] >= y[i,j])

for i in range(year-1):
    for j in range(mine):
        c7 = m.addConstr(x[i+1,j] >= x[i,j])


#목적함수
#for i in range(year):
    #for j in range(mine):
        #result = (quicksum(price_year[i]*w[i]) - quicksum(royalty[j]*x[i,j]))

#result = quicksum(price_year[i]*w[i] for i in range(year)) - quicksum(royalty[j]*x[i,j] for i, j in range(mine)) - quciksum(royalty[j]*x[4,j] for i, j in range(mine))


m.setObjective( quicksum(price_year[i]*w[i] for i in range(year))-quicksum(royalty[j]*x[i,j] for i,j in x) , GRB.MAXIMIZE)

m.write('Mine optimize.lp')
m.optimize()
if m.SolCOunt > 0:
    m.printAttr('x')
print('max mine profit:',m.objVal)
