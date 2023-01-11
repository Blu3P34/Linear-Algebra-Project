from sympy import *
import numpy as np
GroupID = 12

def diagonizability(M):
    #List of eigenvalues
    arr = np.linalg.eigvals(M)
    n = len(arr)

    #--Check for real eigenvalues--
    eig_real = True
    for ele in arr:
        if np.iscomplex(ele) == True:
            eig_real = False
            break

    #--Check for distinction--
    distinct_eig = True
    new_arr = sorted(arr)
    for ele in range(1,len(arr)):
        if new_arr[ele] == new_arr[ele - 1]:
            distinct_eig = False
            break
    
    #--Check for diagonizability
    if distinct_eig == True and len(arr) == M.shape[0] and eig_real == True:
        return true
    else :
        return false

def question1(a):
    print("Question 1")

    M = Matrix([[1,1,0],[0,1,1],[1,0,-a]])
    print("The dimension of Im(f) is",M.shape[0])
    print("The bases are")
    for ele in range(3):
        print(np.array(M.col(ele)))

def question2(a):
    print("Question 2")

    M = Matrix([1, 2, a])
    E = Matrix([[1,1,1],[1,0,1],[1,1,0]])
    F = Matrix([[1,1],[2,1]])
    A_EF = Matrix([[2,1,-3],[0,3,4]])
    f = F*A_EF*(E**-1)*M
    print("F(1,2,a) is\n",np.array(f))

def question3(a):
    print("Question 3")

def question4(a):
    print("Question 4")

def question5(a):
    print("Question 5")
    Diagonizable_M = False 
    while Diagonizable_M == False :
        M = np.random.randint(-10,10,(4,4))
        if diagonizability(M) == True :
            Diagonizable_M = True
    print("Random 4x4 diagonalizable matrix M\n", M)
    print("M^100\n", M**100)

question1(GroupID)
question2(GroupID)
question3(GroupID)
question4(GroupID)
question5(GroupID)