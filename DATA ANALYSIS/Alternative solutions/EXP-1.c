int main() {
    int t;
    cin>>t;
    while(t--){
        
        int w1,w2,w3,w4;
        cin>>w1>>w2>>w3>>w4;
        if(w1==w2 && w1==w3 && w1==w4) 
            cout<<"0\n";
        else if (w1==w2 && w2!=w3 && w3!=w4)
            cout<<"2\n";
        else if ( w1!=w2 && w2==w3 && w3!=w4)
            cout<<"2\n";
        else if ( w1!=w2 && w2!=w3 && w3==w4)

            cout<<"2\n";
        else if ( w1==w2 && w1!=w3 && w2!=w4)
            cout<<"2\n";
        else if ( w1!=w2 && w1==w3 && w2!=w4)

            cout<<"2\n";
        else if ( w1!=w2 && w1!=w3 && w2==w4)
            cout<<"2\n";
        else if ( w1!=w2 && w1!=w3 && w1!=w4 && w2!=w3 && w2!=w3 && w3!=w4)
            cout<<"2\n";
        else 
            cout<<"1\n";
        }
        
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
