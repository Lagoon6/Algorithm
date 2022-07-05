#include<iostream>
#include<string>
#include<cstring>
#include<utility>
#include<algorithm>

using namespace std;
const int MAXN = 50;
const int MAXM = 50;
const int dx[4] = { -1,0,1,0 };
const int dy[4] = { 0,-1,0,1 };

int N, M, Answer = 0;
int MAP[MAXN][MAXM];
int DP[MAXN][MAXM];
bool Visit[MAXN][MAXM];
string S;

void Input();
void backtracking(int depth, pair<int, int> pos);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    Input();

    backtracking(1, make_pair(0, 0));
    cout << Answer;
    
    return 0;
}

void Input() {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> S;
        for (int j = 0; j < M; j++) {
            if (S[j] == 'H') {
                MAP[i][j] = 0;
            }
            else {
                MAP[i][j] = S[j] - '0';
            }
        }
    }
}

void backtracking(int depth, pair<int, int> pos) {
    Answer = max(depth, Answer);
    DP[pos.first][pos.second] = depth;

    for (int i = 0; i < 4; i++) {
        int nx = pos.first + dx[i] * MAP[pos.first][pos.second];
        int ny = pos.second + dy[i] * MAP[pos.first][pos.second];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (Visit[nx][ny]) {
                cout << -1;
                exit(0);
            }
            if (DP[nx][ny] > 0 && depth < DP[nx][ny]) continue;
            if (MAP[nx][ny] != 0) {
                Visit[nx][ny] = true;
                backtracking(depth + 1, make_pair(nx, ny));
                Visit[nx][ny] = false;
            }
        }
    }

}