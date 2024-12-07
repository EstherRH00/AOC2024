def es_posible(resultat, nombres, i, tmp):
    n = len(nombres) - 1
    if nombres[i] > resultat:
        return False
    if i == n:
    
        return resultat == tmp

    suma = tmp + nombres[i+1]
    prod = tmp * nombres[i+1]
    return es_posible(resultat, nombres, i+1, suma) or es_posible(resultat, nombres, i+1, prod)

def es_posible_concat(resultat, nombres, i, tmp):
    n = len(nombres) - 1
    if nombres[i] > resultat:
        return False
    if i == n:
        return resultat == tmp

    suma = tmp + nombres[i+1]
    prod = tmp * nombres[i+1]
    concat = int(str(tmp) + str(nombres[i+1]))
    return es_posible_concat(resultat, nombres, i+1, suma) or es_posible_concat(resultat, nombres, i+1, prod) or es_posible_concat(resultat, nombres, i+1, concat) 


def part1():
    resultat = 0
    with open("input07") as f:
        for fila in f.readlines():
            r, ops = fila.split(':')
            ops = ops.split()
            for i, op in enumerate(ops):
                ops[i] = int(op)
            if (es_posible(int(r), ops, 0, ops[0])):
                resultat += int(r)
    print(resultat)


def part2():
    resultat = 0
    with open("input07") as f:
        for fila in f.readlines():
            r, ops = fila.split(':')
            ops = ops.split()
            for i, op in enumerate(ops):
                ops[i] = int(op)
            if (es_posible_concat(int(r), ops, 0, ops[0])):
                resultat += int(r)
    print(resultat)

part1()
part2()