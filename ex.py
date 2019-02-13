from numpy import matrix

rows = 4
cols = 3
m = []
for c in range( cols ):
    m.append( [] )
    for r in range( rows ):
        if (c == 1):
            m[c].append( 1 )
        else:
            m[c].append( 0 )


print(m[2])
