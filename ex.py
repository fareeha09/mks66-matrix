from numpy import matrix

rows = 4
cols = 4
m = []
for c in range( cols ):
    m.append( [] )
    for r in range( rows ):
        if (c == 1):
            if (r==1):
                m[c].append( 1 )
            else:
                m[c].append( 2 )
        else:
            m[c].append( 0 )

def print_matrix( matrix ):
    numrows= len(matrix[0])
    numcols= len(matrix)
    matrixx=""
    i = 0
    while (i < numrows):
        for j in range(numcols):
            matrixx += str(matrix[j][i]) + " "
        matrixx += "\n"
        i+=1
    print(matrixx)

print_matrix(m)

def ident( matrix ):
    numrows= len(matrix[0])
    numcols= len(matrix)
    #i = 0
    #while (i < numrows):
    #    for j in range(numcols):
    for i in range(numrows):
        for j in range(numrows):
            if (i==j):
                matrix[i][j]=1
            else:
                matrix[i][j]=0

ident(m)
print_matrix(m)
