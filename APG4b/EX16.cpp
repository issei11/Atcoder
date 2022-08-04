#define _GLIBCXX_DEBUG //配列において[]で範囲外を参照したときにエラーを出してくれる
#include <bits/stdc++.h>
using namespace std;

int main(){
    vector <int> vec(5);
    int flag = 0;
    for (int i = 0; i < vec.size(); i++)
    {
        cin >> vec.at(i);
    }
    for (int i = 0; i < vec.size()-1; i++)
    {
        if (vec.at(i) == vec.at(i+1))
        {
            flag++;
        }
    }
    if(flag){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}