#include<iostream>
#include<algorithm>
#include<queue>


using namespace std;
int N, K,Depth, tmp;
queue<int> q;
int A[100001];
int Answer(int x);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> K;
	Answer(N);
	cout << Depth-1;
	return 0;
}

int Answer(int x) {
	q.push(x);
	bool stop = true;
	A[x] = 1;
	while (stop) {
		tmp = q.front();
		q.pop();
		if (tmp == K) {
			Depth = A[tmp];
			stop = false;
		}
		if (A[tmp-1] == 0 && tmp - 1 <= 100000 && tmp-1 >=0) {
			q.push(tmp - 1);
			A[tmp - 1] = A[tmp] + 1;
		}
		if (A[tmp + 1] == 0 && tmp + 1 <= 100000 && tmp + 1 >=0) {
			q.push(tmp + 1);
			A[tmp + 1] = A[tmp]+ 1;
		}
		if (A[tmp*2] == 0 && tmp*2 <= 100000 && tmp*2 >=0) {
			q.push(tmp*2);
			A[tmp*2] = A[tmp] + 1;
		}
	}
	return Depth;
}