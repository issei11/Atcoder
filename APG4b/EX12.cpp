#include <bits/stdc++.h>
using namespace std;

int main(){
    string S;
    cin >> S;
    char a;
    int sum = 1;
    for(int i = 0;i<S.size();i++){
        a = S.at(i);
        if(a == '+'){
            sum++;
        }
        else if(a == '-'){
            sum--;
        }
    }
    cout << sum << endl;
}