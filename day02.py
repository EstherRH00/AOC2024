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
        n1 = int(a[i])
        n2 = int(a[i + 1])
        if parella_invalida(n1, n2, incr):
            if (err_ignore == 0):
                if (i != 0 and not parella_invalida(int(a[i - 1]), n2, incr)) or i == 0:
                    err_ignore += 1
                elif (i != (len(a) - 1) and not parella_invalida(n1, int(a[i + 1]), incr)) or i == (len(a) - 1):
                    err_ignore += 1
                    i += 1  # ignorem el segon
                else:
                    t = True
            else:
                t = True
        i += 1
    return t

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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1()
    part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
