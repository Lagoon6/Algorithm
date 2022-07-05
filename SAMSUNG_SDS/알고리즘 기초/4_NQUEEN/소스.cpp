#include<iostream>
#include<vector>

using namespace std;
const int MAXN = 15;
vector<bool> visit(MAXN); //가로 
vector<bool> visit2(MAXN + MAXN); //오른쪽 위
vector<bool> visit3(MAXN + MAXN); //오른쪽 아래
int Answer, N;
void check(int x);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	Answer = 0;
	check(0);
	cout << Answer;
	return 0;
};

void check(int x) {
	if (x == N) {
		Answer++;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (visit[i] || visit2[x + i] || visit3[x - i + N - 1]) continue;
		visit[i] = true;
		visit2[x + i] = true;
		visit3[x - i + N - 1] = true;

		check(x + 1);
		visit[i] = false;
		visit2[x + i] = false;
		visit3[x - i + N - 1] = false;
		}
	}
