#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cmath>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)

using namespace std;

char scanned[100100];

int score(
        int d, vector<int> &bs, vector<int> &ts, vector<int> &ms,
        vector<vector<int>> &bss, vector<pair<int, vector<int>>> &solution
) {
    int result = 0, signup = 0;
    memset(scanned, 0, 100100 * sizeof(char));
    forn(i, solution.size()) {
        int idx = solution[i].first;
        vector<int> &books = solution[i].second;
        signup += ts[idx];
        if (signup >= d) break;
        int cnt = 0;
        const int lim = ms[idx] * max(0, d - signup);
        forn(j, books.size()) {
            if (cnt == lim) break;
            if (scanned[books[j]] == 0) {
                scanned[books[j]] = 1;
                result += bs[books[j]];
                cnt ++;
            }
        }
    }
    return result;
}

vector<pair<int, vector<int>>> dummy_solve(
        int d, vector<int> bs, vector<int> ts, vector<int> ms, vector<vector<int>> bss
) {
    vector<pair<int, vector<int>>> solution;
    forn(i, ts.size()) {
        solution.push_back(make_pair(i, bss[i]));
    }
    return solution;
}

double rdouble() {
    return 1.0 * rand() / RAND_MAX;
}

vector<pair<int, vector<int>>> simann(
        int d, vector<int> &bs, vector<int> &ts, vector<int> &ms,
        vector<vector<int>> &bss, vector<pair<int, vector<int>>> &solution
) {
    int mejs = score(d, bs, ts, ms, bss, solution);
    int n = solution.size();
    int mmejs = mejs;
    double temp=1e6, alpha=.99;
    int step = 1000;
    vector<pair<int, vector<int>>> res;
    forn(q, 1500) {
        forn(t, step) {
            int i = rand() % n;
            int j = rand() % n;
            swap(solution[i], solution[j]);
            int s = score(d, bs, ts, ms, bss, solution);
            if (s > mmejs) {
                mmejs = s;
                cerr << s << " " << temp << endl;
                res = solution;
            }
            if(rdouble() < exp(-max(-s + mejs, 0) / temp)) {
                mejs = s;
            } else {
                swap(solution[i], solution[j]);
            }
        }
        temp *= alpha;
    }
    return res;
}

vector<pair<int, vector<int>>> filter(
        int d, vector<int> &bs, vector<int> &ts, vector<int> &ms,
        vector<vector<int>> &bss, vector<pair<int, vector<int>>> &solution
) {
    vector<pair<int, vector<int>>> result;
    int signup = 0;
    memset(scanned, 0, 100100 * sizeof(char));
    forn(i, solution.size()) {
        vector<int> current;
        int idx = solution[i].first;
        vector<int> &books = solution[i].second;
        signup += ts[idx];
        int cnt = 0;
        const int lim = ms[idx] * max(0, d - signup);
        forn(j, books.size()) {
            if (cnt == lim) break;
            if (scanned[books[j]] == 0) {
                scanned[books[j]] = 1;
                current.push_back(books[j]);
                cnt ++;
            }
        }
        if (current.size()) result.push_back(make_pair(idx, current));
    }
    return result;

}

void local_search(
        int d, vector<int> &bs, vector<int> &ts, vector<int> &ms,
        vector<vector<int>> &bss, vector<pair<int, vector<int>>> &solution
) {
    int iterations = 400000;
    int mejs = score(d, bs, ts, ms, bss, solution);
    int n = solution.size();
    forn(it, iterations) {
        int i = rand() % n;
        int j = rand() % n;
        swap(solution[i], solution[j]);
        int s = score(d, bs, ts, ms, bss, solution);
        if (mejs < s) {
            mejs = s;
            if (it % 10 == 0) cerr << mejs << " " << it << endl;
        } else {
            swap(solution[i], solution[j]);
        }
    }
}


vector<int> sort_books(vector<int> &bs, vector<int> &cb, vector<int> &books) {
    vector<pair<int, int>> aux;
    forn(i, books.size()) {
        aux.push_back(make_pair(bs[books[i]] +  0  * cb[books[i]], books[i]));
    }
    sort(aux.begin(), aux.end());
    reverse(aux.begin(), aux.end());
    vector<int> result;
    forn(i, aux.size()) result.push_back(aux[i].second);
    return result;
}


int main() {
    int b, l, d;
    cin >> b >> l >> d;
    vector<int> bs(b), ts(l), ms(l), cb(b);
    vector<vector<int>> bss(l);
    forn(i, b) cin >> bs[i];
    forn(i, l) {
        int n;
        cin >> n >> ts[i] >> ms[i];
        bss[i].resize(n);
        forn(j, n) {
            cin >> bss[i][j];
            cb[bss[i][j]] ++;
        }
        bss[i] = sort_books(bs, cb, bss[i]);
    }
    vector<pair<int, vector<int>>> solution = dummy_solve(d, bs, ts, ms, bss);
    solution = simann(d, bs, ts, ms, bss, solution);
    solution = filter(d, bs, ts, ms, bss, solution);
    cerr << score(d, bs, ts, ms, bss, solution) << endl;
    cout << solution.size() << endl;
    forn(i, solution.size()) {
        cout << solution[i].first << " " << solution[i].second.size() << endl;
        forn(j, solution[i].second.size()) {
            cout << (j? " ": "") << solution[i].second[j];
        }
        cout << endl;
    }
}
