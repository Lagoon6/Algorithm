#include<iostream>
#include<queue> //In-dgree가 0이되는 정점을 push/pop하는 자료구조 공간
#include<vector>
using namespace std;
const int MAXN = 32001;
const int MAXM = 100001;

int N, M, a, b;
int indegree[MAXN]; // 해당 정점에 대한 In-degree차수 저장
vector<int> A[MAXN]; //인접리스트 : 정적 별로 크기가 다르므로 동적 배열(리스트)
queue<int> q; //In-dgree 0이 되는 정점 저장 
int Answer[MAXN],idx; // 정답순서

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	//input
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		A[a].push_back(b); //방향성 있는 간선이므로 한곳만 추가.
		++indegree[b]; // a->b 이믈 b의 In-degree 증가
	}
	//processing
	for (int i = 0; i <= N; i++) {
		if (indegree[i] == 0) q.push(i);
	}
	while (!q.empty()) { //q에 남아있는 정점이 하나도 없을떄까지 계속 진행
		int cur = q.front();
		q.pop();
		Answer[idx++] = cur;
		for (int next : A[cur]) { //cur 가 화살을 쏘아 맞는 정점 탐색,for-each로 하나씩 불러냄;
			if (--indegree[next]==0) q.push(next);
		}
	}
	for (int i = 1; i < idx; i++) {
		cout << Answer[i]<< " ";
	}
	return 0;
}
