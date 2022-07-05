#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
const int MAXN = 1000000;
const int MAXM = 2000000000;
int N, M, Answer;
int A[MAXN];
int max_value;

void binary_search();

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		max_value = max(max_value, A[i]);
	}
	binary_search();
	cout << Answer;
	return 0;
}

void binary_search(){
	int start = 0;
	int end = max_value;
	int mid = 0;
	while (start<= end) {
		mid = (start + end) / 2;

		long long cnt = 0;
		for (int i = 0; i < N; i++) {
			if(A[i] > mid) cnt += (A[i] - mid);
		}
		if (cnt >= M) {
			Answer = mid;
			start = mid + 1;
		}
		else end = mid - 1;
	}
	
}