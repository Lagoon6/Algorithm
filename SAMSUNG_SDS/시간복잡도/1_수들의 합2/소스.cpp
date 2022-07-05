#include<iostream>


using namespace std;

const int MAXN = 10000;
const int MAXM = 300000000;
int A[MAXN];
int N, M;
int Answer;
void make(int cnt);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	make(0);
	cout << Answer;
	return 0;
}
void make(int cnt) {
	int left = 0;
	int right = 0;
	while (true){
		if (cnt == M) {
			Answer += 1;
			cnt = M + 1;
		}
		if (cnt < M)
			cnt += A[left++];
		if (cnt > M){
			right++;
			left = right;
			cnt = 0;
		if (left == N) break;
		}
	}
}
