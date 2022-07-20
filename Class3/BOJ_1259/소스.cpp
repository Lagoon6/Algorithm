#include<iostream>

using namespace std;

int N;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	while (1) {
		cin >> N;
		if (N >= 10000) {
			if (N / 10000 == N % 10) {
				N = N % 10000;
				N = N / 10;
				if (N / 100 == N % 10) cout << "yes" << "\n";
				else cout << "no" << "\n";
			}
			else cout << "no" << "\n";
		}
		else if (N >= 1000 && N < 10000) {
			if (N / 1000 == N%10){
				N = N % 1000;
				N = N / 10;
				if (N / 10 == N % 10) cout << "yes" << "\n";
				else cout << "no" << "\n";
			}
			else cout << "no" << "\n";
		}
		else if (N >= 100 && N < 1000){
			if (N / 100 == N % 10) cout << "yes" << "\n";
			else cout << "no" << "\n";
		}
		else if (N >= 10 && N < 100) {
			if (N / 10 == N % 10) cout << "yes" << "\n";
			else cout << "no" << "\n";
		}
		else if (10 > N && N > 0) cout << "yes" << "\n";
		else if (N == 0) break;
	}

	return 0;
}