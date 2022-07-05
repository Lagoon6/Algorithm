#include<iostream>
#include<queue>
#include<algorithm>
#include<set>

using namespace std;
//�ִ� ����Ǽ� 6! (�ִ� 6�ڸ�) 123456
string N;
string answer ="0";
int M, K;
queue<string> q;

void bfs();

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> K;
	q.push(N);
	while (K--) bfs();
	while (!q.empty()) {
		answer = max(answer, q.front());
		q.pop();
	}
	if (answer == "0")cout << -1;
	else cout << answer;
	return 0;

}
void bfs() {
	set<string> s;
	M = q.size();

	for (int i = 0; i < M; i++) {
		string str = q.front();
		q.pop();
		if (s.count(str)) continue;
		s.insert(str); //set�� str �ߺ��˻�
		for (int j = 0; j < str.size()-1; j++) { // str.size() -1 �߿�
			for (int k = j+1; k < str.size(); k++) {
				if (j != 0 || str[k] != '0') { // ���� i<= i < j <=M 
					swap(str[j], str[k]); //��ġ �ٲٰ�
					q.push(str); //�ٲ۰� �������
					swap(str[j], str[k]); //����ġ
				}
			}
		}
	}
}