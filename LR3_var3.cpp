#include <iostream>
#include <string>
#include <vector>
#include <time.h>

using namespace std;


vector<string> all_almost_permut_str(string str) {
    vector<string> result = {};
    for (int i = 0; i < str.length() + 1; i++) {
        for (auto j = str.begin(); j != str.end(); j++) {
            string ob = str.substr(0, i) + *j + str.substr(i);
            if (std::find(result.begin(), result.end(), ob) == result.end()) {
                result.push_back(ob);
            }
        }
    }
    return result;
}

vector<string> sub_sets(string str, int N) {
    vector<string> result = {};
    for (int i = 0; i < str.length() - N + 1; i++) {
        result.push_back(str.substr(i, N + i));
    }
    return result;
}

string main_logic(string str1, string str2, int N) {

    int conunt = 0;

    vector<string> all_possible_hyper_str = {};
    all_possible_hyper_str.push_back(str1 + str2);
    all_possible_hyper_str.push_back(str2 + str1);
    vector<string> al1 = all_almost_permut_str(str1 + str2);
    vector<string> al2 = all_almost_permut_str(str2 + str1);
    std::vector<string> v = {};
    all_possible_hyper_str.insert(all_possible_hyper_str.end(), al1.begin(), al1.end());
    all_possible_hyper_str.insert(all_possible_hyper_str.end(), al2.begin(), al2.end());

    vector<string> all_res = {};

    for (auto i = all_possible_hyper_str.begin(); i != all_possible_hyper_str.end(); i++) {
        vector<string> all_subs_N_1 = sub_sets(*i, N + 1);
        vector<string> aal = all_almost_permut_str(str1);
        vector<string> aal2 = all_almost_permut_str(str2);
        aal.insert(aal.end(), aal2.begin(), aal2.end());
        bool check = false;
        for (auto j = all_subs_N_1.begin(); j != all_subs_N_1.end(); j++) {
            if (std::find(aal.begin(), aal.end(), *j) == aal.end()) {
                break;
            }
            check = true;
        }

        if (check) {
            cout << "check true" << endl;
            all_res.push_back(*i);
        } else {
            cout << "check false" << endl;
        }
        conunt++;
    }
    min_element(all_res.begin(), all_res.end(), [](string a, string b) {
        return a.length() < b.length();
    });
    return *min_element(all_res.begin(), all_res.end(), [](string a, string b) {
        return a.length() < b.length();
    });



}





int main() {
    double start = clock();
    string s1, s2;
    s1 = "ABC";
    s2 = "ACB";
    int N = 3;
    cout << main_logic(s1, s2, N) << endl;
    cout << "time: " << (clock() - start) / CLOCKS_PER_SEC << endl;
    return 0;
}
