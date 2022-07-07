#include<iostream>

using namespace std;
int A,B,A2,B2,Answer1,Answer2;
void fraction();

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >>A >> B;
	cin >> A2 >> B2;
	fraction();
	cout << Answer1 << " "<< Answer2;
	return 0;
}
void fraction() {
	Answer1 = A * B2 + A2 * B;
	Answer2 = B * B2;
	int X = Answer1;
	int Y = Answer2;
	int Z = 0;
	while (Y != 0) {
		Z = X % Y;
		X = Y;
		Y = Z;
	}
	Answer1 /= X;
	Answer2 /= X;
}