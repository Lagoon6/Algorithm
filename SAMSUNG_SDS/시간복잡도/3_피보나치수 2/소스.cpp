#include<iostream>

using namespace std;


int N;
long long memo[100] = { 0,1, };
long long f(int x);
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	cout << f(N);
	return 0;
}

long long f(int x) {
	if (x == 1 || x==0)
		return memo[x];
	else if (memo[x] == 0) 
		memo[x] = f(x - 1) + f(x - 2);
	return memo[x];
}