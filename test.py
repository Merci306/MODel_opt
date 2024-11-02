import gurobipy as gp
from gurobipy import *
m = gp.Model("MIP")
x1 = m.addVar(lb=0,ub=40,vtype=GRB.CONTINUOUS,name='x1')
x2 = m.addVar(vtype=GRB.CONTINUOUS,name= 'x2')
x3 = m.addVar(vtype=GRB.CONTINUOUS,name='x3')
x4 = m.addVar(lb=2,ub=3,vtype=GRB.INTEGER,name='x4')
m.setObjective(x1 + 2*x2 + 3*x3 + x4,GRB.MAXIMIZE)
m.addConstr(-x1+x2+x3+10*x4 <= 20,name='c1')
m.addConstr(x1-3*x2+x3 <= 30,name='c2')
m.addConstr(x2-3.5*x4 == 0,name='c3')
m.setParam('outPutFlag',0)
m.optimize()
if m. status==GRB.Status .OPTIMAL:
    print('obj=' ,m.objVal)
    for v in m.getVars():
        print(v.varName, ':',v.x)