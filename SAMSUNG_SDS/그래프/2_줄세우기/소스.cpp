#include<iostream>
#include<queue> //In-dgree�� 0�̵Ǵ� ������ push/pop�ϴ� �ڷᱸ�� ����
#include<vector>
using namespace std;
const int MAXN = 32001;
const int MAXM = 100001;

int N, M, a, b;
int indegree[MAXN]; // �ش� ������ ���� In-degree���� ����
vector<int> A[MAXN]; //��������Ʈ : ���� ���� ũ�Ⱑ �ٸ��Ƿ� ���� �迭(����Ʈ)
queue<int> q; //In-dgree 0�� �Ǵ� ���� ���� 
int Answer[MAXN],idx; // �������

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	//input
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		A[a].push_back(b); //���⼺ �ִ� �����̹Ƿ� �Ѱ��� �߰�.
		++indegree[b]; // a->b �̹� b�� In-degree ����
	}
	//processing
	for (int i = 0; i <= N; i++) {
		if (indegree[i] == 0) q.push(i);
	}
	while (!q.empty()) { //q�� �����ִ� ������ �ϳ��� ���������� ��� ����
		int cur = q.front();
		q.pop();
		Answer[idx++] = cur;
		for (int next : A[cur]) { //cur �� ȭ���� ��� �´� ���� Ž��,for-each�� �ϳ��� �ҷ���;
			if (--indegree[next]==0) q.push(next);
		}
	}
	for (int i = 1; i < idx; i++) {
		cout << Answer[i]<< " ";
	}
	return 0;
}
