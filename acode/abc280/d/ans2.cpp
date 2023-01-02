#include <bits/stdc++.h>
using namespace std;

int main() {
	long long k,p,a,n,x,ans=1;
	cin >> k;
	for(p=2;(p*p)<=k;p++){
		a=0;
		while(k%p==0)k /= p, a++;
		n=0;
		while(a>0){
			n+=p; // N' = pi, 2pi, ....
			x=n;
			while(x%p==0)x /= p,a--; // recursion
		}
		ans=max(ans,n);
	}
	ans=max(ans,k);
	cout << ans <<endl;
	return 0;
}

// without using binary search
// https://atcoder.jp/contests/abc280/editorial/5330
