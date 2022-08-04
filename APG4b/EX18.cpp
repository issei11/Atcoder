#define _GLIBCXX_DEBUG //配列において[]で範囲外を参照したときにエラーを出してくれる
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,M;
    cin >> N >> M;

    vector<int> A(M,0),B(M,0);
    for (int i=0;i<M;i++){
        cin >> A.at(i) >> B.at(i);
    }

    vector<vector<char> > R(N,vector<char>(N,'-'));

    for(int i=0;i<M;i++){
        R.at(A.at(i)-1).at(B.at(i)-1) = 'o';
        R.at(B.at(i)-1).at(A.at(i)-1) = 'x';
    }

    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            if (j<N-1){
                cout << R.at(i).at(j) << ' ';
            }
            else{
                cout << R.at(i).at(j) << endl;
            }
        }
    }
}