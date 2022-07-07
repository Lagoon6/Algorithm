#include<iostream>
#include<cmath>
#include<queue>
using namespace std;
bool IsPrimeNumber(int x);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N = 1;
	while (N) {
		cin >> N;
		for (int i = 1; i < N / 2; i++) {
			int a = 2 * i + 1;
			int b = N - a;
			if (IsPrimeNumber(a) && IsPrimeNumber(b)) {
				cout << N << " = " << a << " + " << b<<"\n";
				break;
			}
		}
	}
}

bool IsPrimeNumber(int x) {
	for (int i = 2; i <=sqrt(x); i++) {
		if (x%i == 0) return false;
	}
	return true;
}