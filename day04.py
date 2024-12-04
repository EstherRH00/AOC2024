import numpy as np
def part1():
    mat = []
    with open("input04") as f:
        for line in f.readlines():
            l = []
            for char in line:
                if char != '\n':
                    l.append(char)
            mat.append(l)
    n_files = len(mat)
    n_cols = len(mat[0])

    mat = np.asarray(mat)

    total = 0
    for i in range(n_files):
        for j in range(n_cols):
            if mat[i][j] == 'X':
                # horitzontal
                if j+4 <= n_cols and (mat[i, j:j+4] == ['X', 'M', 'A', 'S']).all():
                    total += 1
                if j-3 >= 0 and (mat[i, j-3:j+1] == ['S', 'A', 'M', 'X']).all():
                    total += 1
                # vertical
                if i+4 <= n_files and (mat[i: i+4, j] == ['X', 'M', 'A', 'S']).all():
                    total += 1
                if i-3 >= 0 and (mat[i-3:i+1, j] == ['S', 'A', 'M', 'X']).all():
                    total += 1
                # diagonal
                if j+4 <= n_cols and i+4 <= n_files and mat[i+1,j+1] == 'M' and mat[i+2, j+2] == 'A' and mat[i+3,j+3] == 'S':
                    total += 1
                if j+4 <= n_cols and i-3 >= 0 and mat[i-1,j+1] == 'M' and mat[i-2, j+2] == 'A' and mat[i-3,j+3] == 'S':
                    total += 1
                if j-3 >= 0 and i+4 <= n_files and mat[i+1,j-1] == 'M' and mat[i+2, j-2] == 'A' and mat[i+3,j-3] == 'S':
                    total += 1
                if j-3 >= 0 and i-3 >= 0 and mat[i-1,j-1] == 'M' and mat[i-2, j-2] == 'A' and mat[i-3,j-3] == 'S':
                    total += 1
    print(total)

def part2():
    mat = []
    with open("input04") as f:
        for line in f.readlines():
            l = []
            for char in line:
                if char != '\n':
                    l.append(char)
            mat.append(l)
    n_files = len(mat)
    n_cols = len(mat[0])

    mat = np.asarray(mat)

    total = 0
    for i in range(1, n_files-1):
        for j in range(1, n_cols-1):
            if mat[i][j] == 'A':
                if ((mat[i+1, j+1] == 'S' and mat[i-1, j-1] == 'M') or (mat[i+1, j+1] == 'M' and mat[i-1, j-1] == 'S')) \
                        and ((mat[i+1, j-1] == 'S' and mat[i-1, j+1] == 'M') or (mat[i+1, j-1] == 'M' and mat[i-1, j+1] == 'S')):
                    total += 1
    print(total)

if __name__ == '__main__':
    part1()
    part2()

