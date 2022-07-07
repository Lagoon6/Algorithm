#include<iostream>
using namespace std;
const int MAXN = 1000;
int N, K, Answer;
int A[MAXN];

void eratos();
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> K;
	for (int i = 0; i < N-1; i++) {
		A[i] = (2+i);
	}
	eratos();
	cout << Answer;
	return 0;
}


void eratos() {
	int cnt = 0;
	for (int i = 0; i < N-1; i++) {
		int x = A[i];
		for (int j = i; j < N-1; j++) {
			if (A[j] != 0 && x != 0 && A[j]%x == 0 ) {
				cnt += 1;
				if (cnt == K) {
					Answer = A[j];
					i = N;
					j = N;
				}
				A[j] = 0;
			}
		}
	}
}