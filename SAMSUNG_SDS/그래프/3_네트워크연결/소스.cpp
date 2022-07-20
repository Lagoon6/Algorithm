#include<iostream>
#include<algorithm>

using namespace std;
const int MAXN = 1001;
const int MAXM = 100001;
int N, M, Answer;
struct e_t {
	int a;
	int b;
	int c;
	bool operator<(const e_t &ref) const {
		return this->c < ref.c;
	}
} Edge[MAXM];
int U[MAXN];
int FIND(int a) {
	if (U[a] == a) return a;
	else return FIND(U[a]);
}
void UNION(int a, int b) {
	int aRoot = FIND(a);
	int bRoot = FIND(b);
	U[bRoot] = aRoot;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> Edge[i].a >> Edge[i].b >> Edge[i].c;
	}
	//processing( 크루스칼)
	// 1. sort 
	sort(Edge,Edge + M); // 오름차순 정렬
	// 2. edge 선택: 서로서 집합 이용
	for (int i = 1; i <= N; i++) {
		U[i] = i;
	}
	for (int i = 0; i < M; i++) {
		// 연결 확인 후 안되어 있으면 UNION
		if (FIND(Edge[i].a) != FIND(Edge[i].b)) {
			UNION(Edge[i].a, Edge[i].b);
			Answer += Edge[i].c;
		}
	}
	//print
	cout << Answer;
	return 0;
}