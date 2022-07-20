#include<iostream>

using namespace std;
const int INF = 123456789;

int N, M;
int A[101][101]; //인접 행렬
int a, b, c;

int main() {
	ios::sync_with_stdio;
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	cin >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i != j) A[i][j] = INF;
		}
	}
	for (int i = 1; i <= M; i++) {
		cin >> a >> b >> c;
		A[a][b] = c < A[a][b] ? c : A[a][b];
	}

	//플로이드 워셜 --> 제일 바깥 for문이 경유지 (경유지를 고정해놓고 거리 구하기므로)
	for (int k = 1; k <= N; k++) { // k: 경유지
		for (int i = 1; i <= N; i++) { // i: 출발지
			for (int j = 1; j <= N; j++) { // j:도착지
				if (A[i][j] > A[i][k] + A[k][j]) {
					A[i][j] = A[i][k] + A[k][j];
				}
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (A[i][j] == INF) cout << 0<<" ";
			else cout << A[i][j]<<" ";
		}
		cout << "\n";

	}
	return 0;
}