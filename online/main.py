import random
import sys
from maximizar_librerias_registradas import maximizar_librerias_registradas
from cabeza import solve_cabeza
from matching import matching


class Invalid(Exception):
    pass


def print_data(solution):
    # solution tiene que ser una lista de pares, cada elemento es un par con
    # el id de la library y una lista de libros a ser escaneados
    print(len(solution))
    for idx, books in solution:
        print(idx, len(books))
        print(' '.join(map(str, books)))


def filter(D, bs, libraries, solution):
    result = []
    signup = 0
    scanned = set()
    for idx, books in solution:
        current = []
        t, m, _= libraries[idx]
        # it takes t days to signup
        signup += t
        cnt = 0
        # process non scanned books in order
        for book in books:
            if cnt == m * max(0, D - signup):
                break
            if book not in scanned:
                scanned.add(book)
                current.append(book)
                cnt += 1
        if current:
            result.append((idx, current))
    return result


def score(D, bs, libraries, solution):
    result = 0
    signup = 0
    scanned = set()
    for idx, books in solution:
        t, m, have = libraries[idx]
        # it takes t days to signup
        signup += t
        cnt = 0
        # process non scanned books in order
        for book in books:
            if book not in have:
                raise Invalid
            if cnt == m * max(0, D - signup):
                break
            if book not in scanned:
                scanned.add(book)
                result += bs[book]
                cnt += 1
    return result


def dummy_solve(bs, libraries, d):
    solution = []
    for i, lib in enumerate(libraries):
        solution.append((i, lib[2]))
    return solution


solve = maximizar_librerias_registradas


def local_search(bs, libraries, d, solution):
    ITERATIONS = 50000
    ms = score(d, bs, libraries, solution)
    n = len(solution)
    for it in range(ITERATIONS):
        i = random.randrange(n)
        j = random.randrange(n)
        solution[i], solution[j] = solution[j], solution[i]
        s = score(d, bs, libraries, solution)
        if s > ms:
            ms = s
            print('Local search:', ms, it, file=sys.stderr)
        else:
            solution[i], solution[j] = solution[j], solution[i]


def read_data():
    # devuelve una tupla con scores de los libros, descripcion de las libraries
    # y el limite de dias
    # cada library es una terna con dias para signup, scans por dia y lista de
    # libros
    B, L, D = map(int, input().split())
    bs = list(map(int, input().split()))
    libraries = []
    for _ in range(L):
        N, T, M = map(int, input().split())
        ids = set(map(int, input().split()))
        libraries.append((T, M, ids))
    return bs, libraries, D


if __name__ == '__main__':
    bs, libraries, d = read_data()
    solution = solve(bs, libraries, d)
    local_search(bs, libraries, d, solution)
    s = score(d, bs, libraries, solution)
    print(s, file=sys.stderr)
    with open('scores.txt', 'a') as f:
        f.write(str(s) + '\n')
    # solution = matching(d, bs, libraries, solution)
    solution = filter(d, bs, libraries, solution)
    s = score(d, bs, libraries, solution)
    print(s, file=sys.stderr)
    print_data(solution)
