#include<iostream>
#include <cmath>
using namespace std;
int N, x, y;
int arr[51][2] = {};
int result[51];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i][0] >> arr[i][1];
		result[i] = 1;
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1])
				result[i]++;
		}
	}

	for (int i = 0; i < N; i++)
		cout << result[i] << " ";
	cout << '\n';
	return 0;
}