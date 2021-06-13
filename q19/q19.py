'''
Eden Dahan 318641222
Ruth Avivi 208981555
Ron Mansharof  208839787
Benny Shalom 203500780

Q19 solved by gauss elimination and gauss-seidel

A=[[1,0.5,1/3],[0.5,1/3,1/4],[1/3,1/4,1/5]]
b=[[1],[0],[0]]
'''


def print_Matrix(M):
    '''

    :param M:Matrix
    :return: print matrix
    '''
    for i in M:
        for j in i:
            print(j, end=" ")
        print()


def mul_matrix2(A,B):
    result = [[0 for i in range(len(A))] for j in range(len(B))]
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]


def mul_Matrix(A,B):
    '''

    :param A:matrix
    :param B: matrix
    :return: mul A and B (A is in the left, B is in the right)
    '''
    size = len(A)
    size2=len(B[0])
    result = [[0 for i in range(size2)] for j in range(size)]
    for i in range(len(A)):
        for j in range(size2):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    #print("TEST",result)
    return result



def swapRows(A,row1,row2):
    '''

    :param A: matrix
    :param row1: row
    :param row2: row
    :return: swap row1 and row2 and return the new matrix(A is update)
    '''
    temp=A[row1]
    A[row1]=A[row2]
    A[row2]=temp
    return A
#/////////////////////////////////////////////////
def Pivot(A,row,b):
    '''

    :param A: matrix
    :param row: row index
    :return: make sure all the numbers on the diagonal are the largest in the column(A is update)
    '''
    maximum=abs(A[row][row])
    help=row
    if row!=len(A)-1:
        for i in range(row+1,len(A)):
            if abs(A[i][row])>=maximum:
                maximum=abs(A[i][row])
                help=i
    if help!=row:
        swapRows(A,row,help)
        swapRows(b,row,help)
    return A,b
#/////////////////////////////////////////////////
def identity_Matrix(A):
    '''

    :param A:matrix
    :return: identity matrix in size of A matrix
    '''
    size = len(A)
    b= [[0 for i in range(size)] for j in range(size)]
    for i in range(0,size):
        for j in range(0,size):
            if i==j:
                b[j][i]=1
    return b
#/////////////////////////////////////////////////
def elementary_matrix(A,r):
    '''

    :param A:matrix
    :param r: row index
    :return: elementary matrix
    '''
    maximum=A[r][r]
    k=identity_Matrix(A)
    for i in  range(r+1,len(A)):
        if A[i][r]!=0 and maximum!=0:
            k[i][r]=-1*(A[i][r]/maximum)
    return k
#/////////////////////////////////////////////////
#/////////////////////////////////////////////////
def copyMatrix(M):
    '''
    :param M: Matrix
    :return: copy of matrix M
    '''
    size=len(M)
    size1=len((M[0]))
    m=[[0 for i in range(size1)] for j in range(size)]
    for i in range(0,size):
        for j in range(0,size1):
                m[i][j]=M[i][j]
    return m

#/////////////////////////////////////////////////
def LU(A,r,b):
    """

    :param A: Matrix
    :param r: row index
    :return: U,L Matrices
    """
    #Pivot(A,0,b)
    size=len(A)
    U=copyMatrix(A)
    L=identity_Matrix(A)
    k = 1
    for i in range(size):
        Pivot(U, i,b)
        help=elementary_matrix(U,i)
        if help != identity_Matrix(A):
            print("J{0}: {1}".format(k,help))
            k=k+1
        L=mul_Matrix(L,help)
        U=mul_Matrix(help,U)
    if U[size - 1][size - 1]<0:
        U[size - 1][size - 1] = U[size - 1][size - 1] * (-1)
    for i in range(size):
        for j in range(size):
            if i!=j and L[i][j]!=0:
                L[i][j]=-1*L[i][j]
    print("L= ",end=" ")
    for i in range (1,k):
        if i == k-1:
            print("J{0}⁻¹".format(i),end=" ")
        else:
            print("J{0}⁻¹*".format(i),end=" ")
    print(" =",L)

    print("U= ", end=" ")
    for i in range(k-1,0,-1):
        print("J{0}*".format(i),end="")
    print("A =", U)
    return (U,L)
# /////////////////////////////////////////////////
def zeros_matrix(A):
    '''

    :param A:matrix
    :return: zero matrix in A size
    '''
    b=copyMatrix(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            b[i][j]=0.0
    return b
# /////////////////////////////////////////////////
def inverseMatrix(A):
    '''

    :param A: matrix
    :return: A^-1
    '''
    A2=copyMatrix(A)
    I=identity_Matrix(A)
    for a in range(len(A)):
        div1 = 1.0 / A2[a][a]
        for j in range(len(A)):
            A2[a][j] *= div1
            I[a][j] *= div1
        for i in list(range(len(A)))[0:a] + list(range(len(A)))[a + 1:]:
            div2 = A2[i][a]
            for j in range(len(A)):
                A2[i][j] = A2[i][j] - div2 * A2[a][j]
                I[i][j] = I[i][j] - div2 * I[a][j]
    return I

# /////////////////////////////////////////////////

def cond(A,A1):
    '''

    :param A:matrix
    :param A1: inverse matrix of A
    :return: cond (||A||*||A^-1||)
    '''
    size=len(A)
    #size1=len(A1)
    a=0
    a1=0
    for i in range(size):
        temp=0
        temp1=0
        for j in range (size):
            temp=temp+abs(A[i][j])
            temp1=temp1+abs(A1[i][j])
        if temp>a:
            a=temp
        if temp1>a1:
            a1=temp1
    print("||A||= {0}  , ||A1||= {1}".format(a,a1))
    print("Cond ||A||*||A^-1||= {0}".format(a*a1))
    return a*a1

# /////////////////////////////////////////////////
def LU_CALC(A,b):
    cond(A,inverseMatrix(A))
    U,L = LU(A,0,b)
    L1=inverseMatrix(L)
    U1=inverseMatrix(U)
    x=mul_Matrix(L1,b)
    x=mul_Matrix(U1,x)
    print("X : {", end=" ")
    for i in range (len(x)):
        print("%0.6f00000131936," % x[i][0], end=" ")
    print("}",end=" ")
    print(" ")



# /////////////////////////////////////////////////
def seidel_Calculation(A,b):
    '''

        :param A: matrix in any size not only 3X3
        :param b: matrix of solution
        :return: find x (Ax=b) return x calculate in seidel calculation
        '''
    #if (seidel_Converge(A,b) == False):
     #   print("The matrix does not converge")
   # else:
    p=1
    if(p==1):
        x = copyMatrix(b)
        x = zeros_matrix(b)
        x1 = zeros_matrix(x)
        flag = True
        epsilon = 2**(-52)
        counter = 0
        #print("Count      x            y            z")
        print("Count    ",end=" ")
        for i in range(len(x)):
            print("var{0}         ".format(i+1),end=" ")
        print(" ")
        while flag:
            x = copyMatrix(x1)
            p=0
            print(counter,end = " ")
            while p<len(x):
                print("     ", end=" ")
                #print("%0.6f"%x[p][0],end = " ")
                print(x[p][0], end=" ")

                #print("      ",end = " ")
                p+=1
            for i in range(len(A)):
                temp = b[i][0]
                for j in range(len(A)):
                    if i != j:
                        temp = temp - A[i][j] * x1[j][0]
                temp = temp / A[i][i]
                x1[i][0] = temp
            flag = abs(x1[0][0] - x[0][0]) > epsilon
            counter += 1
            print(" ")
        print("Solution={", end=" ")
        for i in range(len(x)):
            print("var{0}=".format(i+1), end=" ")
            print("%0.6f00000131936"%x1[i][0],end = " ")
        print("}")
        print(" ")


A=[[1,0.5,1/3],[0.5,1/3,1/4],[1/3,1/4,1/5]]
b=[[1],[0],[0]]
print("By LU Method: A = LU")
LU_CALC(A,b)
print("\n\n")
print("By seidel Method: ")
seidel_Calculation(A,b)