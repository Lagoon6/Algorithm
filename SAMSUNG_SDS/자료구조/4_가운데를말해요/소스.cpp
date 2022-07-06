#include<iostream>
#include<queue>
#include<vector>

using namespace std;
int N,NUM;
priority_queue<int> pq1; //자동으로 큰수부터 정렬(내림차순)
priority_queue<int, vector<int>, greater<int>> pq2; //작은수부터정렬(오름차순)

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	while (N--) {
		cin >> NUM;
		if (pq1.size() > pq2.size()) {
			pq2.push(NUM);
		}
		else pq1.push(NUM);
		if (pq1.size() > 0 && pq2.size() > 0) {
			if (pq1.top() > pq2.top()) {
				int pq1top = pq1.top();
				int pq2top = pq2.top();
				pq1.pop();
				pq2.pop();
				pq1.push(pq2top);
				pq2.push(pq1top);
			}
		}
		cout << pq1.top()<<'\n';
	}
	return 0;
}

