from dataclasses import dataclass

def print_data(libraries):
    # libraries tiene que ser una lista de pares, cada elemento es un par con
    # el id de la library y una lista de libros a ser escaneados
    for idx, books in libraries:
        print(idx, len(books))
        print(' '.join(books))

def read_data():
    # devuelve una tupla con scores de los libros, descripcion de las libraries
    # cada library es una terna con dias para signup, scans por dia y lista de
    # libros
    B, L, D = map(int, input().split())
    bs = list(map(int, input().split()))
    libraries = []
    for _ in range(L):
        N, T, M = map(int, input().split())
        ids = list(map(int, input().split()))
        libraries.append((T, M, ids))
    return bs, libraries
