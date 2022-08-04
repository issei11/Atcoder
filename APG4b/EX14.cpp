#define _GLIBCXX_DEBUG //配列において[]で範囲外を参照したときにエラーを出してくれる
#include <bits/stdc++.h>
using namespace std;

int main(){
    int A,B,C;
    cin >> A >> B >> C;
    int ma = max(max(A,B),C);
    int mi = min(min(A,B),C);
    cout << ma-mi << endl;
}