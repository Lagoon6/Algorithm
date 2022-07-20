#include<iostream>

using namespace std;

const int MAXN = 5000;
int N;
int Answer;


void optimize(int x);
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N;
	optimize(N);
	cout << Answer;
	return 0;
}
void optimize(int x) {
	int Y = x/5;
	while (1) {
		if ( Y < 0) {
			Answer = -1;
			break;
		}
		if ((x - (5 * Y)) % 3 == 0) {
			Answer = Y + (x - (5 * Y)) / 3;
			break;
		}
		Y--;
	}
	
}