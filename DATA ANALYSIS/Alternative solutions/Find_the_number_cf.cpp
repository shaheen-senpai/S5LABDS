#include <bits/stdc++.h>
using namespace std;

//this code finds the number of cf. this code uses C++ language, which is a high-level general-purpose programming language created by Danish computer scientist Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".

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
