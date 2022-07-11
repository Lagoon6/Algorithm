#include<iostream>

using namespace std;
const int MAXN = 1000001; //0포함 N+1 주의
const int MAXM = 100000;
int N, M;
int A[MAXN];
int x, a, b;
void UNION(int a, int b);
int FIND(int a);
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N + 1; i++) {
		A[i] = i;
	}
	for (int i = 0; i < M; i++) {
		cin >> x >> a >> b;
		if (x == 0) UNION(a, b);
		else {
			if (FIND(a) == FIND(b)) cout << "YES" << "\n";
			else cout << "NO" <<"\n";
		}
		
	}
	return 0;
}


void UNION(int a, int b) {
	int aRoot = FIND(a);
	int bRoot = FIND(b);
	if (aRoot > bRoot) A[aRoot] = bRoot;
	else A[bRoot] = aRoot;
}
int FIND(int a) {
	if (A[a] == a) return a;
	else return A[a] = FIND(A[a]);
}