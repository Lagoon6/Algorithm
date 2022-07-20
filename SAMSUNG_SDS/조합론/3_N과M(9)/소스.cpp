#include<iostream>
#include<algorithm>

using namespace std;
const int MAXN = 8;

int N, M;
int A[MAXN];
int VISITED[MAXN];
void backtracking(int index);
int cnt;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	sort(A, A + N);
	return 0;
}
void backtracking(int index) {
    if (cnt == 2) {		// 탈출 조건
        return;
    }
    if (VISITED[index] == true) {
        VISITED[index] = true;	// 상태변화
        backtracking(index + 1);	// 재귀호출
        VISITED[index] = false;	// 상태복구
    }
}

