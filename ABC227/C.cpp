#define _GLIBCXX_DEBUG //配列において[]で範囲外を参照したときにエラーを出してくれる
#include <bits/stdc++.h>
using namespace std;

int main(){
    long long N;
    cin >> N;
    long long A = 1;
    long long B = 1;
    long long C = 1;
    long long D = 0;
    long long ans = 0;
    while (A*A*A <= N){
        B = A;
        while (A*B*B <= N){
            ans += N/(A*B) - B + 1;
            B++;
        }
        A++;
    }
    cout << ans << endl;
}