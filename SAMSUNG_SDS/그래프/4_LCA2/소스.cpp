#include<iostream>
#include<vector>
#include<queue>

using namespace std;
const int MAXN = 100001;
int N, M; //N: 노드개수(1~N), M:질문의 개수
int a, b; // 입력 받은 노드 정보
vector<int> A[MAXN];
int Depth[MAXN];
queue<int> q;
int Parent[18][MAXN]; //2^17 = 131072  
int LCA(int a, int b);

int main() { //testcase loop count 초기화 고려하기
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	//전역변수로 정의 된 배열을 모두 0 이나 -1로 초기화하는 방법
	//memset(Parent,0,sizeof Parent);
	for (int i = 1; i < N; i++) { //인접리스트 생성
		cin >> a >> b;
		A[a].push_back(b);
		A[b].push_back(a);
	}
	//루트노드 부터 거리구하기(depth)
	//BFS를 이용하여 Depth 구함. 탐색의 시작은 Root
	for (int i = 1; i <= N; i++) Depth[i] = -1;
	q.push(1); 
	Depth[1] = 0;
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		for (int next : A[cur]) {
			if (Depth[next] == -1) { //미방문시 탐색
				q.push(next);
				Depth[next] = Depth[cur] + 1;
				Parent[0][next] = cur; // !!!!
			}
		}
	}

	//점핑테이블(희소 테이블) 만들기
	for (int r = 1; r < 18; r++) {
		for (int i = 1; i <= N; i++) {
			Parent[r][i] = Parent[r - 1][Parent[r - 1][i]]; // Parent[r][i]는 Parent[r-1][i]의 2^(r-1)번쨰 부모
		}
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b; // a,b 의 LCA 로직 구하기
		cout << LCA(a, b) << "\n";
	}


	return 0;
}

int LCA(int a, int b) {
	//Step1 : Depth 맞추기
	//항상 a의 depth가 크도록 함
	if (Depth[a] < Depth[b]) { //SWAP ^= 쓰면 같은 값 SWAP할때 error 주의
		int tmp = a;
		a = b;
		b = tmp;
	}
	int diff = Depth[a] - Depth[b];
	for (int r = 0; diff >0; r++) {
		if (diff & 1) { //비트 and 연산
			a = Parent[r][a];
		 }
		diff >>= 1; //오른쪽 시프트 (한칸 내려감)
	}
	//diff가 10 = 2^3 + 2^1. == 10 -> 2진수 표현 1010(2의 3제곱1/ 2의 2제곱0/ 2의 제곱 1/ 2의 1제곱 0) 
	//Step2 : LCA찾기
	while (a != b) {
		int r;
		for (r = 0; r < 18; r++) {
			if (Parent[r][a] == Parent[r][b]) break;
		}
		if(r > 0) --r;
		a = Parent[r][a];
		b = Parent[r][b];
	}
	return a;
}