#include<iostream>
#include<algorithm>

inline int mymax(int a, int b) { return a > b ? a : b; }
using namespace std;
int N;
int D[301];
int DP[301];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> D[i];
	DP[1] = D[1];
	DP[2] = mymax(D[2], D[1] + D[2]);
	DP[3] = mymax(D[1] + D[3], D[2] + D[3]);
	
	for (int i = 4; i <= N; i++) {
		DP[i] = mymax(D[i] + DP[i - 2], D[i] + D[i - 1] + DP[i - 3]);
	}
	cout << DP[N];
	return 0;
}