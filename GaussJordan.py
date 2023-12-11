import re
from fractions import Fraction

def add(coefmatx, row, rowthatwillbeadded, const, const2):
    for p, elem in enumerate(coefmatx[row]):
        coefmatx[row][p] = coefmatx[row][p] * const
        coefmatx[row][p] = coefmatx[row][p] + (coefmatx[rowthatwillbeadded][p])*const2


def uniquesoln(coefmatx, rows, columns):
    soln = []
    for i in range(rows):
        soln.append(coefmatx[i][-1])
    return soln


def checkzeros(l1, length):
    for i in range(length):
        if l1[i] == 0:
            continue
        else:
            return False
    return True


def get1ind(coeffmatx, row_number):
    for i, elem in enumerate(coeffmatx[row_number]):
        if (elem == 1):
            return i
        else:
            continue


def printmatx(coefmatx):
    for elem in coeff_matx:
        for pelem in elem:
            print(pelem, end = '\t')
        print('\n')


coeff_matx = []
solution = []
variables = []
solution_element = 0
count_echelon = 0
count_soln = 0
rows = int(input("Enter the number of equations: "))
columns = int(input("Enter the number of variables: "))
var_count = columns
eq_count = rows
rank_c = rows
rank_a = rows
print('''Please enter the following equations in the format:

          ->  3x + 0y + -6z + 1w= 9  <-
''')

for i in range(rows):
    str = input(f"Enter equation {i+1}: ")
    p = re.findall('-?\d+', str)
    for i, elem in enumerate(p):
        p[i] = int(elem)
    coeff_matx.append(p)
    p = []
    variables = re.findall('[a-z]', str)
print("************************************************")

for m in range(columns):
    for n in range(m+1, rows, 1):
        add(coeff_matx, n, m, coeff_matx[m][m], ((coeff_matx[n][m])*(-1)))
        count_echelon += 1

for o, elem in enumerate(coeff_matx):
    t = elem[o]
    if ((t != 0) and (t != 1)):
        for p in range(columns+1):
            if (coeff_matx[o][p] % t == 0):
                coeff_matx[o][p] = int(coeff_matx[o][p] / t)
            else:
                coeff_matx[o][p] = Fraction(coeff_matx[o][p], t)

for z in range(rows - 1, -1, -1):
    if (checkzeros(coeff_matx[z], columns)):
        continue
    else:
        for p in range(z-1, -1, -1):
            a = get1ind(coeff_matx, z)
            add(coeff_matx, p, z, 1, (-1 * coeff_matx[p][a]))
            count_echelon += 1
print("The Reduced Row Echelon form of the augmented matrix of the system of linear equations is: ")
printmatx(coeff_matx)
print("************************************************")

for elem in coeff_matx:
    if checkzeros(elem, columns):
        rank_a -= 1
    if checkzeros(elem, columns + 1):
        rank_c -= 1

print(f"The rank of the coefficient matrix is: {rank_a}")
print(f"The rank of the augmented matrix is: {rank_c}")

if ((rank_c == rank_a) and (rank_c == var_count)):
    print("We will have a Unique Solution.")
    solution = uniquesoln(coeff_matx, rows, columns)
    print("The solutions is: ")
    for index, element in enumerate(solution):
        print(variables[index], " = ", element)
elif((rank_c == rank_a) and (rank_c < var_count)):
    print(f"We will have infinite solutions, as rank of augmented matrix, {rank_c} < number of variablems, {var_count}")
elif(rank_c != rank_a):
    print("Inconsistent set of linear equations.")
else:
    print("Invalid")
print("************************************************")
print(f"The total number of addition and multiplication operations that were done to reach the Reduced Row Echelon form is = {count_echelon}")
print(f"The total number of addition and multiplication operations that were done = {count_soln + count_echelon}")
