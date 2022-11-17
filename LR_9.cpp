
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <math.h>

using namespace std;

struct Edge {
    int fromSubject, toSubject;
    set<string> rules;

    Edge(int from, int to, set<string> rules) {
        this->fromSubject = from;
        this->toSubject = to;
        this->rules = rules;
    }
};

struct Graph {
    set<int> activeObjects;
    int objectsCount;
    vector<Edge> edges;

    Graph(int count, set<int> active, vector<Edge> edges) {
        this->objectsCount = count;
        this->edges = edges;
        this->activeObjects = active;
    }

    bool isAccess(set<string> rules, int subject, int object) {
        vector<int> allObjects;
        for(int i = 0; i < objectsCount; i++) {
            allObjects.push_back(i);
        }

        return findAllSubsets(rules, allObjects, object, [this, subject](vector<int> objects) {
            for(int objectIndex = 0; objectIndex < objects.size(); objectIndex++) {
                if (!isTgWayExist(subject, objects[objectIndex])) {
                    return false;
                }
            }

            return true;
        });
    }

    vector<set<int>> findIslands() {
        vector<set<int>> result;
        set<int> usedObjects;

        for(int objIndex = 0; objIndex < objectsCount; objIndex++) {
            if (!usedObjects.contains(objIndex) && activeObjects.contains(objIndex)) {
                set<int> islandObjects;

                usedObjects.insert(objIndex);
                islandObjects.insert(objIndex);

                for(int isObjIndex = 0; isObjIndex < objectsCount; isObjIndex++) {
                    if (!usedObjects.contains(isObjIndex)) {
                        if (isInIsland(islandObjects, isObjIndex)) {
                            islandObjects.insert(isObjIndex);
                            usedObjects.insert(isObjIndex);
                        }
                    }
                }

                result.push_back(islandObjects);
            }
        }

        return result;
    }

    void findBridges(vector<set<int>> islands) {
        //TODO: realization
    }

private:
    bool isInIsland(set<int> island, int object) {
        for(auto islandObject = island.begin(); islandObject != island.end(); islandObject++) {
            if (!(isTgWayExist(*islandObject, object))) {
                return false;
            }
        }

        return true;
    }

    bool isTgWayExist(int from, int to) {
        set<int> objects;
        return isTgWayExist(from, to, &objects);
    }

    bool isTgWayExist(int from, int to, set<int> *visitedObjects) {
        if (from == to) return true;

        vector<int> neighbours = findNeighbours(from);

        for(auto neighbour = neighbours.begin(); neighbour != neighbours.end(); neighbour++) {
            int edgeIndex = findEdge(from, *neighbour);
            if ((edges[edgeIndex].rules.contains("t") || edges[edgeIndex].rules.contains("g")) && !visitedObjects->contains(*neighbour)) {
                visitedObjects->insert(*neighbour);
                bool isExist = isTgWayExist(*neighbour, to, visitedObjects);
                visitedObjects->erase(*neighbour);

                if (isExist) {
                    return true;
                }
            }
        }

        return false;
    }

    vector<int> findNeighbours(int object) {
        vector<int> neighbours;

        for(int objIndex = 0; objIndex < objectsCount; objIndex++) {
            for(auto edge = edges.begin(); edge != edges.end(); edge++) {
                int index = findEdge(object, objIndex);
                if (index != -1) {
                    neighbours.push_back(objIndex);
                    break;
                }
            }
        }

        return neighbours;
    }

    int findEdge(int obj1, int obj2) {
        for(auto edgeIndex = 0; edgeIndex < edges.size(); edgeIndex++) {
            if ((edges[edgeIndex].fromSubject == obj1 && edges[edgeIndex].toSubject == obj2) || (edges[edgeIndex].fromSubject == obj2 && edges[edgeIndex].toSubject == obj1)) {
                return edgeIndex;
            }
        }

        return -1;
    }

    bool findAllSubsets(set<string> rules, vector<int> objects, int toObject, const function<bool(vector<int>)> &function) {
        for(int subsetIndex = 0; subsetIndex < pow(2, objects.size()); subsetIndex++) {
            vector<int> objectsSubset;
            set<string> subsetRules;

            //find subset
            for(int objectIndex = 0; objectIndex < objects.size(); objectIndex++) {
                if (((subsetIndex >> objectIndex) & 1) == 1) {
                    objectsSubset.push_back(objects[objectIndex]);
                }
            }
            //find subsetRules
            for(auto obj = objectsSubset.begin(); obj != objectsSubset.end(); obj++) {
                int index = findEdge(*obj, toObject);
                if (index != -1) {
                    for(auto rule = edges[index].rules.begin(); rule != edges[index].rules.end(); rule++) {
                        subsetRules.insert(*rule);
                    }
                }
            }

            if (isSubset(subsetRules, rules) && function(objectsSubset)) {
                return true;
            }
        }

        return false;
    }

    bool isSubset(set<string> s, set<string> ss) {
        for(auto rule = ss.begin(); rule != ss.end(); rule++) {
            if (!(s.contains(*rule))) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    Graph g = Graph(4, set<int>{ 0, 1, 2 }, vector<Edge>{
        Edge(0, 1, { "r", "t" }),
        Edge(0, 2, { "w", "g" }),
        Edge(1, 3, { "r" }),
        Edge(2, 3, { "w" }),
    });

    cout << g.isAccess({"r", "w" }, 0, 3); // ок, из можно получить через субъекты 1 и 2
    cout << g.isAccess({"r", "w", "e" }, 0, 3); // не ок, права e нет ни у кого

    g = Graph(4, set<int>{ 0, 1, 2 }, vector<Edge>{
        Edge(0, 1, { "r" }),
        Edge(0, 2, { "w", "g" }),
        Edge(1, 3, { "r" }),
        Edge(2, 3, { "w" }),
    });

    cout << g.isAccess({"r", "w" }, 0, 3) << endl; // не ок, у субьекта 1 нет права t или g

    vector<set<int>> islands = g.findIslands(); // 2 острова - 0, 1 и 2

    for(auto island = islands.begin(); island != islands.end(); island++) {
        for(auto obj = island->begin(); obj != island->end(); obj++) {
            cout << *obj << " ";
        }
        cout << endl;
    }

    return 0;
}
