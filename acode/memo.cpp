#include <iostream>
#define int long long
using namespace std;

int f(int a, int b) {
	return a * a * a * a * a - b * b * b * b * b;
}

signed main() {
	int x;
	cin >> x;
	
	//a = b + iとおく
	for (int i = 1; i <= 240; i++) {
		//f(b) = (b + i)^5 - b^5 (b:実数, i:非負整数)を考えると、b = -i / 2のとき最小値を取る. 
		//(wolfram alphaというサイトで計算）
		//また、b <= -i / 2の範囲ではbを小さくするほどf(b)は大きくなる。
		//b > -i / 2の範囲ではbを大きくするほどf(b)は大きくなる。
		
		//b <= -i / 2の範囲 (について、f(b) <= x (解説にならえば右辺は10^9としてもよい）となる最小のbまで探索
		//c++の場合、-5 / 2 = -2になるらしい。つまり(負の数) / (正の数)は「小数切り上げ」になってしまう。
		//今回は、小数を切り下げたいので、-(i + 1) / 2からスタートにする。i = 5のときはb = -3からスタートということ。
		for (int b = -(i + 1) / 2; ; b--) {
			int res = f(b + i, b);
			if (res > x) break;
			if (res == x) { cout << b + i << " " << b << endl; return 0; }
		}
		
		//b >= i / 2の範囲について、f(b) <= 10^9 (解説にならえば右辺は10^9としてもよい）となる最大のbまで探索
		for (int b = -(i + 1) / 2 + 1; f(b + i, b) <= x; b++) {
			cerr << b + i << ", " << b << endl;
			int res = f(b + i, b);
			if (res > x) break;
			if (res == x) { cout << b + i << " " << b << endl; return 0; }
		}
	}
	return 0;
}

