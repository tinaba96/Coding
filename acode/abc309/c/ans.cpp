// binary search


#include <bits/stdc++.h>
 
using namespace std;
 
int main(){
    int n, k; cin >> n >> k;
    vector<int> a(n), b(n);
    for(int i = 0; i < n; i++){
        cin >> a[i] >> b[i];
    }
    int ok = 1 << 30, ng = 0;
    while(abs(ok - ng) > 1){
        int mid = (ok + ng) / 2;
        long long sum = 0;
        for(int i = 0; i < n; i++){
            if(mid <= a[i]){
                sum += b[i];
            }
        }
        if(sum <= k){
            ok = mid;
        }else{
            ng = mid;
        }
    }
    cout << ok << endl;
}

