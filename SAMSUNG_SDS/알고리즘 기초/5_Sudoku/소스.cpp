#include<iostream>
using namespace std;

int MAP[9][9];

bool line(int x, int y, int k) {
	for (int i = 0; i < 9; i++) {
		if (MAP[x][i] == k || MAP[i][y] == k) return false;
	}
	return true;
}

bool box(int x, int y, int k) {
	int nx = (x / 3) * 3;
	int ny = (y / 3) * 3;
	for (int i = nx; i < nx + 3; i++) {
		for (int j = ny; j < ny + 3; j++) {
			if (MAP[i][j] == k) return false;
		}
	}
	return true;
}

void backtracking(int cnt) {
	if (cnt == 81) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << MAP[i][j] << ' ';
			}
			cout << '\n';
		}
		exit(0);
	}

	int A = cnt / 9;
	int B = cnt % 9;

	if (MAP[A][B] == 0) {
		for (int K = 1; K <= 9; K++) {
			if (line(A, B, K) && box(A, B, K)) {
				MAP[A][B] = K;
				backtracking(cnt + 1);
				MAP[A][B] = 0; //흰색 -> 회색 -> 검은색
			}

		}
	}
	else backtracking(cnt + 1);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> MAP[i][j];
		}
	}
	backtracking(0);
	return 0;
}