"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
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

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    numrows= len(matrix[0])
    numcols= len(matrix)
    for i in range(numrows):
        for j in range(numrows):
            if (i==j):
                matrix[i][j]=1
            else:
                matrix[i][j]=0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	print_matrix(m1)
	print_matrix(m2)
	numrows_m1= len(m1[0]) #4
	numcols_m1= len(m1) #4
	numrows_m2= len(m2[0]) #4
	numcols_m2= len(m2) #N
	
	if ((numcols_m1) != (numrows_m2)):
		print("Undefined")
		return 
		
	temp = m2[:]
	num = 0 
	while (num< numrows_m1):
		for i in range(numcols_m2): #N
			ans = 0
			for n in range(numcols_m1): #4
				ans += temp[i][n] * m1[n][num]
			m2[i][num] = ans
		num = num+ 1
	print_matrix(m2)


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
matrix_mult(A,B)
print_matrix(A)
print_matrix(B)
matrix_mult(B,A)  
print_matrix(A)
print_matrix(B)
ident(B)
matrix_mult(B,A)
print_matrix(A)

