import sys
import networkx as nx


def count(d, bs, libraries, solution):
    result = []
    signup = 0
    scanned = set()
    for idx, books in solution:
        current = []
        t, m, _= libraries[idx]
        # it takes t days to signup
        signup += t
        result.append((idx, m * max(0, d - signup)))
    return result


def matching(d, bs, libraries, solution):
    G = nx.DiGraph()
    counts = count(d, bs, libraries, solution)
    for idx, cnt in counts:
        G.add_edge('source', 'lib_' + str(idx), capacity=cnt, weight=0)
    for idx, books in solution:
        for book in books:
            G.add_edge(
                'lib_' + str(idx), 'book_' + str(book), capacity=1, weight=0
            )
    for idx, score in enumerate(bs):
        G.add_edge('book_' + str(idx), 'target', capacity=1, weight=-score)
    flow_dict = nx.maximum_flow(G, 'source', 'target')
    result = []
    for idx, books in solution:
        current = []
        for book in books:
            if flow_dict[1]['lib_' + str(idx)]['book_' + str(book)]:
                current.append(book)
        result.append((idx, current))
    return result
