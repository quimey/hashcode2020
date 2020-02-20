from main import read_data, score

bs, libraries, D = read_data()

def maximizar_librerias_registradas(b,l,d):
	solution = []
	l = [list(l[i]) + [i] for i in range(len(l))]
	sorted_libs = sorted(l, key= lambda x: x[1])
	for lib in sorted_libs:
		sorted_books = sorted([i for i in lib[2]], key=lambda x: b[x])
		solution.append((lib[-1], sorted_books))
	return solution
