import random
import sys


class Invalid(Exception):
    pass


def print_data(solution):
    # solution tiene que ser una lista de pares, cada elemento es un par con
    # el id de la library y una lista de libros a ser escaneados
    print(len(solution))
    for idx, books in solution:
        print(idx, len(books))
        print(' '.join(map(str, books)))


def score(D, bs, libraries, solution):
    result = 0
    signup = 0
    scanned = set()
    for idx, books in solution:
        t, m, have = libraries[idx]
        # it takes t days to signup
        signup += t
        total = max(0, D - signup)
        cnt = 0
        # process non scanned books in order
        for book in books:
            if book not in have:
                raise Invalid
            if cnt == m * total:
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


solve = dummy_solve


def local_search(bs, libraries, d, solution):
    ITERATIONS = 1000
    ms = score(d, bs, libraries, solution)
    n = len(solution)
    for _ in range(ITERATIONS):
        i = random.randrange(n)
        j = random.randrange(n)
        solution[i], solution[j] = solution[j], solution[i]
        s = score(d, bs, libraries, solution)
        if s > ms:
            ms = s
            print('Local search:', ms, file=sys.stderr)
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
    print(score(d, bs, libraries, solution), file=sys.stderr)
    print_data(solution)
