#include<iostream>
#include<queue>
#include<algorithm>
#include<set>

using namespace std;
//최대 경우의수 6! (최대 6자리) 123456
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
		s.insert(str); //set로 str 중복검사
		for (int j = 0; j < str.size()-1; j++) { // str.size() -1 중요
			for (int k = j+1; k < str.size(); k++) {
				if (j != 0 || str[k] != '0') { // 이유 i<= i < j <=M 
					swap(str[j], str[k]); //위치 바꾸고
					q.push(str); //바꾼거 집어놓고
					swap(str[j], str[k]); //원위치
				}
			}
		}
	}
}