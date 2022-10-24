#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int a,b,c;
    cin>>a>>b>>c;
    int count=0;
    for(int i=1;i<=min(a,min(b,c));i++)
    {
        if(a%i==0 && b%i==0 && c%i==0)
        {
            count++;
        }
    }
    cout<<count;

    
}
