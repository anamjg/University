import numpy as np 
import matplotlib.pyplot as plt 
def creator(rows: int, columns: int, values: list):
        matrix = np.array(values).reshape(rows, columns)
        d = []
        r = []
        for j in range(rows):
            d.append(matrix[j][j])
            s = 0
            for k in range(columns):
                if k != j:
                    s += abs(matrix[j][k])
            r.append(s)
        return matrix, d, r
    
def sirkel(x,y,r):
    t = np.linspace(0,2*np.pi,100)
    plt.plot(x+r*np.cos(t),y+r*np.sin(t),linewidth=2)
    
def circles(r_d):
    for i in range(len(r_d[1])):
        x = r_d[1][i]
        r = r_d[2][i]
        sirkel(x, 0, r)
     
# Exercise 3a: 
values_A = [-2, 0, 1/2, 1, -1/4, 1, 1/4, 0, 0, 0, 3, -1, 1/8, 1/8, 1/4, 2]
A = creator(4,4, values_A)
circles(A)
u,v = np.linalg.eig(A[0])
plt.plot(u.real, u.imag,'.',markersize=30)
plt.axis('equal')
plt.show()
#'''   
# Exercise 3b: 
values_B = [5, -1, 1, 1, 2, 1, 1, -1, -1]
B = creator(3, 3, values_B)
circles(B)
u,v = np.linalg.eig(B[0])
plt.plot(u.real, u.imag,'.',markersize=30)
plt.axis('equal')
plt.show()

# Exercise 3c: 
values_C = [-2, 0, 1/2, 1, -1/4, 1, 1/4, 0, 0, 0, 3, -1, 1/8, 1/8, 1/4, 2, 5, -1, 1, 1, 2, 1, 1, -1, -1]
C = creator(5, 5, values_C)
circles(C)
u,v = np.linalg.eig(C[0])
plt.plot(u.real, u.imag,'.',markersize=30)
plt.axis('equal')
plt.show()

# Exercise 3d:   !!! Mangler forklaring 
values_D = [1, 1.5, 1.5, 1.5, 0, 2, 2.5, 2.5, 0, 0, 3, 3.5, 0, 0, 0, 4]
D = creator(4,4, values_D)
circles(D)
u,v = np.linalg.eig(D[0])
plt.plot(u.real, u.imag,'.',markersize=30)
plt.axis('equal')
plt.show()
'''
Forklar hva som skjer med egensirkelene. Hvor ligger egenverdiene?
'''

# Exercise 4
'''
(a) Gi en formodning om hvor egenverdiene til en nxn matrise befinner seg i forhold til egensirklene, basert på observasjonene fra Oppgave 3.
(b) Bevis formodningen fra Oppgave 4 (a).
'''

# Exercise 5
'''
For a diagonal matrix D = diag(d1, d2, d3, ..., dn), if all di ≠ 0, then
diag(d1, d2, d3, ..., dn) diag(1/d1, 1/d2, 1/d3, ..., 1/dn) = diag(1, 1, 1, ..., 1) = I 
and diag(1/d1, 1/d2, 1/d3, ..., 1/dn) diag(d1, d2, d3, ..., dn) = diag(1, 1, 1, ..., 1) = I
'''

# Exercise 6
'''
En 2x2 matrise som er invertibel, men som ikke er diagonaldominant:

[-3     1
  5     0]

([-3     1 ^(-1)      [0     1/5         
  5     0])        =   1     3/5]
  
Denne matrisen er invertibel, men den er ikke diagonaldominant siden
|-3| > 1
|0| > 5
'''