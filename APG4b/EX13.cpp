#define _GLIBCXX_DEBUG //配列において[]で範囲外を参照したときにエラーを出してくれる
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector <int> A(N);
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    int ave = 0;
    for (int i = 0; i < N; i++){
        ave += A[i];
    }
    ave /= N;
    for (int i = 0; i < N; i++)
    {
        if (A[i] >= ave)
        {
            cout << A[i]-ave << endl;
        }
        else{
            cout << ave-A[i] << endl;
        }
    }
}