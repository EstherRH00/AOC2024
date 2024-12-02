# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1():
    cont = 0
    total = 0
    with open("input02") as f:
        for line in f.readlines():
            total += 1
            a = line.split()
            i = 0
            incr = int(a[0]) < int(a[1])
            t = False
            while i < (len(a) - 1) and not t:
                if ((int(a[i]) < int(a[i+1])) != incr) or (abs(int(a[i]) - int(a[i+1])) > 3) or (int(a[i]) - int(a[i+1]) == 0):
                    t = True
                    cont += 1
                i += 1
    print(total - cont)

def parella_invalida(a, b, incr):
    return ((a < b) != incr) or (abs(a-b) > 3) or (a-b == 0)

def avalua_linia(a, incr):
    i = 0
    t = False
    err_ignore = 0
    while i < (len(a) - 1) and not t:
        # print(a)
        n1 = int(a[i])
        n2 = int(a[i + 1])
        if parella_invalida(n1, n2, incr):
            # print("invalid: ", n1, n2, incr)
            if (err_ignore == 0):
                # Ignorar n1 i mantenir n2
                if ((i != 0 and not parella_invalida(int(a[i - 1]), n2, incr)) and (
                        i != (len(a) - 2) and not parella_invalida(n2, int(a[i+2]), incr))) or (
                            i == 0 and not parella_invalida(n2, int(a[i + 2]), incr)):
                    err_ignore += 1
                    # print("ignorant n1 ", n1, n2, int(a[i+2]))
                # Ignorar n2
                elif (i != (len(a) - 2) and not parella_invalida(n1, int(a[i + 2]), incr)) or (i == len(a) - 2):
                    err_ignore += 1
                    i += 1  # ignorem el segon
                    # print("ignorant n2 ", n2)
                else:
                    # print("no es pot salvar")
                    t = True
            else:
                t = True
        i += 1
    return t

def avalua_linia_brute_force(l):
    for j in range(len(l)):
        a = l.copy()
        a.pop(j)
        incr = int(a[0]) < int(a[1])
        t = False
        i = 0
        while i < (len(a) - 1) and not t:
            if ((int(a[i]) < int(a[i + 1])) != incr) or (abs(int(a[i]) - int(a[i + 1])) > 3) or (
                    int(a[i]) - int(a[i + 1]) == 0):
                t = True
            i += 1
        if(not t):
            return True
    return False

def part2():
    cont = 0
    total = 0
    with open("input02") as f:
        for line in f.readlines():
            total += 1
            a = line.split()
            incr = int(a[0]) < int(a[1])
            if (avalua_linia(a, incr) and avalua_linia(a, not incr)):
                cont += 1
    print(total - cont)

def part2_brute_force():
    cont = 0
    total = 0
    with open("input02") as f:
        for line in f.readlines():
            # print("Avaluant ", line)
            total += 1
            a = line.split()
            if not avalua_linia_brute_force(a):
                cont += 1
    print(total - cont)

def compara():
    with open("input02") as f:
        for line in f.readlines():
            # print("Avaluant ", line)
            a = line.split()

            incr = int(a[0]) < int(a[1])
            force = not avalua_linia_brute_force(a)
            soft = avalua_linia(a, incr) and avalua_linia(a, not incr)

            if(force != soft):
                print(line, force, soft)


if __name__ == '__main__':
    part1()
    part2()
    part2_brute_force()
    compara()

