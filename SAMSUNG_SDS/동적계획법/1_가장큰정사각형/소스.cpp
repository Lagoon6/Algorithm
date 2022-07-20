#include<iostream>
#include<algorithm>

using namespace std;
inline int mymin(int a, int b) { return a < b ? a : b;}
int N, M;
int mat[1001][1001];
string S;

int D[1001][1001];
//D[i][j]: 오른쪽 아래 꼭짓점이 [i][j]이고 1로만 이루어진 정사각형중 가장 넓이가 넓은 정사각형의 넓이
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	int ans = 0;
	for (int i = 1; i <= N; i++) {
		cin >> S;
		for (int j = 1; j <= M; j++) {
			mat[i][j] = S[j-1] - 48;
			if (mat[i][j] == 1) ans = 1;
		}
	}
	//첫번째 행의 D값을 초기값으로 저장
	for (int j = 1; j <= M; j++) {
		D[1][j] = mat[1][j];
	}
	for (int i = 1; i <= N; i++) {
		D[i][1] = mat[i][1];
	}
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			if (i == 1 || j == 1) continue;
			if (mat[i][j] == 0) D[i][j] = 0;
			else {
				//바로 왼쪽 D[i][j-1], 바로 위쪽 D[i-1][j], 바로 왼쪽 위 대각선 D[i-1][j-1]
				// 이 세 가지 값 중 가장 작은 값에 의존될 수 밖에 없음.
				D[i][j] = mymin(mymin(D[i][j - 1], D[i - 1][j]), D[i - 1][j - 1]) + 1;
				ans = max(D[i][j], ans);
			}
			
		}
	}
	cout << ans*ans;

	return 0;
}