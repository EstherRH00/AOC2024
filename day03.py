# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def part1():
    resultat = 0
    with open("input03") as f:
        for line in f.readlines():
            separat = line.split("mul(")

            # perque sigui valid a continuacio hi ha d'haver %d{1-3},%d{1-3})
            for s in separat:
                parts = s.split(",")
                if(len(parts) >= 2):
                    n1 = parts[0]
                    parts2 = parts[1].split(")")
                    if(parts2[0] != parts[1]):
                        n2 = parts2[0]
                        if n1.isnumeric() and len(n1) <= 3 and n2.isnumeric() and len(n2) <= 3 :
                            resultat += (int(n1) * int(n2))
    print(resultat)


def part2():
    resultat = 0
    enabled = True
    with open("input03") as f:
        for line in f.readlines():
            l = line
            if(not enabled):
                l = "don't()" + l
            toDo = l.split("do()")
            for do in toDo:
                reallyDo = do.split("don't()")
                separat = reallyDo[0].split("mul(")

                # perque sigui valid a continuacio hi ha d'haver %d{1-3},%d{1-3})
                for s in separat:
                    parts = s.split(",")
                    if (len(parts) >= 2):
                        n1 = parts[0]
                        parts2 = parts[1].split(")")
                        if (parts2[0] != parts[1]):
                            n2 = parts2[0]
                            if n1.isnumeric() and len(n1) <= 3 and n2.isnumeric() and len(n2) <= 3:
                                resultat += (int(n1) * int(n2))
            lastDo = line.rfind("do()")
            lastDont = line.rfind("don't()")

            if lastDo < lastDont:
                enabled = False
            else:
                enabled = True

    print(resultat)

if __name__ == '__main__':
    part1()
    part2()

