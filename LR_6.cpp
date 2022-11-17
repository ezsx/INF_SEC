
#include <iostream>
#include <vector>
#include <string.h>
#include <set>


using namespace std;

vector<vector<set<string>>> A;
int n, m;

void createObject(int at) {
    A.insert(A.begin() + at, vector<set<string>>(m, set<string>()));
}

void destroyObject(int at) {
    A[at] = vector<set<string>>(m, set<string>());
}

void createSubobject(int at) {
    for (int i = 0; i < A.size(); i++) {
        A[i].insert(A[i].begin() + at, set<string>());
    }
}

void destroySubobject(int at) {
    for (int i = 0; i < A.size(); i++) {
        A[i][at] = set<string>();
    }
}

void enterP(int o, int s, string v) {
    A[o][s].insert(v);
}

void deleteP(int o, int s, string v) {
    A[o][s].erase(v);
}

bool constaint(string* arr, string v, int size) {
    for(int i = 0; i < size; i++) {
        if (arr[i] == v) {
            return true;
        }
    }
    return false;
}

vector<string> split(string input, char ch = ' ') {
    vector<string> result = vector<string>();

    for(int i = 0; i < input.size(); i++) {
        if (input[i] == ch) {
            result.push_back("");
        } else {
            result[result.size() - 1] += input[i];
        }
    }

    return result;
}


void execute(string command) {
    string arr[4] = { "o", "w", "r", "x" };

    if (command.substr(0, 2) == "O+") {
        int index = stoi(command.substr(2, command.size() - 2));
        createObject(index);
    } else if (command.substr(0, 2) == "O-") {
        int index = stoi(command.substr(2, command.size() - 2));
        destroyObject(index);
    } else if (command.substr(0, 2) == "S+") {
        int index = stoi(command.substr(2, command.size() - 2));
        createSubobject(index);
    } else if (command.substr(0, 2) == "S-") {
        int index = stoi(command.substr(2, command.size() - 2));
        destroySubobject(index);
    } else if (constaint( arr, command.substr(0,1), 4)) {
        vector<string> args = split(command);
        int x = stoi(args[1]);
        int y = stoi(args[2]);

        if (args[0] == "+") {
            enterP(x, y, args[0].substr(0, 1));
        } else {
            deleteP(x, y, args[0].substr(0, 1));
        }
    } else {
        vector<string> args = split(command);

        if (args[0] == "if") {
            int x = stoi(split(args[3], ',')[0]);
            int y = stoi(split(args[3], ',')[1]);

            if (A[x][y].contains(args[1])) {
                long offset = args[0].size() + 1 + args[1].size() + 1 + args[2].size() + 1 + args[3].size() + 1;
                execute(command.substr(offset, command.size() - offset));
            }
        }
    }
}

int main(int argc, const char * argv[]) {

    cin >> n >> m;
    A = vector<vector<set<string>>>(n);

    for(int i = 0; i < n; i++) {
        A[i] = vector<set<string>>(m, set<string>());
    }

    string inp;
    getline(cin, inp);

    for(int x = 0; x < n; x++) {
        for(int y = 0; y < m; y++) {
            getline(cin, inp);
            A[x][y] = set<string>();
            A[x][y].insert(inp);
        }
    }

    return 0;
}
