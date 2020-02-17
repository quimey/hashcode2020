#include<iostream>
#include<vector>

using namespace std;

int main() {
    int n, m;
    cin >> m >> n;
    vector<int> s(n);
    vector<char> t(m + 1, 0);
    //vector<int> inv(m + 1, -1);
    vector<pair<int, int>> r;
    int best = 0;
    r.push_back(make_pair(0, -1));
    for (int i = 0; i < n; i ++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i ++) {
        cerr << i << " ";
        int l = r.size();
        for(int j = 0; j < l; j ++) {
            int next = r[j].first + s[i];
            if (next <= m && t[next] == 0) {
                t[next] = 1;
                //inv[next] = r.size();
                r.push_back(make_pair(next, i));
                best = max(best, next);
            }
        }
    }
    cerr << "done " << best << endl;
    vector<int> res;
    /*while (best) {
        int idx = inv[best];
        res.push_back(r[idx].second);
        best -= s[r[idx].second];
    }*/
    cout << res.size() << endl << res[0];
    for (int i = 1; i < res.size(); i ++) {
        cout << " " << res[i];
    }
    cout << endl;
    return 0;
}

