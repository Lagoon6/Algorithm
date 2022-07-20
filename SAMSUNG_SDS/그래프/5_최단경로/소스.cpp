#include <iostream>
#include<vector>
#include<queue>

using namespace std;
const int MAXV = 20001;
const int MAXE = 300001;
const int INF = 1987654321;

int V, E, START;
int a, b, c;
int visited[MAXV];
//vector<pair<int,int>> A[MAXV]; //cost에 대한 min heap 형태로 동작해야하므로
//구조체 방법도 고려 
struct e_t {
	int node;
	int cost;
	e_t(int _node, int _cost) : node(_node), cost(_cost) {}
	bool operator<(const e_t &ref) const {
		return this->cost > ref.cost; // min heap 으로 동작
	}
};
vector<e_t> A[MAXV];
priority_queue <e_t> pq;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> V >> E;
	cin >> START;
	for (int i = 0; i < E; i++) {
		cin >> a >> b >> c;
		A[a].push_back(e_t(b,c));
	}

	//processing;
	for (int i = 1; i <= V; i++) visited[i] = INF;
	visited[START] = 0;
	pq.push(e_t(START, 0));

	while (!pq.empty()) {
		e_t cur = pq.top();
		pq.pop();
		for (e_t next : A[cur.node]) {
			int cost = cur.cost + next.cost;
			if (cost < visited[next.node]) {
				visited[next.node] = cost;
				pq.push(e_t(next.node, cost));
			}
		}
	}
	for (int i = 1; i <= V; i++) {
		if (visited[i] == INF) cout << "INF" << "\n";
		else cout << visited[i] << "\n";

	}
	return 0;
}