//벨만포드
#include<iostream>
#include<climits>
using namespace std;
const int MAXN = 501;
const int MAXM = 6001;

int N, M;
struct e_t {
	int a, b, c;
} E[MAXM];
long long Visited[MAXN];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	for (int i = 1; i <= N; i++) Visited[i] = INT_MAX;
	for (int i = 1; i <= M; i++) {
		cin >> E[i].a >> E[i].b >> E[i].c;
	}
	Visited[1] = 0;
	bool isNegativeCycle = false; 
	// N-1 만큼 돌리기
	for (int i = 1; i < N; i++) {
		for (int j = 1; j <= M; j++) {
			if (Visited[E[j].a] < INT_MAX && Visited[E[j].a] + E[j].c < Visited[E[j].b]) {
				Visited[E[j].b] = Visited[E[j].a] + E[j].c;
			}
		}
	}
	//음수 사이클 확인을 위해 한번 더 돌리기
	for (int j = 1; j <= M; j++) {
		if (Visited[E[j].a] < INT_MAX && Visited[E[j].a] + E[j].c < Visited[E[j].b]) {
			isNegativeCycle = true;
			break;
		}
	}
	if (isNegativeCycle) cout << -1 << "\n";
	else {
		for (int i = 2; i <= N; i++) {
			cout << (Visited[i]== INT_MAX ? -1 : Visited[i])<< "\n";
		}
	}
	return 0;
}
