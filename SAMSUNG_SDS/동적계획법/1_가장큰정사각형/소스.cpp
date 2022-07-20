#include<iostream>
#include<algorithm>

using namespace std;
inline int mymin(int a, int b) { return a < b ? a : b;}
int N, M;
int mat[1001][1001];
string S;

int D[1001][1001];
//D[i][j]: ������ �Ʒ� �������� [i][j]�̰� 1�θ� �̷���� ���簢���� ���� ���̰� ���� ���簢���� ����
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> M;
	int ans = 0;
	for (int i = 1; i <= N; i++) {
		cin >> S;
		for (int j = 1; j <= M; j++) {
			mat[i][j] = S[j-1] - 48;
			if (mat[i][j] == 1) ans = 1;
		}
	}
	//ù��° ���� D���� �ʱⰪ���� ����
	for (int j = 1; j <= M; j++) {
		D[1][j] = mat[1][j];
	}
	for (int i = 1; i <= N; i++) {
		D[i][1] = mat[i][1];
	}
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			if (i == 1 || j == 1) continue;
			if (mat[i][j] == 0) D[i][j] = 0;
			else {
				//�ٷ� ���� D[i][j-1], �ٷ� ���� D[i-1][j], �ٷ� ���� �� �밢�� D[i-1][j-1]
				// �� �� ���� �� �� ���� ���� ���� ������ �� �ۿ� ����.
				D[i][j] = mymin(mymin(D[i][j - 1], D[i - 1][j]), D[i - 1][j - 1]) + 1;
				ans = max(D[i][j], ans);
			}
			
		}
	}
	cout << ans*ans;

	return 0;
}