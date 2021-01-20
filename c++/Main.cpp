#include<iostream>
using namespace std;
int main(){
    long a = 10;
    long c = 10;
    long *b = &a;
    long *d = &c;
    cout<<&b<<endl;
    cout<<&d<<endl;
}