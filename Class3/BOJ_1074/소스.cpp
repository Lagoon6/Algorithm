#include<iostream>
#include<cmath>

using namespace std;

int N, r, c,Ans;

void Answer(int x,int y, int z);
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N >> r >> c;
	Answer(N,r,c);
	cout << Ans;
	return 0;
}
void Answer(int x, int y, int z) {
	if (x == 0) return;
	int len = pow(2, x - 1);
	int cnt = len * len;

	if (y/len == 0 && z/len == 0){
		Answer(x - 1, y % len, z % len);
	}
	if (y / len == 0 && z / len == 1){
		Ans += cnt;
		Answer(x - 1, y % len, z % len);
	}
	if (y/len == 1 && z/len == 0){
		Ans += cnt * 2;
		Answer(x - 1, y % len, z % len);
	}
	if (y/len == 1 && z/len == 1) {
		Ans += cnt * 3;
		Answer(x - 1, y % len, z % len);
	}

}