#include<iostream>
#include<vector>
#include<queue>

using namespace std;
const int MAXN = 100001;
int N, M; //N: ��尳��(1~N), M:������ ����
int a, b; // �Է� ���� ��� ����
vector<int> A[MAXN];
int Depth[MAXN];
queue<int> q;
int Parent[18][MAXN]; //2^17 = 131072  
int LCA(int a, int b);

int main() { //testcase loop count �ʱ�ȭ ����ϱ�
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	//���������� ���� �� �迭�� ��� 0 �̳� -1�� �ʱ�ȭ�ϴ� ���
	//memset(Parent,0,sizeof Parent);
	for (int i = 1; i < N; i++) { //��������Ʈ ����
		cin >> a >> b;
		A[a].push_back(b);
		A[b].push_back(a);
	}
	//��Ʈ��� ���� �Ÿ����ϱ�(depth)
	//BFS�� �̿��Ͽ� Depth ����. Ž���� ������ Root
	for (int i = 1; i <= N; i++) Depth[i] = -1;
	q.push(1); 
	Depth[1] = 0;
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		for (int next : A[cur]) {
			if (Depth[next] == -1) { //�̹湮�� Ž��
				q.push(next);
				Depth[next] = Depth[cur] + 1;
				Parent[0][next] = cur; // !!!!
			}
		}
	}

	//�������̺�(��� ���̺�) �����
	for (int r = 1; r < 18; r++) {
		for (int i = 1; i <= N; i++) {
			Parent[r][i] = Parent[r - 1][Parent[r - 1][i]]; // Parent[r][i]�� Parent[r-1][i]�� 2^(r-1)���� �θ�
		}
	}
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b; // a,b �� LCA ���� ���ϱ�
		cout << LCA(a, b) << "\n";
	}


	return 0;
}

int LCA(int a, int b) {
	//Step1 : Depth ���߱�
	//�׻� a�� depth�� ũ���� ��
	if (Depth[a] < Depth[b]) { //SWAP ^= ���� ���� �� SWAP�Ҷ� error ����
		int tmp = a;
		a = b;
		b = tmp;
	}
	int diff = Depth[a] - Depth[b];
	for (int r = 0; diff >0; r++) {
		if (diff & 1) { //��Ʈ and ����
			a = Parent[r][a];
		 }
		diff >>= 1; //������ ����Ʈ (��ĭ ������)
	}
	//diff�� 10 = 2^3 + 2^1. == 10 -> 2���� ǥ�� 1010(2�� 3����1/ 2�� 2����0/ 2�� ���� 1/ 2�� 1���� 0) 
	//Step2 : LCAã��
	while (a != b) {
		int r;
		for (r = 0; r < 18; r++) {
			if (Parent[r][a] == Parent[r][b]) break;
		}
		if(r > 0) --r;
		a = Parent[r][a];
		b = Parent[r][b];
	}
	return a;
}