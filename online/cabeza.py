

class CabezaSolver():
    
    def __init__(self, bs, libraries, d):
        self.bs =bs
        self.sorted_bs = sorted(enumerate(bs), key=lambda item:item[1])
        self.libs = libraries
        self.d = d
    
    def _lib_score(self, lib_description, books_sent, days_left):
        assert isinstance(books_sent, set)
        signup_days, scans_per_day, book_ids = lib_description
        days_left -= signup_days
        if days_left <= 0:
            return 0, []
        
        book_ids = set(book_ids) - books_sent
        book_pairs = [bp for bp in self.sorted_bs if bp[0] in book_ids]
        
        book_pairs_per_day = [book_pairs[i:i + scans_per_day] for i in range(0, len(book_pairs), scans_per_day)
                              ][0:days_left]
        
        score = 0
        books_to_scan = []
        for bppday in book_pairs_per_day:
            for bp in bppday:
                score += bp[1]
                books_to_scan += [bp[0]]
        
        return score, books_to_scan
    
    def solve(self):
        ret = []
        pending_lib_ids = set(range(len(self.libs)))
        books_sent = set()
        days_left = self.d
        
        while pending_lib_ids and days_left:
            max_score = 0
            best_lib_id = None
            best_books_to_scan = None
            
            for lib_id in pending_lib_ids:
                lib = self.libs[lib_id]
                score, books_to_scan = self._lib_score(lib, books_sent, days_left)
                if score > max_score:
                    max_score = score
                    best_lib_id = lib_id
                    best_books_to_scan = books_to_scan
            
            if best_lib_id is None: # max_score == 0
                break
            
#             print(days_left)
            
            ret += [(best_lib_id, best_books_to_scan)]
            pending_lib_ids.remove(best_lib_id)
            books_sent -= set(best_books_to_scan)
            days_left -= self.libs[best_lib_id][0]
        
        return ret


solve_cabeza = lambda bs, libraries, d : CabezaSolver(bs, libraries, d).solve()
