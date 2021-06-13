

import datetime
from math import *


def simpson_Method(func, a, b, epsilon):
    print("Simpson method is going by the formula - (h/3)*(f(a)+2*sigma(from j=1 to last even)*f(X2j)+4*sigma(from j=1 to last odd)*f(X2j-1)+f(b))")
    sol1 = 2 * epsilon
    sol = 0

    def run(func, a, b, slices):
        slices += slices
        h = (b - a) / slices
        print("h = ", h)
        print("a, b = {}, {}".format(a, b))
        arr = []
        for i in range(1, slices):
            arr.append(a + (((b - a) * i) / slices))
        arr.insert(0, a)
        arr.append(b)
        sol = func(a) + func(b)
        print(f'Adding f(start) + f(end): {func(a)} + {func(b)}')
        for i in range(1, len(arr) - 1):
            if i % 2 != 0:
                print(f'Iteration {i}, Last sum += 4 * (odd index value):\n{sol} += {4 * func(arr[i])}')
                sol += 4 * func(arr[i])
            else:
                print(f'Iteration {i}, Last sum += 2 * (even index value):\n{sol} += {2 * func(arr[i])}')
                sol += 2 * func(arr[i])
            print()
        print(f'Result = h/3 * {sol} = {sol * (h / 3)}')
        sol = sol * (h / 3)
        return sol

    slices = 5
    while abs(sol1 - sol) > epsilon:
        sol = run(func, a, b, slices)
        slices *= 2
        sol1 = run(func, a, b, slices)
    return sol1


def find_intervals(a, b, N):
    jump = (b - a)/N
    intervals = []
    j = a
    for i in range(N + 1):
        intervals.append(j)
        j = j + jump
    return intervals


# trapezoidal rule
def trapezoid(f,a,b,N):
    yi=[]
    h = (b-a)/N
    xi = find_intervals(a,b,N)
    for i in xi:
        yi.append(f(i))
    s = 0.0
    for i in range(1,N):
        if yi[i] != inf and yi[i] != -inf:
            s = s + yi[i]
            print("number iteration of trapezoid method:",i)
            print("Approximation:",s)
        else:
            print("The Approximation of the number iteration",i,"of trapezoid method is -inf or inf")
    s = (h/2)*(yi[0] + yi[N]) + h*s
    return s


def romberg(f,a,b,eps,nmax):
# f     ... function to be integrated
# [a,b] ... integration interval
# eps   ... desired accuracy
# nmax  ... maximal order of Romberg method
    Q = [[0 for _ in range(nmax)] for __ in range(nmax)]
    converged = 0
    k=0
    count=1
    print("Romberg method is using trapezoid method -  ")
    print("The formula of Trapezoidal is - sigma(from i=1 to N)*(h/2)*(f(Xi-h)+f(Xi))")
    print("The formula of Romberg Method is - R(n,m)=1/(4^m-1)*(4^m*R(n,m-1)-R*(n-1,m-1))")
    for i in range(0,nmax):
        N = 2**i
        Q[i][0] = trapezoid(f,a,b,N)
        for k in range(0,i):
            n = k + 2
            Q[i][k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i][k] - Q[i-1][k])
            print("number iteration of romberg method:",count)
            print("Approximation:",Q[i][k])
            count+=1
        if (i > 0):
            if (abs(Q[i][k+1] - Q[i][k]) < eps):
               converged = 1
               break
    if nmax == 1:
        return Q[i][k]
    print("The result is -")
    return Q[i][k + 1]


def formated_solution(sol):
    time = datetime.datetime.now()
    return f'{sol}00000{time.day}{time.hour}{time.minute}'




# q16
f = lambda x: ((x**2)*e**((-x**2) - 5*x -3))*(3*x - 5)
# Q8 -0.4, 0.4; Q17 0.5, 1; Q16 0.5, 1
a = 0.5
b = 1
romberg_result = formated_solution(romberg(f, a, b, 0.0001, 10))
print(romberg_result)
symphson_result = formated_solution(simpson_Method(f, a, b, 0.0001))
print(symphson_result)
