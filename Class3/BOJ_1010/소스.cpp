#include<iostream>

using namespace std;
int T, N, M;long long ans = 1;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		long long ans = 1;

		int r = 1;
		for (int i = M; i > M - N; i--) {
			ans *= i;
			ans /= r++;
		}
		cout << ans << "\n";
	}

	return 0;
}