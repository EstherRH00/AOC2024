import numpy as np
def part1():
    mat = list()
    resultat = 0
    inicial = ['^',0,0]
    with open("input06") as f:
        for i, line in enumerate(f.readlines()):
            l = line[:len(line)-1]
            llista = list()
            for j, elem in enumerate(l):
                if elem != '#' and elem != '.':
                    inicial = [elem, i, j]
                    llista.append('.')
                else:
                    llista.append(elem)
            mat.append(llista)

    n_files = len(mat)
    n_cols = len(mat[0])

    fi = False
    while not fi:

        i = inicial[1]
        j = inicial[2]

        if mat[i][j] != 'X':
            mat[i][j] = 'X'
            resultat += 1

        if inicial[0] == '^':
            if i-1 < 0: fi = True
            elif mat[i-1][j] != '#':
                inicial = ['^',i-1,j]
            else:
                inicial = ['>',i,j]
        elif inicial[0] == '>':
            if j+1 >= n_cols: fi = True
            elif mat[i][j+1] != '#':
                inicial = ['>',i,j+1]
            else:
                inicial = ['v',i,j]
        elif inicial[0] == 'v':
            if i+1 >= n_files: fi = True
            elif mat[i+1][j] != '#':
                inicial = ['v',i+1,j]
            else:
                inicial = ['<',i,j]
        elif inicial[0] == '<':
            if j-1 < 0: fi = True
            elif mat[i][j-1] != '#':
                inicial = ['<',i,j-1]
            else:
                inicial = ['^',i,j]
        else:
            print("ERROR FATAL OMAIGOT")

    print(resultat)

def forca_bruta(mat, inicial):

    n_files = len(mat)
    n_cols = len(mat[0])
    aux = dict()
    fi = False
    while not fi:

        i = inicial[1]
        j = inicial[2]

        if (i,j) in aux.keys() and inicial[0] in aux[(i,j)]:
            return True

        if (i,j) in aux.keys():
            aux[(i,j)].append(inicial[0])
        else:
            aux[(i,j)] = [inicial[0]]

        if inicial[0] == '^':
            if i - 1 < 0:
                fi = True
            elif mat[i - 1][j] != '#':
                inicial = ['^', i - 1, j]
            else:
                inicial = ['>', i, j]
        elif inicial[0] == '>':
            if j + 1 >= n_cols:
                fi = True
            elif mat[i][j + 1] != '#':
                inicial = ['>', i, j + 1]
            else:
                inicial = ['v', i, j]
        elif inicial[0] == 'v':
            if i + 1 >= n_files:
                fi = True
            elif mat[i + 1][j] != '#':
                inicial = ['v', i + 1, j]
            else:
                inicial = ['<', i, j]
        elif inicial[0] == '<':
            if j - 1 < 0:
                fi = True
            elif mat[i][j - 1] != '#':
                inicial = ['<', i, j - 1]
            else:
                inicial = ['^', i, j]
        else:
            print("ERROR FATAL OMAIGOT")

    return False
def part2():
    mat = list()
    resultat = 0
    inicial = ['^', 0, 0]
    n = 0
    with open("input06") as f:
        for i, line in enumerate(f.readlines()):
            l = line[:len(line) - 1]
            llista = list()
            for j, elem in enumerate(l):
                if elem != '#' and elem != '.':
                    inicial = [elem, i, j]
                    llista.append('.')
                else:
                    llista.append(elem)
            mat.append(llista)

    mat = np.asarray(mat)

    n_files = len(mat)
    n_cols = len(mat[0])

    for i in range(n_files):
        print("comencant fila: ", i)
        for j in range(n_cols):
            if not (i == inicial[1] and j == inicial[2]) and mat[i][j] != '#':
                aux = mat.copy()
                aux[i][j] = '#'
                if forca_bruta(aux, inicial.copy()):
                    resultat += 1
    print(resultat)

if __name__ == '__main__':
    part1()
    part2()

