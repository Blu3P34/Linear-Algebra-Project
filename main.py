import numpy as np
groupID = 12

def question1(a) :
    f = np.array([[1,1,0],[0,1,1],[1,0,-a]])
    print("The transformation matrix f is")
    print(f)
    print("The dimension of Im(f) is ",f.shape[0])

    basis = np.zeros((3,1), dtype = int)
    for i in range(3) :
        for j in range(3) :
            basis[j][0] = f[j][i]
        print("Basis",i + 1,"is")
        print(basis)

def question2(a) :
    E = np.array([[1,1,1],[1,0,1],[1,1,0]])
    F = np.array([[1,2],[1,1]])
    AEF = [[2,1,-3],[0,3,4]]
    x = np.array([[1],[2],[a]])
    f = np.matmul(np.linalg.inv(F), np.matmul(
        AEF, np.matmul(
            E,x)))
    f = f.astype(int)
    print(f)
question2(groupID)