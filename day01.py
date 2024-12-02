# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1():
    l1 = list()
    l2 = list()
    with open("input01") as f:
        for line in f.readlines():
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))
    l1.sort()
    l2.sort()

    resultat = 0

    for n1, n2 in zip(l1, l2):
        resultat += abs(n1 - n2)

    print(resultat)

def part2():
    l1 = list()
    l2 = list()
    with open("input01") as f:
        for line in f.readlines():
            a, b = line.split()
            l1.append(int(a))
            l2.append(int(b))

    resultat = 0

    for n1 in l1:
        resultat += n1 * l2.count(n1)

    print(resultat)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1()
    part2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
