import re
from fractions import Fraction


def add(coefmatx, row, rowthatwillbeadded, const, const2):
    for p, elem in enumerate(coefmatx[row]):
        coefmatx[row][p] = coefmatx[row][p] * const
        coefmatx[row][p] = coefmatx[row][p] + (coefmatx[rowthatwillbeadded][p])*const2


def uniquesoln(coefmatx, rows, columns):
    soln = []
    ans = 0
    for i in range(rows - 1, -1, -1):
        if (i == rows - 1):
            soln.append(coefmatx[i][-1])
        else:
            ans = coefmatx[i][-1]
            for k in range(i+1, columns):
                ans = ans - coefmatx[i][k]*soln[k - i - 1]
            soln.insert(0, ans)
    return soln


def checkzeros(l1, length):
    for i in range(length):
        if l1[i] == 0:
            continue
        else:
            return False
    return True


def printmatx(coeff_matx):
    for elem in coeff_matx:
        for pelem in elem:
            print(pelem, end='\t')
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

          ->  3x + 0y + -6z + 1w = 9  <-
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
    if (t != 0) and (t != 1):
        for p in range(columns+1):
            if coeff_matx[o][p] % t == 0:
                coeff_matx[o][p] = int(coeff_matx[o][p] / t)
            else:
                coeff_matx[o][p] = Fraction(coeff_matx[o][p], t)

print("The Row Echelon form of the augmented matrix of the system of linear equations is: ")
printmatx(coeff_matx)
print("************************************************")

for elem in coeff_matx:
    if checkzeros(elem, columns):
        rank_a -= 1
    if checkzeros(elem, columns + 1):
        rank_c -= 1

print(f"The rank of the coefficient matrix is: {rank_a}")
print(f"The rank of the augmented matrix is: {rank_c}")

if (rank_c == rank_a) and (rank_c == var_count):
    print("We will have a Unique Solution.")
    solution = uniquesoln(coeff_matx, rows, columns)
    count_soln = len(solution) - 1
    print("The solutions is: ")
    for index, element in enumerate(solution):
        print(variables[index], " = ", element)
elif(rank_c == rank_a) and (rank_c < var_count):
    print(f"We will have infinite solutions, as rank of augmented matrix, {rank_c} < number of variables, {var_count}")
elif rank_c != rank_a:
    print("Inconsistent set of linear equations.")
else:
    print("Invalid")
print("************************************************")
print(f"The total number of addition and multiplication operations that were done to reach the Row Echelon form is = {count_echelon}")
print(f"The total number of addition and multiplication operations that were done to obtain the solution from Row Echelon form is = {count_soln}")
print(f"The total number of addition and multiplication operations that were done = {count_soln + count_echelon}")
print("************************************************")


