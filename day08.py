import numpy as np

def part1():
    resultat = 0
    taulell = []
    posicions = dict()
    
    with open("input08") as f:
        # taulell = np.asarray([[lletra for lletra in fila if lletra !=  '\n'] for fila in f.readlines()])
        for i, fila in enumerate(f.readlines()):
            l = []
            for j, lletra in enumerate(fila):
                if lletra != '\n': 
                    l.append(lletra)
                    if lletra != '.':
                        if lletra in posicions.keys():
                            posicions[lletra].append((i,j))
                        else:
                            posicions[lletra] = [(i,j)]
            taulell.append(l)   
    
    # print(taulell)
    # print(posicions)

    n_files = len(taulell)
    n_cols = len(taulell[0])

    for clau in posicions.keys():
        # estan ordenats per com els he llegit
        valors = posicions[clau]
        for i in range(len(valors)):
            for j in range(i+1, len(valors)):
                antinodes = [(valors[i][0] - (valors[j][0] - valors[i][0]), valors[i][1] - (valors[j][1] - valors[i][1])), 
                             (valors[j][0] + (valors[j][0] - valors[i][0]), valors[j][1] + (valors[j][1] - valors[i][1]))]
                for antinode in antinodes:
                    if isinstance(antinode[0], int) and isinstance(antinode[1], int) and antinode[0] >= 0 and antinode[0] < n_files and antinode[1] >= 0 and antinode[1] < n_cols:
                        if (taulell[antinode[0]][antinode[1]] != '#'):
                            resultat += 1
                            taulell[antinode[0]][antinode[1]] = '#'

    # print(np.asarray(taulell))
    print(resultat)


def part2():
    resultat = 0
    taulell = []
    posicions = dict()
    
    with open("input08") as f:
        # taulell = np.asarray([[lletra for lletra in fila if lletra !=  '\n'] for fila in f.readlines()])
        for i, fila in enumerate(f.readlines()):
            l = []
            for j, lletra in enumerate(fila):
                if lletra != '\n': 
                    l.append(lletra)
                    if lletra != '.':
                        if lletra in posicions.keys():
                            posicions[lletra].append((i,j))
                        else:
                            posicions[lletra] = [(i,j)]
            taulell.append(l)   
    
    # print(taulell)
    # print(posicions)

    n_files = len(taulell)
    n_cols = len(taulell[0])

    for clau in posicions.keys():
        # estan ordenats per com els he llegit
        valors = posicions[clau]
        for i in range(len(valors)):
            for j in range(i+1, len(valors)):
                k = 0
                dins = [True, True]
                while(dins[0] or dins[1]):
                    antinodes = [(valors[i][0] - k * (valors[j][0] - valors[i][0]), valors[i][1] - k * (valors[j][1] - valors[i][1])), 
                                (valors[j][0] + k * (valors[j][0] - valors[i][0]), valors[j][1] + k * (valors[j][1] - valors[i][1]))]
                    for iter, antinode in enumerate(antinodes):
                        dins[iter] = antinode[0] >= 0 and antinode[0] < n_files and antinode[1] >= 0 and antinode[1] < n_cols
                        if isinstance(antinode[0], int) and isinstance(antinode[1], int) and dins[iter]:
                            if (taulell[antinode[0]][antinode[1]] != '#'):
                                resultat += 1
                                taulell[antinode[0]][antinode[1]] = '#'
                                # print("antinode!", antinode, resultat)
                    k += 1

    # print(np.asarray(taulell))
    print(resultat)

part1()
part2()