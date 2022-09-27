#include <iostream>
#include <tuple>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <memory>

using namespace std;

class Network_member {
public:
    tuple<int, int, int> points;
    int id;
    vector<shared_ptr<Network_member>> NM_list;
    vector<tuple<string, tuple<int, int>>> Comp_list;

    Network_member(int id, int x, int y, int z) {
        this->id = id;
        points = make_tuple(x, y, z);
    }
};

vector<tuple<string, tuple<int, int>>>
getComp_list(vector<shared_ptr<Network_member>> NM_list, vector<tuple<string, tuple<int, int>>> Comp_list) {

    for (int i = 0; i < NM_list.size(); i++) {
        int a1, b1, c1, a2, b2, c2, ap, bp, cp;
        tie(a1, b1, c1) = NM_list[i]->points;
        for (int j = i+1; j < NM_list.size(); j++) {

            if (i != j) {
                tie(a2, b2, c2) = NM_list[j]->points;
                ap = abs(a1 - a2);
                bp = abs(b1 - b2);
                cp = abs(c1 - c2);
                if ((ap == 0) and (bp != 0 and cp != 0) and (bp or cp) != 0) {
                    Comp_list.push_back(make_tuple("a", make_tuple(NM_list[i]->id, NM_list[j]->id)));
                }
                if ((bp == 0) and (ap != 0 and cp != 0) and (ap or cp) != 0) {
                    Comp_list.push_back(make_tuple("b", make_tuple(NM_list[i]->id, NM_list[j]->id)));
                }
                if ((cp == 0) and (ap != 0 and bp != 0) and (ap or bp) != 0) {
                    Comp_list.push_back(make_tuple("c", make_tuple(NM_list[i]->id, NM_list[j]->id)));
                } else {
                    Comp_list.push_back(make_tuple("NONE", make_tuple(NM_list[i]->id, NM_list[j]->id)));
                }
            }
        }
    }
    return Comp_list;
}

int main() {
    vector<shared_ptr<Network_member>> NM_list;
    Network_member NM1(1, 1, 2, 3);
    Network_member NM2(2, 1, 4, 5);
    Network_member NM3(3, 1, 2, 4);
    NM_list.push_back(make_shared<Network_member>(NM1));
    NM_list.push_back(make_shared<Network_member>(NM2));
    NM_list.push_back(make_shared<Network_member>(NM3));
    vector<tuple<string, tuple<int, int>>> Comp_list;
    Comp_list = getComp_list(NM_list, Comp_list);
    int count = 0;
    for (auto i: Comp_list) {
        cout << get<0>(i) << " " << get<0>(get<1>(i)) << " " << get<1>(get<1>(i)) << endl;
        if (get<0>(i) != "NONE") {
            count++;
        }
    }


    cout<<count<<endl;

    return 0;


}
