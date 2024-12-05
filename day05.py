# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1():
    ordre = dict()
    resultat = 0


    with open("input") as f:
        for line in f.readlines():
            line = line[:len(line)-1]
            if('|' in line):
                n1, n2 = line.split('|')
                if (n1 in ordre.keys()):
                    ordre[n1].append(n2)
                else:
                    ordre[n1] = [n2]
            elif ',' in line:

                print(ordre)
                llista = line.split(",")
                i = 0
                trobat = False
                while i < len(llista) and not trobat:
                    j = i+1
                    while j < len(llista) and not trobat:
                        if llista[j] in ordre.keys() and llista[i] in ordre[llista[j]]:
                            trobat = True
                        j += 1
                    i += 1
                if not trobat:
                    resultat += int(llista[len(llista)//2])
    print(resultat)

def troba_ordre(llista, ordre):
    i = 0
    while i < len(llista):
        j = i + 1
        canvi = False
        while j < len(llista) and not canvi:
            if llista[j] in ordre.keys() and llista[i] in ordre[llista[j]]:
                aux = llista[j]
                del llista[j]
                llista.insert(i, aux)
                canvi = True
                break
            j += 1
        if not canvi:
            i += 1
    return int(llista[len(llista)//2])

def part2():
    ordre = dict()
    resultat = 0

    with open("input05") as f:
        for line in f.readlines():
            line = line[:len(line) - 1]
            if ('|' in line):
                n1, n2 = line.split('|')
                if (n1 in ordre.keys()):
                    ordre[n1].append(n2)
                else:
                    ordre[n1] = [n2]
            elif ',' in line:
                llista = line.split(",")
                for i in range(len(llista)):
                    for j in range(i+1, len(llista)):
                        if llista[j] in ordre.keys() and llista[i] in ordre[llista[j]]:
                            resultat += troba_ordre(llista, ordre)

    print(resultat)


if __name__ == '__main__':
    part2()

