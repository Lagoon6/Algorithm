#include<iostream>

using namespace std;
int N, M;
int recursive(int x);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	cout << recursive(N) /(recursive(M) * recursive(N - M));

}
int recursive(int x) {
	if (x == 1 || x == 0 ) {
		return 1;
	}
	return recursive(x - 1)*x;
}