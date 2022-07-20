#include<iostream>
#include<climits>
using namespace std;

inline int mymin(int a, int b) { return a < b ? a : b; }
int N, Row[501], Col[501];
int D[501][501]; // D[i][j] : i번째 행렬부터 j번째 행렬까지 곱했을떄 필요한 '최소'곱셈연산수
int main() {
	ios::sync_with_stdio(false);
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> Row[i] >> Col[i];
	}
	//DP 테이블을 만드는 순서
	// D[1][2], D[2][3] ....D[N-1][N] step =1
	// D[1][3] , D[2][4] ....D[N-2][N] step =2
	// D[1][N] step =N-1

	// ABCD: A(BCD), (AB)(CD), (ABC)D
	for (int step = 1; step < N; step++) {
		for (int start = 1; start + step <= N; start++) {
			D[start][start + step] = INT_MAX;
			for (int mid = start; mid < start + step; mid++) {
				D[start][start + step] = mymin(D[start][start + step],
					D[start][mid] + D[mid + 1][start + step] + Row[start] * Col[start + step] * Col[mid]);
			}
		}
	}
	cout << D[1][N];
	return 0;
}