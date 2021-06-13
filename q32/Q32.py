#Git link:
'''
Eden Dahan 318641222
Ruth Avivi 208981555
Ron Mansharof  208839787
Benny Shalom 203500780

Question num 32 : solved by lagrange interpolation , linear interpolation.
'''
import datetime


def lagrangeInterpolation(table,point):
    sol=0
    l=1
    counter=0
    p="P{0}({1})".format(len(table)-1,point)

    for i in range(len(table)):
        print("l{0}({1})=".format(i,point),end=" ")
        for j in range(len(table)):
            if i != j :
                if (i==len(table)-1) and j == (len(table) - 2):
                    print("(({0}-{1})/({2}-{3}))=".format(point, table[j][0], table[counter][0], table[j][0]), end=" ")
                elif j != len(table)-1:
                    print("(({0}-{1})/({2}-{3}))*".format(point,table[j][0],table[counter][0],table[j][0]),end=" ")
                else:
                    print("(({0}-{1})/({2}-{3}))=".format(point, table[j][0], table[counter][0], table[j][0]), end=" ")
                l*=(point-table[j][0])/(table[counter][0]-table[j][0])
        print(l,end=" ")
        print(" ")
        l*=table[counter][1]
        counter+=1
        sol+=l
        l=1
    print("P{0}({1}) = ".format(len(table)-1,point),end=" ")
    for i in range (len(table)):
        if i == len(table)-1:
            print("l{0}({1})*y{2}  ".format(i,point,i),end=" ")
        else:
            print("l{0}({1})*y{2} + ".format(i,point,i),end=" ")
    print(" ")
    return (sol)

#////////////////////////////////////////////////////////////////////////////////
def linearInterpolation(table,point):
    for i in range (0,len(table)):
        if point<table[i+1][0] and point > table[i][0]:
            print("f(x)=((y₁-y₂)/(x₁-x₂))*point + (y₂x₁ - y₁x₂)/(x₁-x₂)")
            y1=table[i][1]
            y2=table[i+1][1]
            x1=table[i][0]
            x2=table[i+1][0]
            sol=((y1-y2)/(x1-x2))*point+(y2*x1-y1*x2)/(x1-x2)
            print("f(x)=(({0}-{1})/({2}-{3}))*{10} + ({4} * {5} - {6} * {7})/({8}-{9}) ".format(y1,y2,x1,x2,y2,x1,y1,x2,x1,x2,point))
            print("f({0}) = {1}".format(point,sol))
            return sol
    return "Not sol for this table "
#////////////////////////////////////////////////////////////////////////////////



k=[[0.2, 13.7241], [0.35, 13.9776], [0.45, 14.0625], [0.6, 13.9776], [0.75,13.7241], [0.85, 13.3056], [0.9, 12.7281]]
sol_lagrange=lagrangeInterpolation(k, 0.65)
time = datetime.datetime.now()
print("lagrange formula - sigma(from i=1 to n)*Li(x)*Yi")
print("lagrange sol = ",sol_lagrange,end = "")
print("00000",end = "")
print(time.day,end = "")
print(time.hour,end = "")
print(time.minute,end = "")
print("")
print("\n")
sol_linear=linearInterpolation(k, 0.65)
print("linear sol = ",sol_linear,end = "")
print("00000",end = "")
print(time.day,end = "")
print(time.hour,end = "")
print(time.minute,end = "")